# Tool-Coupler

## The Patterns

- Metadata
- Prompt (WIP)
- Resource
- Tool

## Deliverables

The deliverables are structured as follows.

1. **Use-Case** \
   Contains the narrative of our use case and motivation for the research, along with the initially formulated research questions (RQs), competency questions (CQs), and available datasets.
2. **Key-Notions** \
   Contains the identified concepts that overlapped with the CQs and the available data. Each key notion has a brief description of the rationale, potential existing patterns for reuse, and applicable datasets.
3. **Patterns** \
   This directory includes the schema diagrams for each constructed pattern along with the final schema.
4. **Ontology** \
   Contains OWL file with the axioms applied using the Protege software.
5. **Knowledge Graph** \
   The instance level data materialized by [Morph-kgc](https://github.com/morph-kgc/morph-kgc/) resides here.

## Scripts

1. **Data** \
   The data used for materialzing the knowlege graph resides here. Some of the files are too large, but are hosted in other locations: 
   - mcp-atlas: [list-tools.json](https://gist.github.com/geobio/e1c08cc4d74d96223cb8cf0919a72c3e)
2. **Materialization** \
   The configuration file and other scripts used for materialization are located in this directory.