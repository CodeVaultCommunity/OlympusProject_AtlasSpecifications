"""Deterministic, page-bounded TikZ views of structured Atlas graphs.

Only the graph is authoritative. This rendering uses short edge keys and a
complete legend so long identifiers never collide with nodes or other edges.
"""

from __future__ import annotations

from collections import deque
import textwrap
import re


def _escape_tikz(value: str) -> str:
    mapping = {
        "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}",
        "%": r"\%", "#": r"\#", "&": r"\&", "_": r"\_",
        "$": r"\$", "^": r"\textasciicircum{}", "~": r"\textasciitilde{}",
    }
    return "".join(mapping.get(char, char) for char in value).replace("\r\n", " ").replace("\n", " ").replace("\r", " ")


def _label(text: dict | None, width: int = 18) -> tuple[str, int]:
    value = (text or {}).get("text", "")
    # Break stable IDs at their delimiters rather than letting an unbroken
    # uppercase token overflow the fixed-width box. This is presentation only.
    spaced = re.sub(r"(?<=[_-])(?=\w)", " ", value)
    wrapped = textwrap.wrap(spaced, width=width, break_long_words=True,
                            break_on_hyphens=True) or [""]
    wrapped = [line.replace("_ ", "_").replace("- ", "-") for line in wrapped]
    return r"\\".join(_escape_tikz(line) for line in wrapped), len(wrapped)


def _depths(graph: dict) -> dict[str, int]:
    """Longest-path ranks for DAGs; deterministic placement for cyclic residue."""
    node_ids = [node["id"] for node in graph["nodes"]]
    incoming = {node_id: 0 for node_id in node_ids}
    outgoing = {node_id: [] for node_id in node_ids}
    for edge in graph["edges"]:
        if edge["from"] in outgoing and edge["to"] in incoming:
            outgoing[edge["from"]].append(edge["to"])
            incoming[edge["to"]] += 1
    queue = deque(node_id for node_id in node_ids if incoming[node_id] == 0)
    depth = {node_id: 0 for node_id in queue}
    while queue:
        current = queue.popleft()
        for target in outgoing[current]:
            depth[target] = max(depth.get(target, 0), depth[current] + 1)
            incoming[target] -= 1
            if incoming[target] == 0:
                queue.append(target)
    # A cycle is meaningful content, not an invitation to an infinite layout loop.
    next_depth = max(depth.values(), default=-1) + 1
    for node_id in node_ids:
        if incoming[node_id] > 0:
            depth[node_id] = next_depth
            next_depth += 1
    return depth


