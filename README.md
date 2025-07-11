# Multi-Agent-AI-Platform-for-Finance-and-Market-Research

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
---

## 🎯 Business Challenge

My goal in this project is to accelerate and enrich financial/market research, analysis by orchestrating specialized AI agents, RAG, LLMs to streamline research, document retrieval, stock analysis, market analysis and expert review. So that high-quality investment reports can be produced faster, with deeper insights and reliable sourcing.

---

## 🏛️ Solution Architecture

![Architecture Diagram](solution_architecture.png)

---

## 🧠 Why AI Agents for Financial/Market Research?

* **Faster, Deeper Analysis**: Instantly synthesize data and news far beyond manual tools.
* **Collaborative Expertise**: Specialized agents cover research, retrieval, analysis, and review in one workflow.
* **Up-to-Date & Cited**: Agents pull the latest info and transparently cite sources—no more stale data.


---
## 🤖 AI Agent Roles and Capabilities Overview :

| **Agent** | **Role / Specialty**               | **Main Parameters / Components**                                                             | **Special Functions / Tools**                                             |
| --------- | ---------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Agent 1   | Financial/Market Research & Web Search    | - GoogleSearchAPIWrapper<br>- ChatOpenAI (gpt-4.1)<br>- Article extraction with requests\_html | Fetches news, scrapes articles, sources market insights                   |
| Agent 2   | RAG Document Retrieval & QA        | - HuggingFaceEmbeddings<br>- Chroma vector DB<br>- PyPDFLoader<br>- OpenAI (gpt-3.5-turbo)   | Loads/splits PDFs, builds vector store, answers with retrieval QA         |
| Agent 3   | Stock Data & Financial/Market Analysis    | - yfinance<br>- ChatOpenAI (ggpt-4o)<br>- ReAct agent with custom prompt               | Live stock info (price, ratios), structured multi-ticker comparison       |
| Agent 4   | Review & Synthesis (RAG Evaluator) | - Custom RAGReview class<br>- ChatOpenAI (gpt-o4-mini-high)<br>- PromptTemplate scoring rubric  | Scores output (accuracy, relevance, citations), synthesizes and critiques |


**Evaluation criteria with metrics:**

* **Accuracy & Relevance**: Are insights factually correct and directly answer the query? *(Measured by correctness and relevance scores)*
* **Response Latency (LangChain Metric):** How quickly each agent returns an answer, measured in seconds—critical for time-sensitive financial analysis.
* **Contextual Relevance & Factuality (Model Metrics):** Are answers accurate and grounded in retrieved documents or live data? Evaluated by fact-checking rate and retrieval overlap.
* **Citation Quality & Traceability (Custom/Chain Metric):** Do responses provide clear, verifiable source links or references? Scored by presence and completeness of citations.

---

## 🏆 Project Goals

1. **Multi-Source Data Acquisition**
   * Real-time news search, PDF document retrieval, and live financial data extraction.
2. **Automated Knowledge Extraction**
   * LLM-driven summarization, RAG-based context retrieval, and structured stock metric parsing.
3. **Agent Orchestration**
   * Workflow routing: query → research agent → RAG agent → analysis agent → review agent.
4. **Synthesis & Structured Reporting**
   * Section-wise assembly: executive summary, financials, risk, peer analysis, citations.
5. **Evaluation & Validation**
   * Metrics: response latency, factual accuracy, citation completeness, relevance scoring.
6. **Result Delivery & Transparency**
   * Export as markdown/PDF, all findings traceable to cited, time-stamped sources.

---


## 🔧 Installation & Quick Start


# 1. Clone repo
```bash
git clone https://github.com/your_username/ai_agents_for_finance_market_research.git](https://github.com/SindhePandurangBITS/Multi-Agent-AI-Platform-for-Finance-and-Market-Research.git
cd ai_agents_for_finance_market_research
```
# 2. Create & activate venv
```bash
python3 -m venv venv
source venv/bin/activate
```

# 3. Install dependencies
```bash
pip install -r requirements.txt
```
# 4. Start supporting services
```bash
docker-compose up -d
```
# 5. Run Agent Tests Individually
```bash
python tests/test_agent1.py
python tests/test_agent2.py
python tests/test_agent3.py
python tests/test_agent4.py
```
# 6. Launch the Streamlit Dashboard
```bash
streamlit run streamlit.py
```
---

Absolutely! Here’s a similar section tailored for your `ai_agents_for_finance_market_research` repo and the folders you have:

---

## 📖 Documentation & Notebooks

Key workflows and demos are documented in the `notebooks` folder:

* **agent\_demo:** End-to-end demo of all four AI agents on real market queries.
* **financial\_research:** How to run deep-dive financial research using Agent 1.
* **rag\_document\_qa:** Using ChromaDB and PDF-based retrieval with Agent 2.
* **stock\_analysis:** Interactive stock and peer comparison via Agent 3.
* **report\_orchestration:** Full workflow—combining agent outputs into structured investment reports.
* **evaluation\_metrics:** Scoring and reviewing outputs with Agent 4.

> For configuration and custom runs, see `src/config.py` and the `README.md`.


---
⭐ Support
If this project helped you, please ⭐ star the repository and share!

---

## 📑 Key References

1. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**  
   _Patrick Lewis et al., NeurIPS 2020_  
   🔗 [Paper](https://arxiv.org/abs/2005.11401)  
   > **Overview:** Introduces the RAG framework that combines a learned retriever with a seq-to-seq generator for open-domain question answering—foundational for your document-driven agent.

2. **REALM: Retrieval-Augmented Language Model Pre-Training**  
   _Kelvin Guu et al., ICML 2020_  
   🔗 [Paper](https://arxiv.org/abs/2002.08909)  
   > **Overview:** Shows end-to-end training of retrieval and language-model components, informing vector-database setups like your PgVector usage.

3. **Toolformer: Language Models Can Teach Themselves to Use Tools**  
   _Timo Schick et al., arXiv 2023_  
   🔗 [Paper](https://arxiv.org/abs/2302.04761)  
   > **Overview:** Demonstrates how LLMs can self-instruct to integrate external APIs/tools—directly applicable to your agent’s tool-calling mechanism.

4. **GPT4Tools: Teaching Large Language Models to Use Tools via Self-Instruction**  
   _Rui Yang et al., arXiv 2023_  
   🔗 [Paper](https://arxiv.org/abs/2305.18752)  
   > **Overview:** Proposes a self-instruction dataset approach enabling open-source LLMs to learn tool usage, complementing your Groq-based integrations.
