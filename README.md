# Tool-Coupler

Tool-Coupler is an ontology for describing
the relationships between MCP servers or APIs, their tools, tool parameters, resources, metadata, and tool related failure modes. The repository contains the ontology, ontology design documentation, schema visualizations, source data, and scripts used to prep data and materialize the knowledge graph.

## Key Resources

- [Ontology](deliverables/ontology/tool-coupler.ttl) is the aggregate OWL ontology artifact.
- [Ontology axioms](deliverables/ontology/tool-coupler-axioms.md) provides the ontology axioms in natural language.
- [Full schema PDF](deliverables/patterns/full-schema.pdf) provides a visual representation of the complete ontology schema.
- [Key notions](deliverables/key-notions.md) documents the central concepts represented in the ontology.
- [Use case](deliverables/use-case.md) describes the motivating use case for the ontology, including the appropriate research and ontology related questions.

## Repository Map

| Directory                                                     | Intent                                                                                                                                                   |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [deliverables](deliverables/)                                 | Contains the ontology, ontology documentation, schema visualizations, and materialized RDF/TTL artifacts.                                                |
| [deliverables/ontology](deliverables/ontology/)               | Contains the aggregate OWL ontology and its axiomatization in natural language.                                                                          |
| [deliverables/patterns](deliverables/patterns/)               | Contains GraphML and PDF visualizations of the complete ontology and its individual patterns, including Tool, Metadata, Resource, and FailureMode.       |
| [deliverables/materialization](deliverables/materialization/) | Contains the materialized RDF/TTL outputs generated from the source data and mappings.                                                                   |
| [deliverables/queries](deliverables/queries/)                 | Contains the SPARQL queries associated with each CQ.                                                                                                     |
| [scripts](scripts/)                                           | Contains scripts, source data, mappings, and utilities used to generate and materialize the ontology data.                                               |
| [scripts/data](scripts/data/)                                 | Contains the tabular and text source data used during ontology materialization.                                                                          |
| [scripts/materialization](scripts/materialization/)           | Contains the scripts and mappings used to transform source data into materialized RDF/TTL artifacts.                                                     |
| [scripts/axiomatization](scripts/axiomatization/)             | Contains the script used to convert ontology axioms into natural language.                                                                               |
| [benchmarks](benchmarks)                                      | Contains the benchmark data for evaluations, scoring, and diagnostics from the MCP-Atlas benchmark.                                                      |

## Ontology Patterns

The ontology is organized around several core patterns:

| Pattern                                                                  | Description                                                               |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| [Tool](deliverables/patterns/tool/tool.pdf)                              | Represents the tool-oriented portion of the ontology.                     |
| [Metadata](deliverables/patterns/metadata/metadata-pattern.pdf)          | Represents metadata associated with the modeled resources.                |
| [Resource](deliverables/patterns/resource/resource.pdf)                  | Represents the resource-oriented portion of the ontology.                 |
| [FailureMode](deliverables/patterns/failuremode/failuremode-pattern.pdf) | Represents failure-mode information associated with the modeled entities. |

## Namespaces

| Prefix   | Namespace                                                 |
| -------- | --------------------------------------------------------- |
| `tc-ont` | `https://kastle-lab.github.io/tool-coupler/lod/ontology#` |
| `tc-r`   | `https://kastle-lab.github.io/tool-coupler/lod/resource#` |

## Tooling

[Kastle Foundry](https://github.com/kastle-lab/foundry) was used to materialize RDF/Turtle graph fragments from the synthetic CSV data and YAML mappings.

## Validation Status

<p>
  <a href="http://oops.linkeddata.es">
    <img src="https://oops.linkeddata.es/images/conformance/oops_free.png"
      alt="free pitfalls were found" height="69.6" width="100" />
  </a>
</p>

The ontology has been checked with OOPS and detected no critical pitfalls.

## License

This repository is licensed under the terms in [LICENSE](LICENSE).