def render_tikz_legacy(graph: dict) -> str:
    nodes = graph["nodes"]
    depths = _depths(graph)
    rows: dict[int, list[dict]] = {}
    labels: dict[str, str] = {}
    heights: dict[int, float] = {}
    for node in nodes:
        rank = depths[node["id"]]
        rows.setdefault(rank, []).append(node)
        label_width = 16 if node["type"] == "decision" else (
            14 if node["type"] in {"start", "end", "result", "refusal", "failure"} else 18
        )
        label, count = _label(node.get("label"), label_width)
        labels[node["id"]] = label
        height = max(1.0, count * 0.38 + 0.35)
        if node["type"] == "decision":
            height *= 1.7
        heights[rank] = max(heights.get(rank, 0), height)
    positions: dict[str, tuple[float, float]] = {}
    y = 0.0
    previous = None
    for rank in sorted(rows):
        if previous is not None:
            y -= heights[previous] / 2 + heights[rank] / 2 + 0.85
        for column, node in enumerate(rows[rank]):
            positions[node["id"]] = ((column - (len(rows[rank]) - 1) / 2) * 4.4, y)
        previous = rank
    index = {node["id"]: i for i, node in enumerate(nodes)}
    half_width = max((abs(x) for x, _ in positions.values()), default=0) + 2.0
    detours = [edge for edge in graph["edges"]
               if edge["from"] in depths and edge["to"] in depths
               and depths[edge["to"]] != depths[edge["from"]] + 1]
    width = half_width * 2 + (0.7 + len(detours) * 0.25 if detours else 0)
    height = abs(y) + max(heights.values(), default=1)
    graph_budget = min(16.0, max(8.0, 20.0 - 0.40 * len(graph["edges"])))
    scale = min(1.0, 15.4 / max(width, 1), graph_budget / max(height, 1))
    lines = [
        r"\clearpage",
        r"\noindent{\large\bfseries " + _escape_tikz(graph["title"]["text"]) + "}\\par",
        r"\noindent{\small " + _escape_tikz(graph["id"]) + "}\\par",
        r"\begin{center}",
        f"\\scalebox{{{scale:.4f}}}{{%",
        r"\begin{tikzpicture}[",
        r"  >=Stealth, line width=0.65pt, draw=black!65,",
        r"  box/.style={draw, rounded corners=3pt, fill=blue!4, align=center, text width=3.5cm, minimum height=1.0cm, inner sep=5pt, font=\small},",
        r"  decision/.style={draw, diamond, aspect=1.7, fill=orange!8, align=center, text width=2.5cm, inner sep=3pt, font=\small},",
        r"  terminal/.style={draw, rounded corners=9pt, fill=blue!8, align=center, text width=3.5cm, minimum height=1.0cm, inner sep=5pt, font=\small\bfseries},",
        r"  state/.style={draw, ellipse, fill=blue!4, align=center, text width=3.3cm, inner sep=5pt, font=\small},",
        r"  note/.style={draw, dashed, fill=black!3, align=center, text width=3.5cm, inner sep=5pt, font=\small\itshape},",
        r"  edgekey/.style={fill=white, inner sep=1.5pt, font=\scriptsize\bfseries}",
        "]",
    ]
    for node in nodes:
        style = {
            "decision": "decision", "start": "terminal", "end": "terminal",
            "result": "terminal", "refusal": "terminal", "failure": "terminal",
            "state": "state", "note": "note",
        }.get(node["type"], "box")
        x, y = positions[node["id"]]
        lines.append(f"\\node[{style}] (n{index[node['id']]}) at ({x:.2f},{y:.2f}) {{{labels[node['id']]}}};")
    detour_index = 0
    for edge_number, edge in enumerate(graph["edges"], 1):
        if edge["from"] not in index or edge["to"] not in index:
            continue
        source, target = f"n{index[edge['from']]}", f"n{index[edge['to']]}"
        key = f"E{edge_number}"
        if depths[edge["to"]] == depths[edge["from"]] + 1:
            lines.append(f"\\draw[->] ({source}.south) -- node[edgekey,pos=0.65]{{{key}}} ({target}.north);")
        else:
            lane = half_width + 0.45 + detour_index * 0.25
            detour_index += 1
            sx, sy = positions[edge["from"]]
            tx, ty = positions[edge["to"]]
            if edge["from"] == edge["to"]:
                lines.append(f"\\draw[->] ({source}.east) to[out=0,in=90,looseness=5] node[edgekey]{{{key}}} ({target}.north);")
            else:
                exit_y = sy - heights[depths[edge["from"]]] / 2 - 0.28
                entry_y = ty + heights[depths[edge["to"]]] / 2 + 0.28
                key_position = detour_index / (len(detours) + 1)
                lines.append(
                    f"\\draw[->] ({source}.south) -- ({sx:.2f},{exit_y:.2f}) "
                    f"-- ({lane:.2f},{exit_y:.2f}) "
                    f"-- node[edgekey,pos={key_position:.3f}]{{{key}}} ({lane:.2f},{entry_y:.2f}) "
                    f"-- ({tx:.2f},{entry_y:.2f}) -- ({target}.north);"
                )
    lines.extend([r"\end{tikzpicture}%", "}", r"\end{center}", r"\noindent\textbf{Edge key}\par", r"\begingroup\small\raggedright\setlength{\parskip}{1pt}"])
    for edge_number, edge in enumerate(graph["edges"], 1):
        label = (edge.get("label") or {}).get("text", "")
        # Preserve label/condition in the complete structured listing above; the
        # diagram legend disambiguates every edge using its exact stable ID.
        detail = _escape_tikz(edge["id"])
        if label:
            detail += " --- " + _escape_tikz(label)
        lines.append(f"\\noindent\\textbf{{E{edge_number}}} {detail}\\par")
    lines.extend([r"\endgroup", r"\clearpage"])
    return "\n".join(lines)


