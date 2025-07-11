import sys
import os
from textwrap import dedent

# Ensure src folder is in path
project_root = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(project_root, 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from src.agent3_stock_analysis import agent3

# Test Case 1: Latest financial snapshot for Goldman Sachs
query1 = dedent("""
    Please provide the latest financial snapshot for Goldman Sachs (GS), including:
    - Current share price
    - 52-week high and low
    - P/E ratio and EPS
    - Recent analyst recommendations
    - A brief forward-looking outlook
""")
result1 = agent3.invoke({"input": query1})
print("\nQ1:", query1, "\nA1:\n", result1.get("output"))

# Test Case 2: Comparative analysis of leading banks
query2 = dedent("""
    Conduct a comparative financial review of these global banks:
    - Goldman Sachs (GS)
    - JPMorgan Chase (JPM)
    - HSBC Holdings (HSBC)
    - Barclays (BCS)

    For each institution, include:
    1. Most recent quarterly results (revenue, net income)
    2. Key profitability metrics (ROE, ROA)
    3. Capital adequacy (CET1 ratio)
    4. Credit quality indicators (NPL ratio, provisions)
    5. Forward-looking outlook and primary risk factors

    Then summarize:
    • Which bank appears best positioned for interest-rate changes
    • Comparative strengths and vulnerabilities in the current macroeconomic environment
    • Any notable strategic initiatives or M&A activity affecting their outlook
""")
result2 = agent3.invoke({"input": query2})
print("\nQ2:", query2, "\nA2:\n", result2.get("output"))

# Test Case 3: JPMorgan Chase strategy
query3 = dedent("""
    How is JPMorgan Chase (JPM) navigating the current rising interest rate environment and credit risk landscape?
""")
result3 = agent3.invoke({"input": query3})
print("\nQ3:", query3, "\nA3:\n", result3.get("output"))
