import sys
import os

# Ensure src folder is in path
project_root = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(project_root, 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from agent4_evaluator import reviewer as agent4

# Test input for Agent 4: RAG Evaluation
user_query = (
    "How is Goldman Sachs using AI in the BFSI sector to enhance its wealth "
    "management and trading operations?"
)

retrieved_passages = [
    "Goldman Sachs has deployed AI-driven portfolio optimization engines that adjust asset allocations in real-time based on market signals and individual risk profiles.",
    "The bank employs NLP models to analyze financial news and social media sentiment, integrating those insights directly into its risk management frameworks."
]

model_answer = (
    "Goldman Sachs leverages machine learning-based portfolio optimization to continuously rebalance client portfolios "
    "according to shifting market conditions and personalized risk targets. They also use natural language processing "
    "to monitor news and social media sentiment, feeding those signals into trading algorithms and risk models. "
    "Additionally, AI-powered chatbots deliver personalized client support within their digital wealth platform, and "
    "NLP-driven compliance tools automatically flag regulatory issues, improving operational efficiency and reducing risk."
)

print("=== TEST AGENT 4: RAG Evaluation ===")

# Invoke the evaluator and stream output
review_report = agent4.assess_response(
    user_query,
    model_answer,
    retrieved_passages,
    stream=True
)

# If not streaming, print the full report
if not hasattr(review_report, 'read'):
    print(review_report)
