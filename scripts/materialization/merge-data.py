"""
Merge MCP server, tool, and parameter CSV files.

Input:
    servers.csv
    tools.csv
    parameters.csv

Output:
    merged-final.csv
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

OUTPUT_CSV = SCRIPT_DIR / "data/server-tools-merged.csv"

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

# ------------------------------------------------------------
# Sort nicely
# ------------------------------------------------------------

sort_columns = [
    "server_name",
    "tool_name",
    "parameter_name",
]

merged = merged.sort_values(sort_columns)

# ------------------------------------------------------------
# Save
# ------------------------------------------------------------

merged.to_csv(OUTPUT_CSV, index=False)

print(f"\nDone!")
print(f"Rows written: {len(merged):,}")
print(f"Output: {Path(OUTPUT_CSV).resolve()}")