"""Export BFCL function declarations to source-matched CSVs for graph import.

Each occurrence links to a definition. Identical declarations share a
SHA-256 definition_id across files. The parameters_json column preserves
the structure of the input schema.
"""

import csv
import hashlib
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
OUTPUT_DIR = DATA_DIR / "function_extraction"
COLUMNS = (
    "definition_id",
    "source_file",
    "name",
    "description",
    "parameters_json",
    "server_name",
    "tool_name",
)


def read_records(path: Path) -> list[dict]:
    """Read records from a JSON document or JSON Lines file.

    Args:
        path: Path to the dataset file.

    Returns:
        Records in source order.

    Raises:
        ValueError: A line contains invalid JSON.
    """
    content = path.read_text(encoding="utf-8")
    try:
        document = json.loads(content)
    except json.JSONDecodeError:
        records = []
        for number, line in enumerate(content.splitlines(), start=1):
            if line.strip():
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError as error:
                    raise ValueError(f"{path}:{number}: {error}") from error
        return records
    return document if isinstance(document, list) else [document]


def encode_json(value: object) -> str:
    """Serialize a value for a stable definition hash or CSV field.

    Args:
        value: JSON-compatible value to encode.

    Returns:
        Compact JSON with sorted object keys.
    """
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )


# Column names and relationship tables follow the Tool Coupler CSV mapping:
# https://github.com/kastle-lab/tool-coupler-ontology/tree/main/scripts/data
TOOL_KEY = ("server_name", "tool_name", "definition_id")
PARAMETER_COLUMNS = ("parameter_name", "schema_type")
PARAMETER_KEY = TOOL_KEY + PARAMETER_COLUMNS
PARAMETER_FIELDS = ("datatype", "parameter_description", "is_required")
ELEMENT_FIELDS = (
    "element_name",
    "element_path",
    "datatype",
    "element_description",
)
HIERARCHY_FIELDS = (
    "parent_element_name",
    "parent_element_path",
    "child_element_name",
    "element_path",
    "datatype",
    "element_element_description",
)


def datatype(schema: dict) -> str:
    """Map a BFCL schema type to its CSV datatype label.

    Args:
        schema: Schema declaring the source type.

    Returns:
        The normalized label, preserving Float and Double when declared,
        or an empty string for a missing type.
    """
    original = schema.get("type", "")
    aliases = {
        "dict": "Object",
        "hashmap": "Object",
        "long": "Integer",
        "arraylist": "Array",
        "tuple": "Array",
        "char": "String",
    }
    return aliases.get(original.lower(), original.capitalize())


def named_children(schema: dict):
    """Find named properties of an object or its array items.

    Args:
        schema: Schema to inspect for properties and item schemas.

    Yields:
        Pairs of property names and their schemas.
    """
    yield from schema.get("properties", {}).items()
    if isinstance(schema.get("items"), dict):
        yield from named_children(schema["items"])


def add_elements(tables, key, schema, parent_name, parent_path, *, root=False):
    """Append relationship rows for nested parameter elements.

    Args:
        tables: CSV row lists to update, keyed by table name.
        key: Server, tool name, definition ID, parameter, and schema direction.
        schema: Schema whose named children should be exported.
        parent_name: Name of the containing parameter or element.
        parent_path: Dotted path of the containing parameter or element.
        root: Whether the parent is the top-level parameter.
    """
    for name, child in named_children(schema):
        path = f"{parent_path}.{name}"
        details = (datatype(child), child.get("description", ""))
        if root:
            row = key + (name, path) + details
            tables["parameters-to-elements"].append(row)
            tables[f"parameters-to-elements-{key[-1].lower()}"].append(row)
        else:
            row = key + (parent_name, parent_path, name, path) + details
            tables["elements-hierarchy"].append(row)
            if key[-1] == "Input":
                tables["elements-hierarchy-input"].append(row)
        add_elements(tables, key, child, name, path)


