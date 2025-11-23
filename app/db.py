from sqlalchemy import create_engine, text, inspect
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
from .config import DATABASE_URL

engine = create_engine(DATABASE_URL, future=True)

def get_table_schema(table_name: str) -> str:
    """
    Returns a simple text description of the table schema.
    """
    inspector = inspect(engine)
    cols = inspector.get_columns(table_name)
    lines = []
    for col in cols:
        lines.append(f"{col['name']} ({col['type']})")
    return f"Table '{table_name}' columns: " + ", ".join(lines)

def run_sql_query(sql: str) -> pd.DataFrame:
    """
    Executes a SQL query and returns a DataFrame.
    """
    try:
        with engine.connect() as conn:
            df = pd.read_sql(text(sql), conn)
        return df
    except SQLAlchemyError as e:
        raise RuntimeError(f"SQL execution error: {e}")
