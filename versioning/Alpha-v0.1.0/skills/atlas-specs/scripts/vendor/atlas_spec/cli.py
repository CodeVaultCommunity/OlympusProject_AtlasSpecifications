"""Command-line interface for the Atlas translator."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from .errors import AtlasError
from .registry import ALL_FORMATS, AdapterRegistry, default_registry
from .validation import Validator
from .util import atlas_content_equal, json_dumps

SUFFIXES = {".json": "json", ".md": "markdown", ".tex": "latex"}


def _guess_format(path: Path) -> str | None:
    return SUFFIXES.get(path.suffix.lower())


def _add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--version",
        dest="representation_version",
        default="Alpha-v0.1.0",
        help="representation version (default: Alpha-v0.1.0)",
    )
    parser.add_argument(
        "--resources",
        type=Path,
        default=None,
        help="resource root for files named in the Atlas resource catalog",
    )
    parser.add_argument(
        "--no-check-resources",
        action="store_true",
        help="do not open or hash resource files (limited preservation guarantee)",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="atlas-spec",
        description=(
            "Validate Atlas documents and convert between Atlas JSON, Atlas Markdown, "
            "and Atlas LaTeX. Every conversion goes through a validated Atlas JSON document."
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate", help="validate one Atlas instance")
    validate.add_argument("input", type=Path)
    validate.add_argument(
        "--format",
        choices=ALL_FORMATS,
        default=None,
        help="source representation (inferred from the file suffix when omitted)",
    )
    _add_common(validate)

    convert = sub.add_parser("convert", help="convert one Atlas instance")
    convert.add_argument("input", type=Path)
    convert.add_argument("-o", "--output", type=Path, required=True)
    convert.add_argument("--from", dest="source_format", choices=ALL_FORMATS, required=True)
    convert.add_argument("--to", dest="target_format", choices=ALL_FORMATS, required=True)
    convert.add_argument(
        "--no-verify",
        action="store_true",
        help="skip the post-encode decode-and-compare check",
    )
    _add_common(convert)

    package = sub.add_parser(
        "package",
        help="copy one instance and its local resources into a self-contained folder",
    )
    package.add_argument("input", type=Path)
    package.add_argument("-o", "--output", type=Path, required=True)
    package.add_argument("--from", dest="source_format", choices=ALL_FORMATS, required=True)
    package.add_argument(
        "--name",
        default=None,
        help="name of the copied instance inside the package (default: source file name)",
    )
    package.add_argument(
        "--force",
        action="store_true",
        help="overwrite an existing output directory/file",
    )
    _add_common(package)

    sub.add_parser("formats", help="list registered representation adapters")
    return parser


def _registry(args) -> AdapterRegistry:
    registry = AdapterRegistry(validator=Validator())
    return registry


def _resource_root_for(path: Path, args) -> Path:
    return (args.resources or path.parent).resolve()


def cmd_validate(args) -> int:
    source_format = args.format or _guess_format(args.input)
    if source_format is None:
        raise AtlasError("cannot infer format from suffix; pass --format")
    registry = _registry(args)
    document = registry.decode_to_atlas_json(
        args.input,
        source_format=source_format,
        representation_version=args.representation_version,
        resource_root=_resource_root_for(args.input, args),
        check_resources=not args.no_check_resources,
    )
    text = document["atlas"]["title"]["text"]
    print(
        f"valid: {args.input} ({source_format}, {args.representation_version}, "
        f"document_id={document['atlas']['document_id']}, title={text!r})"
    )
    return 0


def cmd_convert(args) -> int:
    registry = _registry(args)
    source_root = _resource_root_for(args.input, args)
    target_root = (args.resources or args.output.parent).resolve()
    document = registry.decode_to_atlas_json(
        args.input,
        source_format=args.source_format,
        representation_version=args.representation_version,
        resource_root=source_root,
        check_resources=not args.no_check_resources,
    )
    output = registry.encode_from_atlas_json(
        document,
        target_format=args.target_format,
        representation_version=args.representation_version,
        resource_root=target_root,
        check_resources=not args.no_check_resources,
    )
    if not args.no_verify:
        try:
            verified = registry.decode_to_atlas_json(
                output,
                source_format=args.target_format,
                representation_version=args.representation_version,
                resource_root=target_root,
                check_resources=not args.no_check_resources,
            )
        except AtlasError as exc:
            raise AtlasError(
                "the generated representation cannot be decoded; nothing was written. "
                + str(exc)
            ) from exc
        if not atlas_content_equal(verified, document):
            raise AtlasError(
                "post-encode verification failed: the generated representation does not "
                "recover the Atlas content. Nothing was written."
            )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        handle.write(output)
    result = "Atlas content preserved" if not args.no_verify else "verification skipped"
    if args.no_check_resources:
        result += "; resource bytes not checked"
    print(
        f"converted: {args.input} ({args.source_format}) -> {args.output} "
        f"({args.target_format}); {result}"
    )
    return 0


def cmd_package(args) -> int:
    """Prepare a self-contained publication package (instance + resource bytes)."""

    registry = _registry(args)
    source_root = _resource_root_for(args.input, args)
    document = registry.decode_to_atlas_json(
        args.input,
        source_format=args.source_format,
        representation_version=args.representation_version,
        resource_root=source_root,
        check_resources=not args.no_check_resources,
    )
    output = args.output.resolve()
    name = args.name or args.input.name
    if name in {".", ".."} or "/" in name or "\\" in name or Path(name).is_absolute():
        raise AtlasError("--name must be one file name inside the output package")
    destination = (output / name).resolve()
    try:
        destination.relative_to(output)
    except ValueError as exc:
        raise AtlasError("the instance destination escapes the package root") from exc
    if output.exists():
        if not args.force:
            raise AtlasError(
                f"output {output} already exists; pass --force to overwrite"
            )
        if args.force and output.is_dir() and any(output.iterdir()):
            # Overwrite the files this command owns; leave unrelated files alone.
            pass
    output.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(args.input, destination)

    atlas = document["atlas"]
    copied: list[str] = []
    for resource in atlas["resources"]:
        paths = [resource["path"], *(v["path"] for v in resource.get("variants", []))]
        for relative in paths:
            source = (source_root / relative).resolve()
            try:
                source.relative_to(source_root)
            except ValueError as exc:
                raise AtlasError(
                    f"resource path {relative!r} escapes the resource root"
                ) from exc
            target = (output / relative).resolve()
            try:
                target.relative_to(output)
            except ValueError as exc:
                raise AtlasError(
                    f"resource path {relative!r} escapes the package root"
                ) from exc
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            copied.append(relative)

    packaged_style = Path(__file__).resolve().parent / "templates" / "atlas.sty"
    published_style = Path(__file__).resolve().parents[3] / "implementations" / "latex" / "atlas.sty"
    style_source = packaged_style if packaged_style.is_file() else published_style
    if style_source.is_file():
        shutil.copyfile(style_source, output / "atlas.sty")

    verified = registry.decode_to_atlas_json(
        destination,
        source_format=args.source_format,
        representation_version=args.representation_version,
        resource_root=output,
        check_resources=not args.no_check_resources,
    )
    if not atlas_content_equal(verified, document):
        raise AtlasError(
            "packaged instance does not recover the validated Atlas content"
        )
    resources_status = "local resources verified" if not args.no_check_resources else "resource bytes not checked"
    print(
        f"packaged: {args.input} -> {destination} "
        f"({len(copied)} resource file(s), {resources_status})"
    )
    return 0


def cmd_formats(args) -> int:
    registry = _registry(args)
    print(f"representation version: {registry.representation_version}")
    for version, fmt in sorted(registry.adapter_factories):
        print(f"  {fmt}/{version}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            return cmd_validate(args)
        if args.command == "convert":
            return cmd_convert(args)
        if args.command == "package":
            return cmd_package(args)
        if args.command == "formats":
            return cmd_formats(args)
    except AtlasError as exc:
        for diagnostic in exc.diagnostics:
            print(diagnostic.format(), file=sys.stderr)
        return 2
    return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
