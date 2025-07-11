""" DB helper for connecting to PGVector db (Postgres) """

import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import time
from pathlib import Path

def test_db_connection(conn_str, max_tries=5, wait_seconds=10):
    """ test connect to postgres and vector extention """
    for i in range(1, max_tries + 1):
        print(f"try {i}/{max_tries}…")
        try:
            engine = create_engine(conn_str)
            with engine.connect() as conn:
                version = conn.execute(text("SELECT version();")).scalar()
                print("conected! PostgreSQL ver:", version)
                conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
                print("vector extention enabled.")
                return engine
        except OperationalError:
            print(f"fail, retry after {wait_seconds}s...")
            time.sleep(wait_seconds)
    print("not able to connect after retry.")
    return None

def reset_pgvector_container(data_dir):
    # Try to kill Postgres (windows style)
    import subprocess
    import shutil
    subprocess.run(["taskkill", "/F", "/IM", "postgres.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if data_dir.exists():
        shutil.rmtree(data_dir)
    subprocess.run(["docker", "rm", "-f", "pgvector"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log = Path("postgres.log")
    if log.exists():
        log.unlink()
