import streamlit as st
import os

# --- Import your agent builders ---
from src.agent1_financial_research import get_agent1
from src.agent2_rag_qa import get_agent2
from src.agent3_stock_analysis import get_agent3
from src.agent4_evaluator import get_agent4

# --- Page config ---
st.set_page_config(page_title="AI-Powered Financial Intelligence Agents", layout="wide")

# --- Sidebar (Inputs) ---
with st.sidebar:
    st.title("Configuration")
    openai_key = st.text_input("OpenAI API Key", type="password")
    langchain_key = st.text_input("LangChain API Key", type="password")
    model = st.selectbox("Select Model", ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo", "gpt-4"])
    vectordb_url = st.text_input("Vector DB PDF Link (for Agent 2)")
    user_query = st.text_area("Your Query", height=100)
    agent_options = ["Agent 1: Financial Research", 
                     "Agent 2: RAG QA", 
                     "Agent 3: Stock Analysis", 
                     "Agent 4: LLM Evaluator (Judge)"]
    agent_select = st.radio("Choose Agent", agent_options, index=0)
    submit = st.button("Run Query")

# --- Main Output Panel ---
_, outcol = st.columns([1,2])

def format_report(sections):
    """Return markdown for all documentation report sections."""
    titles = [
        "Executive Summary", "Introduction", "Objectives", "Methodology", "Data Sources",
        "Literature Review", "Analysis", "Findings", "Discussion", "Conclusion",
        "Recommendations", "Limitations", "References", "Financial Statements", "Appendices"
    ]
    md = ""
    for title in titles:
        md += f"\n\n### {title}\n"
        md += f"{sections.get(title, 'N/A')}\n"
    return md

def parse_agent_output_to_sections(output):
    # Placeholder: you might want to improve this for your actual outputs!
    sections = {title: "" for title in [
        "Executive Summary", "Introduction", "Objectives", "Methodology", "Data Sources",
        "Literature Review", "Analysis", "Findings", "Discussion", "Conclusion",
        "Recommendations", "Limitations", "References", "Financial Statements", "Appendices"
    ]}
    # For now, everything to "Analysis"
    sections["Analysis"] = output
    return sections

with outcol:
    st.title("AI-Powered Financial Intelligence Report")
    if submit:
        os.environ["OPENAI_API_KEY"] = openai_key
        os.environ["LANGCHAIN_API_KEY"] = langchain_key

        # -- Route to the correct agent --
        if agent_select.startswith("Agent 1"):
            agent1 = get_agent1(model=model)
            result = agent1.invoke({"input": user_query})
            output = result['output'] if isinstance(result, dict) and 'output' in result else str(result)
        elif agent_select.startswith("Agent 2"):
            agent2 = get_agent2(model=model, pdf_url=vectordb_url)
            output = agent2.ask(user_query)
        elif agent_select.startswith("Agent 3"):
            agent3 = get_agent3(model=model)
            result = agent3.invoke({"input": user_query})
            output = result['output'] if isinstance(result, dict) and 'output' in result else str(result)
        elif agent_select.startswith("Agent 4"):
            agent4 = get_agent4(model=model)
            # This assumes you have functions to get the relevant inputs:
            st.info("Agent 4 expects: (1) Query, (2) a model answer, and (3) context passages.")
            model_answer = st.text_area("Paste the model answer to judge:", key="model_answer")
            context = st.text_area("Paste the retrieved context(s) (one per line):", key="context")
            if model_answer and context:
                output = agent4.assess_response(user_query, model_answer, context.split('\n'))
            else:
                output = "Please provide model answer and context for Agent 4."
        else:
            output = "Unknown agent selection."

        # --- Documentation formatting ---
        # In production, use a real output-to-section parser; here, just drop into Analysis.
        sections = parse_agent_output_to_sections(output)
        st.markdown(format_report(sections))

    else:
        st.markdown("⬅️ Set config and submit a query.")

# Optional: Add a footer or custom CSS for styling
st.markdown("""
    <style>
        .st-cg {background: #f9f9fa;}
        .st-bb {font-size: 18px;}
    </style>
""", unsafe_allow_html=True)
