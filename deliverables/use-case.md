# Use Case

## Narrative

With the advent of Large Language Models (LLMs), scientists and everyday
users have been experimenting with ways to integrate them into their workflows
or improve their experimentation processes. A common method for achieving this
is to create assistants that have access to domain-specific data via techniques
such as RAG, fine-tuning, few-shot prompting, and other various methodologies
[1]. To further enhance the capabilities of these LLM assistants, Model
Context Protocol (MCP) servers were introduced and is becoming the standard
framework for quickly implementing agentic tool usage, as an alternative to
Application Programming Interfaces (APIs) [2].

When LLM models are paired with an MCP server, many issues can arise. For example, to name a few issues that frequently occur are tool selection failure (i.e., not identifying and selecting a tool that exists), incorrect tool calls, non-explicit expected tool chain breaks, tool misuse, tool and argument hallucinations, and forgotten context as the context window threshold is reached [3]. To remedy the issue with tool chains within an MCP, it is recommended to explicitly chain tools together, i.e., call other tools within the initially called tool. While an acceptable solution to some of the errors noted above, explicit tool chaining is not allowed or typically absent in datasets when testing or benchmarking an LLM's reasoning capabilities.

Given the experimental conditions for using tool benchmarks to evaluate LLM capabilities, we want to engineer an ontology that enables LLMs, specifically low-parameter models, to reason more effectively about the MCP tools available to them without explicit instructions in the tools themselves. This would meet the need for flagship-model tooling capabilities, but on local models using consumer-grade hardware.

## Research Questions

**RQ1**: Will the introduction of an OWL-based KG into an agentic workflow involving tool usage improve the tool-use performance of SLMs? \
**RQ2**: Does the inclusion of an OWL-based KG improve the error recovery performance of SLMs following MCP tool-use errors?

## Competency Questions

**Tool Selection, Usage, Chaining, and Failure Recovery**: These CQs focuses on the identification of tools, their inputs and outputs, the various ways they might relate to each other, and how failures can be recovered.

1. What subsets of `Tools` have `Outputs` matching the `Datatypes` and `Element` structures of other tool `Inputs`? \
   1a) What is the `OutputParameter` for a given `Tool`, and what are its expected `Datatype` and `Element` structure? \
   1b) What are all the `Optional` `Parameters` for a given `Tool`, and what are their expected `Datatypes` and `Element` structures? \
   1c) What are all the `Required` `InputParameters` for a given `Tool`, and what are their expected `Datatypes` and `Element structures`?
2. What is the list of `Tools` for each available `Server`? \
   2a) To which `Server` does a given `Tool` belong?
3. If a `Tool` encounters a `FailureMode`, what is the appropriate response to that `FailureMode`?
4. What is the description of a given `Tool` and its required `Parameters`?
5. What are the descriptions of a `Tool` and ALL of its `Parameters`?
6. What is the description of a Tool's `Output Parameters`?
7. How many `Tools` does a given `Server` have?
8. What are the descriptions of the `Tools` from a given set of available `Tools`?
9. Which `Servers` have `Tools` that produce an `Output`, and how many?
10. If `Outputs` exist from a set of `Tools`, do any `Datatypes` overlap, and how many?
11. What are all the required `Input Parameters` for a given set of `Tools`, and what are their descriptions, expected `Datatypes`, and `Element structures`?

Bridges Datasets: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

## Potential Datasets

1. [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas),
2. [Toolathlon](https://toolathlon.xyz/docs/dataset),
3. [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

## References

[1] Chowa, S.S., Alvi, R., Rahman, S.S., Rahman, M.A., Azam, M., Islam, M.R., Hussain, M., Azam, S.: From language to action: a review of large language models as autonomous agents and tool users. Artificial Intelligence Review 59(2) (Jan 2026). https://doi.org/https://doi.org/10.1007/s10462-025-11471-9

[2] Gao, X., Xie, S., Zhai, J., Ma, S., Shen, C.: Mcp-radar: A multi-dimensional benchmark for evaluating tool use capabilities in large language models (2025), https://arxiv.org/abs/2505.16700

[3] Winston, C., Just, R.: A taxonomy of failures in tool-augmented llms. In: 2025
IEEE/ACM International Conference on Automation of Software Test (AST). pp. 125–135 (2025). https://doi.org/10.1109/AST66626.2025.000
