temparature: 0
from langchain.agents import create_react_agent, AgentExecutor 
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from textwrap import dedent
from langchain.tools import Tool
import yfinance as yf

def get_stock_info(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period="1y")
        
        return f"""
Stock: {ticker}
Current Price: ${info.get('currentPrice', 'N/A')}
52-Week High: ${info.get('fiftyTwoWeekHigh', 'N/A')}
52-Week Low: ${info.get('fiftyTwoWeekLow', 'N/A')}
P/E Ratio: {info.get('trailingPE', 'N/A')}
EPS: {info.get('trailingEps', 'N/A')}
Market Cap: ${info.get('marketCap', 'N/A')}
"""
    except Exception as e:
        return f"Error getting data for {ticker}: {e}"

yfinance_tool = Tool(
    name="YFinance",
    func=get_stock_info,
    description="Get stock information. Input: ticker symbol"
)
tools = [yfinance_tool]
stock_analysis_prompt = dedent("""
    You are a senior credit analyst with expertise in equity markets.

    **Analysis Workflow**
    1. Market Snapshot
       - Real‐time share price
       - 52-week high/low
    2. Key Financial Ratios
       - P/E ratio
       - Market capitalization
       - EPS
    3. Industry Context
       - Sector trends
       - Competitor comparison
       - Market sentiment indicators

    **Reporting Guidelines**
    - Start with an executive summary
    - Present figures in tables
    - Use clear section headings
    - Highlight top insights as bullet points
    - Benchmark against industry averages
    - Provide definitions for specialized terms
    - Finish with forward‐looking observations

    **Risk Disclosures**
    - Outline principal risk factors
    - Note market volatility
    - Mention any regulatory issues
You have access to the following tools:
{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought: {agent_scratchpad}
""")

prompt_template = PromptTemplate(
    input_variables=["input", "tools", "tool_names", "agent_scratchpad"],
    template=stock_analysis_prompt
)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

agent = create_react_agent(llm, tools, prompt_template)
agent3 = AgentExecutor(agent=agent, tools=tools, verbose=True)
