---
id: "17-tools-and-frameworks/gradio-streamlit/references"
topic: "Gradio & Streamlit (interactive ML demos & apps) — References"
parent: "17-tools-and-frameworks/gradio-streamlit"
type: references
updated: 2026-09-14
---

# Gradio & Streamlit — Interactive ML Demos & Apps — references

> Companion link library for **[Gradio & Streamlit — Interactive ML Demos & Apps](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/gradio-and-streamlit/gradio-and-streamlit)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Ship a demo in 5 lines** — read the [Gradio Quickstart](https://www.gradio.app/guides/quickstart). *Wrap a function in `gr.Interface` and you have a live UI immediately.*
2. **Watch it built** — [Gradio Crash Course](https://www.youtube.com/watch?v=eE7CamOE-PA) (AssemblyAI). *Components, inputs/outputs, and sharing in one sitting.*
3. **Build a data app** — work the [Streamlit Get Started](https://docs.streamlit.io/get-started). *The script-reruns-on-interaction model is Streamlit's whole mental model.*
4. **See Streamlit end to end** — [Streamlit Crash Course: From Zero to Data App](https://www.youtube.com/watch?v=d7fnzDQ5qM8) (Streamlit). *Widgets, layout, caching, and deploy.*
5. **Choose the right tool** — Gradio for model demos / HF Spaces, Streamlit for dashboards; browse the [Gradio guides](https://www.gradio.app/guides) and [Streamlit gallery](https://streamlit.io/gallery). *Seeing real examples makes the choice obvious.*

**In this platform**:
- [08 Hugging Face](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/hugging-face/hugging-face) — pairs with: *(Gradio powers HF Spaces)*
- [10. GenAI](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/readme) — related domain.
- [12. Deployment & MLOps](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/readme) — related domain.
- [RAG & LLM Applications](/ai-ml/practitioner-workflows/llm-applications/rag-foundations/rag-foundations) — deeper concept (the *why*): demos, serving & deployment: LLM apps.

**Videos**:
- [Gradio Crash Course — Fastest way to build & share ML apps](https://www.youtube.com/watch?v=eE7CamOE-PA) — **AssemblyAI** — the complete Gradio intro.
- [How to Build a Streamlit App (Beginner tutorial)](https://www.youtube.com/watch?v=-IM3531b1XU) — **Mısra Turp** — a friendly first Streamlit app.
- [Hugging Face Course (full playlist)](https://www.youtube.com/playlist?list=PLo2EIpI_JMQvWfQndUesu0nPBAtZ9gP1o) — **Hugging Face** — includes the Gradio chapter: Interfaces, Blocks, and publishing a demo to Spaces, taught by the maintainers.
- [Streamlit Crash Course: From Zero to Data App](https://www.youtube.com/watch?v=d7fnzDQ5qM8) — **Streamlit** — the official end-to-end crash course.

**Papers**:
- [Gradio: Hassle-Free Sharing and Testing of ML Models in the Wild](https://arxiv.org/abs/1906.02569) — **Abid et al. (2019)** — the foundational paper introducing Gradio (free on arXiv).

**Documentation**:
- [Gradio — build a chatbot fast](https://www.gradio.app/guides/creating-a-chatbot-fast) — **Gradio (Hugging Face)** — `gr.ChatInterface` with streaming and history; the default shape of an LLM demo in 2026.
- [Gradio as an MCP server](https://www.gradio.app/guides/building-mcp-server-with-gradio) — **Gradio (Hugging Face)** — expose your demo's functions as Model Context Protocol tools, so an agent can call the app you just built.
- [Gradio guides & docs](https://www.gradio.app/guides) — **Gradio (Hugging Face)** — the authoritative, structured guides from quickstart to advanced.
- [Gradio Quickstart](https://www.gradio.app/guides/quickstart) — **Gradio** — a live UI in a few lines.
- [Streamlit API reference](https://docs.streamlit.io/develop/api-reference) — **Streamlit** — every widget and layout primitive.
- [Streamlit chat elements](https://docs.streamlit.io/develop/api-reference/chat) — **Streamlit** — `st.chat_message` and `st.write_stream` for conversational data apps.
- [Streamlit documentation](https://docs.streamlit.io/) — **Streamlit (Snowflake)** — the official guide: get started, API reference, and deployment.
- [Streamlit Get Started](https://docs.streamlit.io/get-started) — **Streamlit** — the reactive-script model and first app.

**Books**:
- [Gradio guides (full set)](https://www.gradio.app/guides) — **Gradio** — a free, chapter-structured progression.
- [Streamlit documentation (full)](https://docs.streamlit.io/) — **Streamlit** — a book-length, free guide including the gallery of [examples](https://streamlit.io/gallery).
