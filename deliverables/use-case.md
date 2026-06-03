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

**RQ1**: Does combining a KG with an MCP server yield higher efficiency by reducing the number of incorrect tool calls despite possibly taking more time due to a more complex workflow?

## Competency Questions

**Tool Selection, Usage, and Chaining**: This set of CQs focuses on the identification of tools, and the various ways they might relate to eachother

- What set of `tools` might be capable of chaining together based on their `inputs` and `outputs`?
- Which `tools` take in (`input`) `parameter type` _x_?
- Which `tools` `output` `parameter type` _x_?

Bridges Datasets: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Toolathlon](https://toolathlon.xyz/docs/dataset), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools), [LLM-STATS](https://llm-stats.com/leaderboards/best-ai-for-tool-calling)

---

## Potential Datasets

1. [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas),
2. [Toolathlon](https://toolathlon.xyz/docs/dataset),
3. [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)
4. [LLM-STATS](https://llm-stats.com/leaderboards/best-ai-for-tool-calling)

## References

[1] Chowa, S.S., Alvi, R., Rahman, S.S., Rahman, M.A., Azam, M., Islam, M.R., Hussain, M., Azam, S.: From language to action: a review of large language models as autonomous agents and tool users. Artificial Intelligence Review 59(2) (Jan 2026). https://doi.org/https://doi.org/10.1007/s10462-025-11471-9

[2] Gao, X., Xie, S., Zhai, J., Ma, S., Shen, C.: Mcp-radar: A multi-dimensional benchmark for evaluating tool use capabilities in large language models (2025), https://arxiv.org/abs/2505.16700

[3] Winston, C., Just, R.: A taxonomy of failures in tool-augmented llms. In: 2025
IEEE/ACM International Conference on Automation of Software Test (AST). pp. 125–135 (2025). https://doi.org/10.1109/AST66626.2025.000
