"""Structural and referential validation for Atlas Alpha-v0.1.0."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator
from jsonschema.exceptions import best_match

from .errors import AtlasValidationError, Diagnostic
from .util import sha256_file, sha256_text

SUPPORTED_SPEC_VERSION = "Alpha-v0.1.0"
SUPPORTED_PROFILE_VERSION = "Alpha-v0.1.0"
PACKAGED_SCHEMA_PATH = Path(__file__).resolve().parent / "schemas" / "atlas.schema.json"
PUBLISHED_SCHEMA_PATH = Path(__file__).resolve().parents[3] / "implementations" / "json" / "atlas.schema.json"
SCHEMA_PATH = PACKAGED_SCHEMA_PATH if PACKAGED_SCHEMA_PATH.is_file() else PUBLISHED_SCHEMA_PATH

CONCEPT_ARRAYS = {
    "actors": "actor",
    "vocabulary": "term",
    "types": "type",
    "entities": "entity",
    "tools": "tool",
    "use_cases": "use_case",
    "boundaries": "boundary",
}


class Validator:
    def __init__(self, schema_path: Path | None = None):
        path = schema_path or SCHEMA_PATH
        self.schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(self.schema)
        self.validator = Draft202012Validator(self.schema)

    def validate(
        self,
        document: dict,
        *,
        resource_root: Path | None = None,
        check_resources: bool = True,
    ) -> list[Diagnostic]:
        diagnostics = self._schema_errors(document)
        if diagnostics:
            raise AtlasValidationError(diagnostics)

        diagnostics = self._semantic_errors(document)
        if check_resources and resource_root is not None:
            diagnostics.extend(self._resource_errors(document, resource_root))
        if diagnostics:
            raise AtlasValidationError(diagnostics)
        return []

    # -- schema ---------------------------------------------------------
    def _schema_errors(self, document: dict) -> list[Diagnostic]:
        errors = sorted(self.validator.iter_errors(document), key=lambda e: list(e.absolute_path))
        result: list[Diagnostic] = []
        for error in errors:
            path = "/" + "/".join(str(part) for part in error.absolute_path)
            result.append(
                Diagnostic(
                    "ATL-E-SCHEMA",
                    error.message,
                    path if path != "/" else "document",
                )
            )
        if result:
            return result
        return []

    # -- helpers --------------------------------------------------------
    def _semantic_errors(self, document: dict) -> list[Diagnostic]:
        diagnostics: list[Diagnostic] = []
        atlas = document["atlas"]

        if atlas["spec_version"] != SUPPORTED_SPEC_VERSION:
            diagnostics.append(
                Diagnostic(
                    "ATL-E-VERSION",
                    f"unsupported Atlas specification version {atlas['spec_version']!r}; "
                    f"this translator implements {SUPPORTED_SPEC_VERSION!r}",
                    "/atlas/spec_version",
                )
            )
        if atlas["profile_version"] != SUPPORTED_PROFILE_VERSION:
            diagnostics.append(
                Diagnostic(
                    "ATL-E-PROFILE-VERSION",
                    f"unsupported profile version {atlas['profile_version']!r}; "
                    f"this implementation provides {SUPPORTED_PROFILE_VERSION!r}",
                    "/atlas/profile_version",
                )
            )
        if document.get("format") != f"atlas-json/{SUPPORTED_PROFILE_VERSION}":
            diagnostics.append(
                Diagnostic(
                    "ATL-E-FORMAT",
                    "Atlas JSON transport member 'format' must be "
                    f"'atlas-json/{SUPPORTED_PROFILE_VERSION}'",
                    "/format",
                )
            )

        ids: dict[str, str] = {}
        self._collect_ids(atlas, "$", ids, diagnostics)
        root_id = atlas["document_id"]
        if root_id in ids:
            diagnostics.append(
                Diagnostic("ATL-E-DUPLICATE-ID", f"document_id {root_id!r} is also an object id", "$")
            )
        ids[root_id] = "$.document_id"

        by_kind: dict[str, dict[str, Any]] = defaultdict(dict)
        for key, kind in CONCEPT_ARRAYS.items():
            for index, item in enumerate(atlas[key]):
                by_kind[kind][item["id"]] = item
        all_elements = {item_id for group in by_kind.values() for item_id in group}
        seen_in_structure: dict[str, str] = {}
        for section in atlas["structure"]:
            for ref in section["items"]:
                if ref not in all_elements:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"section {section['id']} references unknown element {ref!r}",
                            f"/atlas/structure/{section['id']}/items",
                        )
                    )
                elif ref in seen_in_structure:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-STRUCTURE-DUPLICATE",
                            f"element {ref!r} appears in both {seen_in_structure[ref]} "
                            f"and {section['id']}",
                            f"/atlas/structure/{section['id']}",
                        )
                    )
                else:
                    seen_in_structure[ref] = section["id"]
        for element_id in sorted(all_elements - set(seen_in_structure)):
            diagnostics.append(
                Diagnostic(
                    "ATL-E-STRUCTURE-MISSING",
                    f"element {element_id!r} is not placed in the editorial structure",
                    "/atlas/structure",
                )
            )

        # entities
        for entity in atlas["entities"]:
            entity_id = entity["id"]
            field_ids = {f["id"] for f in entity["fields"]}
            state_ids = {s["id"] for s in entity["states"]}
            validation_ids = {v["id"] for v in entity["validations"]}
            for field_id in entity["identity"]["fields"]:
                if field_id not in field_ids:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"identity of {entity_id} references unknown field {field_id!r}",
                            f"/atlas/entities/{entity_id}/identity",
                        )
                    )
            for relationship in entity["relationships"]:
                if relationship["target"] not in by_kind["entity"]:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"relationship {relationship['id']} references unknown entity "
                            f"{relationship['target']!r}",
                            f"/atlas/entities/{entity_id}/relationships",
                        )
                    )
            for transition in entity["transitions"]:
                for endpoint in (transition["from"], transition["to"]):
                    if endpoint not in state_ids:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-REF",
                                f"transition {transition['id']} references unknown state {endpoint!r}",
                                f"/atlas/entities/{entity_id}/transitions",
                            )
                        )
            for validation in entity["validations"]:
                diagnostic = self._graph_owner_error(
                    atlas, validation["flow"], "validation", validation["id"]
                )
                if diagnostic:
                    diagnostics.append(diagnostic)
            for example_id in [e["id"] for e in entity["examples"]]:
                if example_id not in ids:
                    diagnostics.append(
                        Diagnostic("ATL-E-ID", f"entity example {example_id} has no id", entity_id)
                    )

        # tools
        for tool in atlas["tools"]:
            operation_ids = {op["id"] for op in tool["operations"]}
            for operation in tool["operations"]:
                if operation["id"] not in operation_ids:
                    diagnostics.append(
                        Diagnostic("ATL-E-ID", "operation id disappeared", tool["id"])
                    )

        # graphs
        graphs = {graph["id"]: graph for graph in atlas["graphs"]}
        graph_element_ids: dict[str, set[str]] = {}
        for graph in atlas["graphs"]:
            node_ids = [node["id"] for node in graph["nodes"]]
            if len(node_ids) != len(set(node_ids)):
                diagnostics.append(
                    Diagnostic(
                        "ATL-E-DUPLICATE-NODE",
                        f"graph {graph['id']} contains duplicate node ids",
                        f"/atlas/graphs/{graph['id']}",
                    )
                )
            graph_element_ids[graph["id"]] = set(node_ids)
            for edge in graph["edges"]:
                graph_element_ids[graph["id"]].add(edge["id"])
                if edge["from"] not in set(node_ids):
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-GRAPH-EDGE",
                            f"edge {edge['id']} starts at unknown node {edge['from']!r}",
                            f"/atlas/graphs/{graph['id']}",
                        )
                    )
                if edge["to"] not in set(node_ids):
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-GRAPH-EDGE",
                            f"edge {edge['id']} ends at unknown node {edge['to']!r}",
                            f"/atlas/graphs/{graph['id']}",
                        )
                    )
            for node in graph["nodes"]:
                call = node.get("call")
                if call:
                    expected = {
                        "validation": "validation",
                        "tool": "tool",
                        "operation": "operation",
                        "use_case": "use_case",
                        "entity": "entity",
                    }[call["kind"]]
                    if not self._call_target_exists(atlas, by_kind, call, expected):
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-GRAPH-CALL",
                                f"node {node['id']} calls unknown {call['kind']} {call['id']!r}",
                                f"/atlas/graphs/{graph['id']}",
                            )
                        )
            self._check_graph_owner(atlas, by_kind, graph, diagnostics)

        # use cases
        for case in atlas["use_cases"]:
            case_id = case["id"]
            rf_ids = {rf["id"] for rf in case["functional_requirements"]}
            rnf_ids = {rnf["id"] for rnf in case["nonfunctional_requirements"]}
            outcome_ids = {o["id"] for o in case["outcomes"]}
            entity_ids = {e["id"] for e in atlas["entities"]}
            operation_owner = {
                op["id"]: tool["id"] for tool in atlas["tools"] for op in tool["operations"]
            }
            case_graph_ids = {case["flows"]["main"], *case["flows"]["subflows"]}
            for graph_id in case_graph_ids:
                if graph_id not in graphs:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"use case {case_id} references unknown flow graph {graph_id!r}",
                            f"/atlas/use_cases/{case_id}/flows",
                        )
                    )
                else:
                    self._expect_owner(
                        graphs[graph_id], "use_case", case_id, diagnostics, case_id
                    )
            for actor in case["actors"]:
                if actor["actor"] not in by_kind["actor"]:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"use case {case_id} references unknown actor {actor['actor']!r}",
                            f"/atlas/use_cases/{case_id}/actors",
                        )
                    )
            for use in case["entities"]:
                if use["entity"] not in entity_ids:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"use case {case_id} references unknown entity {use['entity']!r}",
                            f"/atlas/use_cases/{case_id}/entities",
                        )
                    )
                    continue
                entity = by_kind["entity"][use["entity"]]
                entity_validations = {v["id"] for v in entity["validations"]}
                for validation_id in use["validations"]:
                    if validation_id not in entity_validations:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-REF",
                                f"use case {case_id} applies {validation_id!r}, which does not "
                                f"belong to entity {entity['id']}",
                                f"/atlas/use_cases/{case_id}/entities",
                            )
                        )
            for use in case["tools"]:
                if use["tool"] not in by_kind["tool"]:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"use case {case_id} references unknown tool {use['tool']!r}",
                            f"/atlas/use_cases/{case_id}/tools",
                        )
                    )
                elif operation_owner.get(use["operation"]) != use["tool"]:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"use case {case_id} references operation {use['operation']!r} "
                            f"outside tool {use['tool']!r}",
                            f"/atlas/use_cases/{case_id}/tools",
                        )
                    )
            for call in case["calls"]:
                if call["use_case"] not in by_kind["use_case"]:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"use case {case_id} calls unknown use case {call['use_case']!r}",
                            f"/atlas/use_cases/{case_id}/calls",
                        )
                    )
                if call["use_case"] == case_id:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-SELF-CALL",
                            f"use case {case_id} cannot call itself",
                            f"/atlas/use_cases/{case_id}/calls",
                        )
                    )
            element_requirements: dict[str, set[str]] = {}
            graph_rf_refs: set[str] = set()
            for graph_id in case_graph_ids:
                graph = graphs.get(graph_id)
                if not graph:
                    continue
                for node in graph["nodes"]:
                    element_requirements[node["id"]] = set(node.get("requirement_refs", []))
                    graph_rf_refs.update(node.get("requirement_refs", []))
                for edge in graph["edges"]:
                    element_requirements[edge["id"]] = set(edge.get("requirement_refs", []))
                    graph_rf_refs.update(edge.get("requirement_refs", []))
            for rf in case["functional_requirements"]:
                refs = set(rf["flow_refs"])
                if not refs:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-RF-FLOW",
                            f"functional requirement {rf['id']} has no flow association",
                            f"/atlas/use_cases/{case_id}/functional_requirements",
                        )
                    )
                for ref in refs:
                    if ref not in element_requirements:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-RF-FLOW",
                                f"functional requirement {rf['id']} references {ref!r}, "
                                "which is not a node or edge of this case's flows",
                                f"/atlas/use_cases/{case_id}/functional_requirements",
                            )
                        )
                    elif rf["id"] not in element_requirements[ref]:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-RF-FLOW",
                                f"functional requirement {rf['id']} claims flow element "
                                f"{ref!r}, but that element does not list {rf['id']} in "
                                "its requirement_refs",
                                f"/atlas/use_cases/{case_id}/functional_requirements",
                            )
                        )
                for applies in rf["applies_to"]:
                    if not self._applies_to_exists(atlas, case, rf, applies, by_kind):
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-REF",
                                f"functional requirement {rf['id']} applies to unknown "
                                f"target {applies!r}",
                                f"/atlas/use_cases/{case_id}/functional_requirements",
                            )
                        )
            for ref in sorted(graph_rf_refs - rf_ids):
                diagnostics.append(
                    Diagnostic(
                        "ATL-E-RF-GRAPH",
                        f"graph of {case_id} references {ref!r}, which is absent from the "
                        "case's functional requirements list",
                        f"/atlas/use_cases/{case_id}/flows",
                    )
                )
            rf_by_id = {rf["id"]: rf for rf in case["functional_requirements"]}
            for element_id, requirements in element_requirements.items():
                for requirement_id in sorted(requirements & rf_ids):
                    if element_id not in rf_by_id[requirement_id]["flow_refs"]:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-RF-FLOW",
                                f"flow element {element_id!r} lists {requirement_id!r}, "
                                "but the requirement does not reciprocate in flow_refs",
                                f"/atlas/use_cases/{case_id}/flows",
                            )
                        )
            for rnf in case["nonfunctional_requirements"]:
                for field in ("applies_to", "references"):
                    for target in rnf.get(field, []):
                        if target not in ids:
                            diagnostics.append(
                                Diagnostic(
                                    "ATL-E-REF",
                                    f"non-functional requirement {rnf['id']} has unknown "
                                    f"{field} target {target!r}",
                                    f"/atlas/use_cases/{case_id}/nonfunctional_requirements",
                                )
                            )
                if rnf.get("reference_to"):
                    continue
                for required in ("statement", "criterion", "verification"):
                    if required not in rnf:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-RNF",
                                f"non-functional requirement {rnf['id']} defines no {required}; "
                                "a full definition or an explicit reference_to is required",
                                f"/atlas/use_cases/{case_id}/nonfunctional_requirements",
                            )
                        )
            for ac in case["acceptance_criteria"]:
                for target in ac["verifies"]:
                    if target not in ids:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-REF",
                                f"acceptance criterion {ac['id']} verifies unknown {target!r}",
                                f"/atlas/use_cases/{case_id}/acceptance_criteria",
                            )
                        )
            for trace in case["traceability"]:
                for target in [trace["source"], *trace["targets"]]:
                    if target not in ids:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-REF",
                                f"trace link {trace['id']} references unknown {target!r}",
                                f"/atlas/use_cases/{case_id}/traceability",
                            )
                        )
            for ref in [*case["assumptions"], *case["sources"], *case["open_issues"]]:
                if ref not in ids:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"use case {case_id} references unknown record {ref!r}",
                            f"/atlas/use_cases/{case_id}",
                        )
                    )

        # shared RNF definitions
        rnf_locations: dict[str, tuple[str, dict]] = {}
        for case in atlas["use_cases"]:
            for rnf in case["nonfunctional_requirements"]:
                rnf_locations[rnf["id"]] = (case["id"], rnf)
        for case in atlas["use_cases"]:
            for rnf in case["nonfunctional_requirements"]:
                target = rnf.get("reference_to")
                if target:
                    if target not in rnf_locations:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-REF",
                                f"non-functional requirement {rnf['id']} references unknown "
                                f"definition {target!r}",
                                f"/atlas/use_cases/{case['id']}/nonfunctional_requirements",
                            )
                        )
                    elif rnf_locations[target][1].get("reference_to"):
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-RNF-CHAIN",
                                f"{rnf['id']} references {target!r}, which is itself only a "
                                "reference; point to the canonical definition",
                                f"/atlas/use_cases/{case['id']}/nonfunctional_requirements",
                            )
                        )
                    elif rnf_locations[target][0] == case["id"]:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-RNF-LOCAL",
                                f"{rnf['id']} references {target!r} in the same use case; "
                                "an entry does not need a local reference",
                                f"/atlas/use_cases/{case['id']}/nonfunctional_requirements",
                            )
                        )

        # boundaries
        rf_owner: dict[str, str] = {}
        for case in atlas["use_cases"]:
            for rf in case["functional_requirements"]:
                rf_owner[rf["id"]] = case["id"]
        for boundary in atlas["boundaries"]:
            for interaction in boundary["interactions"]:
                if interaction["use_case"] not in by_kind["use_case"]:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"interaction {interaction['id']} exposes unknown use case "
                            f"{interaction['use_case']!r}",
                            f"/atlas/boundaries/{boundary['id']}",
                        )
                    )
                for ref in interaction["requirement_refs"]:
                    if ref not in rf_owner:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-REF",
                                f"interaction {interaction['id']} references unknown functional "
                                f"requirement {ref!r}",
                                f"/atlas/boundaries/{boundary['id']}",
                            )
                        )
                    elif rf_owner[ref] != interaction["use_case"]:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-BOUNDARY-RF",
                                f"interaction {interaction['id']} references {ref!r} from "
                                f"{rf_owner[ref]}, not from its use case "
                                f"{interaction['use_case']}",
                                f"/atlas/boundaries/{boundary['id']}",
                            )
                        )
                for ref in interaction["resources"]:
                    if ref not in {r["id"] for r in atlas["resources"]}:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-REF",
                                f"interaction {interaction['id']} references unknown resource "
                                f"{ref!r}",
                                f"/atlas/boundaries/{boundary['id']}",
                            )
                        )
            for ref in [*boundary["assumptions"], *boundary["sources"], *boundary["open_issues"]]:
                if ref not in ids:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"boundary {boundary['id']} references unknown record {ref!r}",
                            f"/atlas/boundaries/{boundary['id']}",
                        )
                    )

        # figure references and graph freshness
        for graph_id, graph in graphs.items():
            for node in graph["nodes"]:
                for ref in node.get("requirement_refs", []):
                    if ref not in rf_owner:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-RF-GRAPH",
                                f"node {node['id']} references unknown functional requirement {ref!r}",
                                f"/atlas/graphs/{graph_id}",
                            )
                        )
            for edge in graph["edges"]:
                for ref in edge.get("requirement_refs", []):
                    if ref not in rf_owner:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-RF-GRAPH",
                                f"edge {edge['id']} references unknown functional requirement {ref!r}",
                                f"/atlas/graphs/{graph_id}",
                            )
                        )
        common_texts = self._common_texts(atlas)
        for resource in atlas["resources"]:
            for relative in [resource["path"], *(v["path"] for v in resource.get("variants", []))]:
                parts = relative.replace("\\", "/").split("/")
                if (
                    not relative
                    or relative.startswith(("/", "\\"))
                    or ".." in parts
                    or any(":" in part for part in parts)
                ):
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-RESOURCE-PATH",
                            f"resource path {relative!r} must be a relative POSIX package path "
                            "without '..' or a drive letter",
                            f"/atlas/resources/{resource['id']}",
                        )
                    )
            for embedded in resource["embedded_text"]:
                value = embedded["text"]
                if value and not any(value in candidate for candidate in common_texts):
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-RESOURCE-TEXT",
                            f"text present in resource {resource['id']} does not also occur "
                            f"in the common textual content: {value!r}",
                            f"/atlas/resources/{resource['id']}/embedded_text",
                        )
                    )
            graph_id = resource.get("derived_from_graph")
            if graph_id:
                if graph_id not in graphs:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"resource {resource['id']} derives from unknown graph {graph_id!r}",
                            f"/atlas/resources/{resource['id']}",
                        )
                    )
                else:
                    expected = graph_fingerprint(graphs[graph_id])
                    revision = (resource.get("drawing_source") or {}).get("revision")
                    if revision != expected:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-FIGURE-STALE",
                                f"resource {resource['id']} records drawing revision "
                                f"{revision!r}, but graph {graph_id} now has fingerprint "
                                f"{expected}. Regenerate the figure and update the revision.",
                                f"/atlas/resources/{resource['id']}/drawing_source",
                            )
                        )
            for variant in resource.get("variants", []):
                if variant["derived_from"] != resource["path"]:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-VARIANT",
                            f"variant {variant['path']} does not identify {resource['path']} "
                            "as its source",
                            f"/atlas/resources/{resource['id']}/variants",
                        )
                    )

        # generic record references
        for record_key in ("assumptions", "decisions", "open_issues"):
            for record in atlas[record_key]:
                refs = record.get("affected") or record.get("refs") or []
                for ref in refs:
                    if ref not in ids:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-REF",
                                f"{record_key} record {record['id']} references unknown {ref!r}",
                                f"/atlas/{record_key}/{record['id']}",
                            )
                        )
        for case in atlas["use_cases"]:
            for ref in case["sources"]:
                if ref not in {s["id"] for s in atlas["sources"]}:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"use case {case['id']} references unknown source {ref!r}",
                            f"/atlas/use_cases/{case['id']}",
                        )
                    )
        for entity in atlas["entities"]:
            for ref in [*entity["assumptions"], *entity["open_issues"]]:
                if ref not in ids:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-REF",
                            f"entity {entity['id']} references unknown record {ref!r}",
                            f"/atlas/entities/{entity['id']}",
                        )
                    )
        return diagnostics

    def _common_texts(self, value: Any) -> list[str]:
        texts: list[str] = []

        def walk(node: Any) -> None:
            if isinstance(node, dict):
                for key, item in node.items():
                    if key in {"extensions", "meta", "data", "embedded_text"}:
                        continue
                    if key == "text" and isinstance(item, str):
                        texts.append(item)
                    else:
                        walk(item)
            elif isinstance(node, list):
                for item in node:
                    walk(item)

        walk(value)
        return texts

    def _collect_ids(
        self, value: Any, path: str, ids: dict[str, str], diagnostics: list[Diagnostic]
    ) -> None:
        if isinstance(value, dict):
            for key, item in value.items():
                if key in {"extensions", "meta", "data", "owner", "call"}:
                    continue
                if key == "id" and isinstance(item, str):
                    if item in ids:
                        diagnostics.append(
                            Diagnostic(
                                "ATL-E-DUPLICATE-ID",
                                f"id {item!r} is already used at {ids[item]}",
                                path,
                            )
                        )
                    else:
                        ids[item] = path
                self._collect_ids(item, f"{path}.{key}", ids, diagnostics)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                self._collect_ids(item, f"{path}[{index}]", ids, diagnostics)

    def _graph_owner_error(
        self, atlas: dict, graph_id: str, kind: str, owner_id: str
    ) -> Diagnostic | None:
        graph = next((g for g in atlas["graphs"] if g["id"] == graph_id), None)
        if graph is None:
            return Diagnostic(
                "ATL-E-REF",
                f"{kind} {owner_id} references unknown graph {graph_id!r}",
                f"/atlas/{kind}s/{owner_id}",
            )
        if graph["owner"]["kind"] != kind or graph["owner"]["id"] != owner_id:
            return Diagnostic(
                "ATL-E-GRAPH-OWNER",
                f"graph {graph_id} is not owned by {kind} {owner_id}",
                f"/atlas/graphs/{graph_id}",
            )
        return None

    def _check_graph_owner(
        self,
        atlas: dict,
        by_kind: dict[str, dict[str, Any]],
        graph: dict,
        diagnostics: list[Diagnostic],
    ) -> None:
        owner = graph["owner"]
        exists = False
        if owner["kind"] == "document":
            exists = owner["id"] == atlas["document_id"]
        elif owner["kind"] == "validation":
            exists = any(
                v["id"] == owner["id"] and v["flow"] == graph["id"]
                for entity in atlas["entities"]
                for v in entity["validations"]
            )
            if not exists and any(
                v["id"] == owner["id"] for entity in atlas["entities"] for v in entity["validations"]
            ):
                diagnostics.append(
                    Diagnostic(
                        "ATL-E-GRAPH-OWNER",
                        f"validation {owner['id']} does not nominate graph {graph['id']} as its flow",
                        f"/atlas/graphs/{graph['id']}",
                    )
                )
        elif owner["kind"] == "use_case":
            exists = owner["id"] in by_kind["use_case"]
            if exists:
                case = by_kind["use_case"][owner["id"]]
                if graph["id"] not in {case["flows"]["main"], *case["flows"]["subflows"]}:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-GRAPH-OWNER",
                            f"graph {graph['id']} is not listed in the flows of {owner['id']}",
                            f"/atlas/graphs/{graph['id']}",
                        )
                    )
        elif owner["kind"] == "entity":
            exists = owner["id"] in by_kind["entity"]
        if not exists:
            diagnostics.append(
                Diagnostic(
                    "ATL-E-GRAPH-OWNER",
                    f"graph {graph['id']} has an unknown owner {owner['kind']} {owner['id']!r}",
                    f"/atlas/graphs/{graph['id']}",
                )
            )

    def _expect_owner(
        self,
        graph: dict,
        kind: str,
        owner_id: str,
        diagnostics: list[Diagnostic],
        case_id: str,
    ) -> None:
        if graph["owner"]["kind"] != kind or graph["owner"]["id"] != owner_id:
            diagnostics.append(
                Diagnostic(
                    "ATL-E-GRAPH-OWNER",
                    f"use case {case_id} uses graph {graph['id']} owned by "
                    f"{graph['owner']['kind']} {graph['owner']['id']}",
                    f"/atlas/use_cases/{case_id}/flows",
                )
            )

    def _call_target_exists(
        self,
        atlas: dict,
        by_kind: dict[str, dict[str, Any]],
        call: dict,
        expected: str,
    ) -> bool:
        if expected == "validation":
            return any(
                v["id"] == call["id"] for e in atlas["entities"] for v in e["validations"]
            )
        if expected == "operation":
            return any(
                op["id"] == call["id"] for t in atlas["tools"] for op in t["operations"]
            )
        return call["id"] in by_kind.get(expected, {})

    def _applies_to_exists(
        self,
        atlas: dict,
        case: dict,
        rf: dict,
        target: str,
        by_kind: dict[str, dict[str, Any]],
    ) -> bool:
        if target == case["id"]:
            return True
        if target in {op["id"] for t in atlas["tools"] for op in t["operations"]}:
            return True
        return any(
            interaction["id"] == target
            for boundary in atlas["boundaries"]
            for interaction in boundary["interactions"]
        )

    # -- resources ------------------------------------------------------
    def _resource_errors(self, document: dict, resource_root: Path) -> list[Diagnostic]:
        diagnostics: list[Diagnostic] = []
        root = resource_root.resolve()
        for resource in document["atlas"]["resources"]:
            entries = [(resource["path"], resource["sha256"], resource["size"], "original")]
            entries.extend(
                (variant["path"], variant["sha256"], variant["size"], "variant")
                for variant in resource.get("variants", [])
            )
            for relative, digest, size, role in entries:
                path = (root / relative).resolve()
                if not _is_relative_to(path, root):
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-RESOURCE-PATH",
                            f"{role} {relative!r} escapes the resource root",
                            f"/atlas/resources/{resource['id']}",
                        )
                    )
                    continue
                if not path.is_file():
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-RESOURCE-MISSING",
                            f"{role} file {relative!r} is missing under {root}",
                            f"/atlas/resources/{resource['id']}",
                        )
                    )
                    continue
                if path.stat().st_size != size:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-RESOURCE-SIZE",
                            f"{role} file {relative!r} has size {path.stat().st_size}, "
                            f"but the catalog declares {size}",
                            f"/atlas/resources/{resource['id']}",
                        )
                    )
                actual = sha256_file(path)
                if actual != digest:
                    diagnostics.append(
                        Diagnostic(
                            "ATL-E-RESOURCE-HASH",
                            f"{role} file {relative!r} has sha256 {actual}, "
                            f"but the catalog declares {digest}",
                            f"/atlas/resources/{resource['id']}",
                        )
                    )
        return diagnostics


def graph_fingerprint(graph: dict) -> str:
    canonical = json.dumps(
        graph,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return sha256_text(canonical)


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def validate_document(
    document: dict,
    *,
    resource_root: Path | None = None,
    check_resources: bool = True,
) -> None:
    Validator().validate(document, resource_root=resource_root, check_resources=check_resources)