# The legacy renderer above is frozen for exact validation of existing Stable files.
def render_tikz(graph: dict) -> str:
    nodes = graph["nodes"]
    depths = _depths(graph)
    rows: dict[int, list[dict]] = {}
    labels: dict[str, str] = {}
    heights: dict[int, float] = {}
    for node in nodes:
        rank = depths[node["id"]]
        rows.setdefault(rank, []).append(node)
        label_width = 16 if node["type"] == "decision" else (
            14 if node["type"] in {"start", "end", "result", "refusal", "failure"} else 18
        )
        label, count = _label(node.get("label"), label_width)
        labels[node["id"]] = label
        height = max(1.0, count * 0.38 + 0.35)
        if node["type"] == "decision":
            height *= 1.7
        heights[rank] = max(heights.get(rank, 0), height)
    positions: dict[str, tuple[float, float]] = {}
    y = 0.0
    previous = None
    for rank in sorted(rows):
        if previous is not None:
            y -= heights[previous] / 2 + heights[rank] / 2 + 0.45
        for column, node in enumerate(rows[rank]):
            positions[node["id"]] = ((column - (len(rows[rank]) - 1) / 2) * 3.3, y)
        previous = rank
    index = {node["id"]: i for i, node in enumerate(nodes)}
    half_width = max((abs(x) for x, _ in positions.values()), default=0) + 2.0
    detours = [edge for edge in graph["edges"]
               if edge["from"] in depths and edge["to"] in depths
               and depths[edge["to"]] != depths[edge["from"]] + 1]
    width = half_width * 2 + (0.7 + len(detours) * 0.25 if detours else 0)
    height = abs(y) + max(heights.values(), default=1)
    graph_budget = 22.0
    scale = min(1.0, 15.4 / max(width, 1), graph_budget / max(height, 1))
    legend_lines = sum(max(1, (len(edge["id"]) + len((edge.get("label") or {}).get("text", "")) + 79) // 80) for edge in graph["edges"])
    # Keep short legends with their diagrams; larger legends remain breakable.
    reserved_extra = 1.5
    if legend_lines <= 8:
        reserved_extra += (legend_lines + 2) * 0.45
    lines = [
        r"\sbox{\AtlasGraphBox}{%",
        f"\\scalebox{{{scale:.4f}}}{{%",
        r"\begin{tikzpicture}[",
        r"  >=Stealth, line width=0.65pt, draw=black!65,",
        r"  box/.style={draw, rounded corners=3pt, fill=blue!4, align=center, text width=2.6cm, minimum height=1.0cm, inner sep=5pt, font=\fontsize{9.5}{11}\selectfont},",
        r"  decision/.style={draw, diamond, aspect=1.7, fill=orange!8, align=center, text width=2.0cm, inner sep=3pt, font=\fontsize{9.5}{11}\selectfont},",
        r"  terminal/.style={draw, rounded corners=9pt, fill=blue!8, align=center, text width=2.8cm, minimum height=1.0cm, inner sep=5pt, font=\fontsize{9.5}{11}\selectfont\bfseries},",
        r"  state/.style={draw, ellipse, fill=blue!4, align=center, text width=2.6cm, inner sep=5pt, font=\fontsize{9.5}{11}\selectfont},",
        r"  note/.style={draw, dashed, fill=black!3, align=center, text width=2.6cm, inner sep=5pt, font=\fontsize{9.5}{11}\selectfont\itshape},",
        r"  edgekey/.style={fill=white, inner sep=1.5pt, font=\fontsize{8.5}{10}\selectfont\bfseries}",
        "]",
    ]
    for node in nodes:
        style = {
            "decision": "decision", "start": "terminal", "end": "terminal",
            "result": "terminal", "refusal": "terminal", "failure": "terminal",
            "state": "state", "note": "note",
        }.get(node["type"], "box")
        x, y = positions[node["id"]]
        lines.append(f"\\node[{style}] (n{index[node['id']]}) at ({x:.2f},{y:.2f}) {{{labels[node['id']]}}};")
    detour_index = 0
    for edge_number, edge in enumerate(graph["edges"], 1):
        if edge["from"] not in index or edge["to"] not in index:
            continue
        source, target = f"n{index[edge['from']]}", f"n{index[edge['to']]}"
        key = f"E{edge_number}"
        if depths[edge["to"]] == depths[edge["from"]] + 1:
            lines.append(f"\\draw[->] ({source}.south) -- node[edgekey,pos=0.65]{{{key}}} ({target}.north);")
        else:
            lane = half_width + 0.45 + detour_index * 0.25
            detour_index += 1
            sx, sy = positions[edge["from"]]
            tx, ty = positions[edge["to"]]
            if edge["from"] == edge["to"]:
                lines.append(f"\\draw[->] ({source}.east) to[out=0,in=90,looseness=5] node[edgekey]{{{key}}} ({target}.north);")
            else:
                exit_y = sy - heights[depths[edge["from"]]] / 2 - 0.28
                entry_y = ty + heights[depths[edge["to"]]] / 2 + 0.28
                key_position = detour_index / (len(detours) + 1)
                lines.append(
                    f"\\draw[->] ({source}.south) -- ({sx:.2f},{exit_y:.2f}) "
                    f"-- ({lane:.2f},{exit_y:.2f}) "
                    f"-- node[edgekey,pos={key_position:.3f}]{{{key}}} ({lane:.2f},{entry_y:.2f}) "
                    f"-- ({tx:.2f},{entry_y:.2f}) -- ({target}.north);"
                )
    lines.extend([r"\end{tikzpicture}%", "}}",
                  # Measure the actual drawing; the layout estimate is only
                  # for scaling very large graphs, never for reserving pages.
                  r"\Needspace{\dimexpr\ht\AtlasGraphBox+\dp\AtlasGraphBox+" + f"{reserved_extra:.2f}cm" + r"\relax}",
                  "\\hypertarget{figure-" + graph["id"] + "}{}",
                  r"\noindent{\large\bfseries " + _escape_tikz(graph["title"]["text"]) + "}\\par",
                  r"\noindent{\small " + _escape_tikz(graph["id"]) + "}\\par",
                  r"\begin{center}\usebox{\AtlasGraphBox}\end{center}",
                  r"\begingroup\small\setlength{\LTleft}{0pt}\setlength{\LTright}{0pt}",
                  r"\begin{longtable}{@{}p{.07\linewidth}p{.90\linewidth}@{}}",
                  r"\textbf{Key} & \textbf{Edge identity and label}\\\midrule\endhead"])
    for edge_number, edge in enumerate(graph["edges"], 1):
        label = (edge.get("label") or {}).get("text", "")
        detail = _escape_tikz(edge["id"]).replace("-", r"-\allowbreak{}")
        if label:
            detail += " --- " + _escape_tikz(label)
        lines.append(f"\\textbf{{E{edge_number}}} & {detail}" + r"\\")
    lines.extend([r"\end{longtable}\endgroup"])
    return "\n".join(lines)
