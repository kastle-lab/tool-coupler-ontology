"""
Split element CSV files by schema type (Input / Output / InOut).

For each input file, produces three CSVs:
    <name>-input.csv    (Input-only rows)
    <name>-output.csv   (Output-only rows)
    <name>-inout.csv    (rows whose identity appears as BOTH Input and Output)

InOut detection is based on each file's identity columns (KEY_COLS below):
if the same element appears with both an Input row and an Output row,
it is classified as InOut and removed from the other two files.

The schema_type column is kept in every output file, set to that file's
type (Input / Output / InOut). Duplicate / empty rows are removed.
"""

from pathlib import Path
import pandas as pd

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

# Directory where this Python script is located
SCRIPT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = SCRIPT_DIR / "data"

# Each entry: input file -> the columns that identify a unique element
# (used to detect InOut: same identity appearing as both Input and Output)
FILES = {
    DATA_DIR / "elements-hierarchy.csv": [
        "server_name",
        "tool_name",
        "parameter_name",
        "element_path",
    ],
    DATA_DIR / "parameters-to-elements.csv": [
        "server_name",
        "tool_name",
        "parameter_name",
        "element_name",
    ],
}

print(f"Script directory: {SCRIPT_DIR}")

# ------------------------------------------------------------
# Split logic
# ------------------------------------------------------------

def split_by_schema_type(csv_path: Path, key_cols: list[str]) -> None:
    print(f"\nProcessing {csv_path.name}...")

    df = pd.read_csv(csv_path)

    # Remove accidental whitespace from column names and key values
    df.columns = df.columns.str.strip()
    for col in key_cols:
        df[col] = df[col].astype(str).str.strip()

    # Fill NaNs so string comparisons behave predictably
    df = df.fillna("")

    # Normalize schema_type so "input" / " Input " etc. all match
    df["schema_type"] = df["schema_type"].astype(str).str.strip().str.title()

    # Drop rows with no identity (blank key columns across the board)
    df = df[df[key_cols].ne("").any(axis=1)]

    # An element is "InOut" if the same identity appears with BOTH
    # an Input row and an Output row
    schema_sets = df.groupby(key_cols)["schema_type"].agg(set)
    inout_keys = set(schema_sets[schema_sets >= {"Input", "Output"}].index)

    keys = pd.MultiIndex.from_frame(df[key_cols])
    # InOut is either (a) the same key appearing as both an Input row and an
    # Output row, or (b) a single row pre-consolidated as "Input/Output"
    is_inout = keys.isin(inout_keys) | (df["schema_type"] == "Input/Output")

    inout_df = df[is_inout]
    input_df = df[~is_inout & (df["schema_type"] == "Input")]
    output_df = df[~is_inout & (df["schema_type"] == "Output")]

    # Compress: set schema_type to this file's label, de-duplicate, sort.
    # InOut elements exist as two rows (one Input, one Output); once
    # schema_type is overwritten they collapse into one via drop_duplicates.
    def finalize(part: pd.DataFrame, schema_label: str) -> pd.DataFrame:
        part = part.copy()
        part["schema_type"] = schema_label
        return part.drop_duplicates().sort_values(key_cols)

    stem = csv_path.stem  # e.g. "elements-hierarchy"
    for label, part in (
        ("input", finalize(input_df, "Input")),
        ("output", finalize(output_df, "Output")),
        ("inout", finalize(inout_df, "InOut")),
    ):
        out_path = csv_path.with_name(f"{stem}-{label}.csv")

        # Skip empty dataframes so we don't write header-only files
        if part.empty:
            print(f"   {label:<6}     0 rows -> skipped (empty)")
            continue

        part.to_csv(out_path, index=False)
        print(f"   {label:<6} {len(part):>5,} rows -> {out_path.name}")


# ------------------------------------------------------------
# Run
# ------------------------------------------------------------

for path, key_cols in FILES.items():
    split_by_schema_type(path, key_cols)

print("\nDone!")
