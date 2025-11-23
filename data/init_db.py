import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "analytics.db"
CSV_PATH = BASE_DIR / "sample_sales.csv"

def init_db():
    print("Initializing SQLite database...")
    df = pd.read_csv(CSV_PATH)

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()

    print(f"Database created at {DB_PATH}")
    print("Table 'sales' created with columns:")
    print(df.dtypes)

if __name__ == "__main__":
    init_db()
