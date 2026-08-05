#!/usr/bin/env bash
# Runs all kastle-foundry materialization steps in sequence.
# Exits immediately if any step fails.

set -euo pipefail

FOUNDRY="kastle-foundry.py"
NAMESPACE="https://kastle-lab.github.io/tool-coupler"
PREFIX="tool-coupler"

run_step() {
    local step_name="$1"
    local mapping="$2"
    local data="$3"
    local output="$4"
    local log_file="$5"

    echo "=================================================="
    echo "Running step: ${step_name}"
    echo "=================================================="

    python3 "${FOUNDRY}" \
        -m "${mapping}" \
        -d "${data}" \
        -o "${output}" \
        --namespace "${NAMESPACE}" \
        --prefix "${PREFIX}" \
        --log-file "${log_file}" \
        --verbose

    echo "Completed: ${step_name}"
    echo
}

# 1. server-tools-mapping
run_step "server-tools-mapping" \
    "./mappings/server-tools-mapping.yml" \
    "../../scripts/data/tools.csv" \
    "../../deliverables/materialization/servers-tools" \
    "../../server-tools-materialization.log"

# 2. tool-input-parameter-mapping
run_step "tool-input-parameter-mapping" \
    "./mappings/tool-input-parameter-mapping.yml" \
    "../../scripts/data/server-tools-input.csv" \
    "../../deliverables/materialization/tool-input-parameters" \
    "../../tool-input-parameter-materialization.log"

# 3. tool-output-parameter-mapping
run_step "tool-output-parameter-mapping" \
    "./mappings/tool-output-parameter-mapping.yml" \
    "../../scripts/data/server-tools-output.csv" \
    "../../deliverables/materialization/tool-output-parameters" \
    "../../tool-output-materialization.log"

# 4. input-parameter-elements-mapping
run_step "input-parameter-elements-mapping" \
    "./mappings/input-parameter-elements-mapping.yml" \
    "../../scripts/data/parameters-to-elements-input.csv" \
    "../../deliverables/materialization/input-parameter-elements" \
    "../../input-parameter-elements-mapping.log"

# 5. output-parameter-elements-mapping
run_step "output-parameter-elements-mapping" \
    "./mappings/output-parameter-elements-mapping.yml" \
    "../../scripts/data/parameters-to-elements-output.csv" \
    "../../deliverables/materialization/output-parameter-elements" \
    "../../output-parameter-elements-mapping.log"

# 6. input-element-hierarchy-mapping
run_step "input-element-hierarchy-mapping" \
    "./mappings/input-element-hierarchy-mapping.yml" \
    "../../scripts/data/elements-hierarchy-input.csv" \
    "../../deliverables/materialization/elements-of-elements" \
    "../../input-element-hierarchy-mapping.log"

# 7. tool-inout-parameter-mapping
run_step "tool-inout-parameter-mapping" \
    "./mappings/tool-inout-parameter-mapping.yml" \
    "../../scripts/data/server-tools-inout.csv" \
    "../../deliverables/materialization/tool-inout-parameters" \
    "../../tool-inout-parameter-mapping.log"

# 8. Controlled Vocabularies
run_step "controlled-vocabularies" \
    "./mappings/controlled-vocabularies.yml" \
    "../../scripts/data/controlled-vocabularies.csv" \
    "../../deliverables/materialization/controlled-vocabularies" \
    "../../controlled-vocabularies.log"
echo "All materialization steps completed successfully."