def add_definition(tables, tool_key, function):
    """Append the tool, parameter, and element rows for one declaration.

    Args:
        tables: CSV row lists to update, keyed by table name.
        tool_key: Server name, tool name, and definition ID.
        function: Source declaration with input and optional output schemas.
    """
    description = function["description"]
    tables["servers"].append(tool_key)
    tables["tools"].append(tool_key + (description,))
    for field, direction in (("parameters", "Input"), ("response", "Output")):
        schema = function.get(field, {})
        for name, parameter in schema.get("properties", {}).items():
            key = tool_key + (name, direction)
            required = (
                "Required"
                if name in schema.get("required", [])
                else "Optional"
            )
            details = (
                datatype(parameter),
                parameter.get("description", ""),
                required,
            )
            tables["parameters"].append(key + details)
            tables[f"server-tools-{direction.lower()}"].append(
                tool_key + (description, name, direction) + details
            )
            add_elements(tables, key, parameter, name, name, root=True)


def write_table(path: Path, header: tuple, rows: list) -> None:
    """Write a CSV table, creating parent directories as needed.

    Args:
        path: Destination CSV path.
        header: Column names in output order.
        rows: Data rows in the same column order.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(header)
        writer.writerows(rows)


def extract_source(path: Path) -> int:
    """Write occurrence and relationship tables for one source file.

    Args:
        path: Dataset file beneath DATA_DIR.

    Returns:
        Number of declaration occurrences, including duplicates.
    """
    source = path.relative_to(DATA_DIR)
    # Use the dataset path as the collection identifier.
    collection = source.with_suffix("").as_posix()
    headers = {
        "servers": TOOL_KEY,
        "tools": TOOL_KEY + ("tool_description",),
        "parameters": PARAMETER_KEY + PARAMETER_FIELDS,
        "elements-hierarchy": PARAMETER_KEY + HIERARCHY_FIELDS,
        "elements-hierarchy-input": PARAMETER_KEY + HIERARCHY_FIELDS,
        "parameters-to-elements": PARAMETER_KEY + ELEMENT_FIELDS,
    }
    for direction in ("input", "output"):
        headers[f"parameters-to-elements-{direction}"] = (
            PARAMETER_KEY + ELEMENT_FIELDS
        )
        headers[f"server-tools-{direction}"] = (
            TOOL_KEY
            + ("tool_description",)
            + PARAMETER_COLUMNS
            + PARAMETER_FIELDS
        )
    tables = {name: [] for name in headers}
    rows = []
    seen = set()
    for record in read_records(path):
        declarations = record.get("function", [])
        if "name" in record and "parameters" in record:
            declarations = [record]
        for function in declarations:
            digest = hashlib.sha256(
                encode_json(function).encode("utf-8")
            ).hexdigest()
            definition_id = f"sha256:{digest}"
            tool_name = f"{collection}_{function['name']}"
            tool_key = (collection, tool_name, definition_id)
            if digest not in seen:
                add_definition(tables, tool_key, function)
                seen.add(digest)
            rows.append(
                (
                    definition_id,
                    source.as_posix(),
                    function["name"],
                    function["description"],
                    encode_json(function["parameters"]),
                    collection,
                    tool_name,
                )
            )

    if rows:
        destination = OUTPUT_DIR / source.with_suffix(".csv")
        write_table(destination, COLUMNS, rows)
        for table, header in headers.items():
            write_table(
                destination.with_suffix("") / f"{table}.csv",
                header,
                tables[table],
            )
    return len(rows)


def main() -> None:
    """Export declarations from all dataset files and print the totals."""
    counts = [
        extract_source(path) for path in sorted(DATA_DIR.rglob("*.json"))
    ]
    file_count = sum(bool(count) for count in counts)
    print(f"Exported {sum(counts)} declarations from {file_count} files.")


if __name__ == "__main__":
    main()
