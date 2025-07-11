# config.py

"""Loads environment variables and provides central config for agents"""

import os
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "AI_Powered_Financial_Intelligence")

# DB connection for PGVector
PGVECTOR_CONN_STRING = os.getenv(
    "PGVECTOR_CONN_STRING",
    "postgresql+psycopg2://ai:ai@localhost:5532/ai"
)

def check_env():
    """Simple check for critical env vars, warn if missing"""
    if not OPENAI_API_KEY:
        print("Warning: OPENAI_API_KEY is not set!")
    if not LANGCHAIN_API_KEY:
        print("Warning: LANGCHAIN_API_KEY is not set!")
    if not PGVECTOR_CONN_STRING:
        print("Warning: PGMVECTOR_CONN_STRING is not set (using default)")

if __name__ == "__main__":
    print("OPENAI_API_KEY =", OPENAI_API_KEY)
    print("LANGCHAIN_API_KEY =", LANGCHAIN_API_KEY)
    print("LANGCHAIN_TRACING_V2 =", LANGCHAIN_TRACING_V2)
    print("LANGCHAIN_PROJECT =", LANGCHAIN_PROJECT)
    print("PGVECTOR_CONN_STRING =", PGVECTOR_CONN_STRING)
    check_env()
# 