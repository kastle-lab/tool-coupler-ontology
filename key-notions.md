# Key Notions

- **API/MCP**
  - <u>**Rationale**</u>: Represents the MCP server(s) or API(s) where all of the components for usage reside.
  - <u>**Connected Pattern**</u>: None
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Toolathlon](https://toolathlon.xyz/docs/dataset), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools), [LLM-STATS](https://llm-stats.com/leaderboards/best-ai-for-tool-calling)

---

- **Tool**
  - <u>**Rationale**</u>: The MCP Tool or API Function that an LLM can utilize.
  - <u>**Connected Pattern**</u>: None
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

- **Parameter**
  - <u>**Rationale**</u>: The
  - <u>**Connected Pattern**</u>: [MODL: data-transformation](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/data-transformation/data-transformation-pattern.pdf)
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

- **Parameter Type**
  - <u>**Rationale**</u>: The input or output variable associated with a Tool.
  - <u>**Connected Pattern**</u>: [MODL: data-transformation](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/data-transformation/data-transformation-pattern.pdf)
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

- **Parameter Role**
  - <u>**Rationale**</u>:
  - <u>**Connected Pattern**</u>: [MODL: data-transformation](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/data-transformation/data-transformation-pattern.pdf)
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

- **Output Role**
  - <u>**Rationale**</u>:
  - <u>**Connected Pattern**</u>: [MODL: data-transformation](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/data-transformation/data-transformation-pattern.pdf)
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

- **Input Role**
  - <u>**Rationale**</u>:
  - <u>**Connected Pattern**</u>: [MODL: data-transformation](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/data-transformation/data-transformation-pattern.pdf)
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

- **Data Transformation**
  - <u>**Rationale**</u>:
  - <u>**Connected Pattern**</u>: [MODL: data-transformation](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/data-transformation/data-transformation-pattern.pdf)
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

- **Resource**
  - <u>**Rationale**</u>: Represent the read-only data or files that an MCP client has access to.
  - <u>**Connected Pattern**</u>: None
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

- **Resource Class**
  - <u>**Rationale**</u>: The class of a resource (Http, Directory, File, Text, Binary, etc.)
  - <u>**Connected Pattern**</u>: None
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

- **Metadata**
  - <u>**Rationale**</u>: Data that defines and describes the characteristics of other data.
  - <u>**Connected Pattern**</u>: [Dublin Core™ Metadata](https://www.dublincore.org/specifications/dublin-core/dces/)
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

- **Location**
  - <u>**Rationale**</u>: The explicit location of a tool, resource, server, etc.
  - <u>**Connected Pattern**</u>: [Dublin Core™ Metadata](https://www.dublincore.org/specifications/dublin-core/dces/)
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---

- **Format**
  - <u>**Rationale**</u>: The format of a tool, resource, server, etc. For example a text file would have the format of .txt, or a video file may have the format of .mp4.
  - <u>**Connected Pattern**</u>: [Dublin Core™ Metadata](https://www.dublincore.org/specifications/dublin-core/dces/)
  - <u>**Source Dataset(s)**</u>: [MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas), [Fast-MCP](https://fastmcp.wiki/en/v2/servers/tools)

---
