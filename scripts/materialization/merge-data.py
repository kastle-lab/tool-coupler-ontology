"""
Merge MCP server, tool, and parameter CSV files, then split by schema type.

Input:
    servers.csv
    tools.csv
    parameters.csv

Output:
    server-tools-input.csv    (Input-only parameters)
    server-tools-output.csv   (Output-only parameters)
    server-tools-inout.csv    (parameters that are BOTH input and output)
"""

from pathlib import Path
import pandas as pd

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

# Directory where this Python script is located
SCRIPT_DIR = Path(__file__).resolve().parent.parent

# Updated paths matching the new decoupled files
SERVER_CSV = SCRIPT_DIR / "data/servers.csv"
TOOLS_CSV = SCRIPT_DIR / "data/tools.csv"
PARAMETERS_CSV = SCRIPT_DIR / "data/parameters.csv"

INPUT_CSV = SCRIPT_DIR / "data/server-tools-input.csv"
OUTPUT_CSV = SCRIPT_DIR / "data/server-tools-output.csv"
INOUT_CSV = SCRIPT_DIR / "data/server-tools-inout.csv"

print(f"Script directory: {SCRIPT_DIR}")

# ------------------------------------------------------------
# Read CSVs
# ------------------------------------------------------------

print("Loading CSV files...")

servers = pd.read_csv(SERVER_CSV)
tools = pd.read_csv(TOOLS_CSV)
params = pd.read_csv(PARAMETERS_CSV)

# Remove accidental whitespace from column names
servers.columns = servers.columns.str.strip()
tools.columns = tools.columns.str.strip()
params.columns = params.columns.str.strip()


# ------------------------------------------------------------
# Clean values
# ------------------------------------------------------------

for df in (servers, tools, params):
    df["tool_name"] = df["tool_name"].astype(str).str.strip()
    df["server_name"] = df["server_name"].astype(str).str.strip()


# ------------------------------------------------------------
# Check for missing tools
# ------------------------------------------------------------

server_tools = set(servers["tool_name"])
parameter_tools = set(params["tool_name"])
missing_parameters = sorted(server_tools - parameter_tools)

if missing_parameters:
    print("\nWARNING: These tools have no parameters:")
    for tool in missing_parameters:
        print(f"   {tool}")


# ------------------------------------------------------------
# Merge
# ------------------------------------------------------------

print("\nMerging server + tools...")

# Merge on both server_name and tool_name to prevent duplicate columns
merged = servers.merge(
    tools,
    on=["server_name", "tool_name"],
    how="left",
    validate="many_to_one",
)

print("Adding parameters...")

# Merge on both server_name and tool_name
merged = merged.merge(
    params,
    on=["server_name", "tool_name"],
    how="left",
    validate="one_to_many",
)

# Fill NaNs so string comparisons below behave predictably
merged = merged.fillna("")

# Normalize schema_type so "input" / " Input " etc. all match
merged["schema_type"] = merged["schema_type"].astype(str).str.strip().str.title()

# ------------------------------------------------------------
# Split by schema type (Input / Output / InOut)
# ------------------------------------------------------------

print("\nSplitting by schema type...")

KEY_COLS = ["server_name", "tool_name", "parameter_name"]

# Drop "unrelated" rows: tools that matched no parameters (empty parameter_name)
has_param = merged["parameter_name"] != ""
param_rows = merged[has_param].copy()

# A parameter is "InOut" if the same (server, tool, parameter) appears
# with BOTH an Input row and an Output row
schema_sets = param_rows.groupby(KEY_COLS)["schema_type"].agg(set)
inout_keys = set(schema_sets[schema_sets >= {"Input", "Output"}].index)

keys = pd.MultiIndex.from_frame(param_rows[KEY_COLS])
# InOut is either (a) the same key appearing as both an Input row and an
# Output row, or (b) a single row pre-consolidated as "Input/Output"
is_inout = keys.isin(inout_keys) | (param_rows["schema_type"] == "Input/Output")

inout_df = param_rows[is_inout]
input_df = param_rows[~is_inout & (param_rows["schema_type"] == "Input")]
output_df = param_rows[~is_inout & (param_rows["schema_type"] == "Output")]

# ------------------------------------------------------------
# Compress: set schema_type to each file's label and de-duplicate
# ------------------------------------------------------------

sort_columns = ["server_name", "tool_name", "parameter_name"]

def finalize(df: pd.DataFrame, schema_label: str) -> pd.DataFrame:
    """Set schema_type to this file's label, drop duplicate rows, sort."""
    df = df.copy()
    df["schema_type"] = schema_label
    return df.drop_duplicates().sort_values(sort_columns)

input_df = finalize(input_df, "Input")
output_df = finalize(output_df, "Output")
# InOut parameters exist as two rows (one Input, one Output); once
# schema_type is overwritten with "InOut" they collapse into a single
# row via drop_duplicates
inout_df = finalize(inout_df, "InOut")

# ------------------------------------------------------------
# Save
# ------------------------------------------------------------

input_df.to_csv(INPUT_CSV, index=False)
output_df.to_csv(OUTPUT_CSV, index=False)
inout_df.to_csv(INOUT_CSV, index=False)

print(f"\nDone!")
print(f"Input-only rows:  {len(input_df):,}  -> {Path(INPUT_CSV).resolve()}")
print(f"Output-only rows: {len(output_df):,}  -> {Path(OUTPUT_CSV).resolve()}")
print(f"InOut rows:       {len(inout_df):,}  -> {Path(INOUT_CSV).resolve()}")
