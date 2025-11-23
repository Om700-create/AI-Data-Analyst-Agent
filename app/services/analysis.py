from pathlib import Path
import uuid
import pandas as pd
import matplotlib.pyplot as plt

from ..db import run_sql_query
from .nl2sql import call_llm

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
PLOTS_DIR = STATIC_DIR / "plots"
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

def safe_plot_from_dataframe(df: pd.DataFrame) -> str | None:
    """
    Creates a simple bar plot or line plot from the query result.
    Returns relative URL path to the saved plot or None.
    """
    if df.empty or df.shape[1] < 2:
        return None

    # For simplicity: use first column as x, second numeric column as y
    x_col = df.columns[0]
    # find first numeric column after x
    y_col = None
    for col in df.columns[1:]:
        if pd.api.types.is_numeric_dtype(df[col]):
            y_col = col
            break

    if y_col is None:
        return None

    plt.figure(figsize=(8, 4))
    # simple bar chart
    plt.bar(df[x_col].astype(str), df[y_col])
    plt.xticks(rotation=45, ha="right")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.tight_layout()

    file_name = f"plot_{uuid.uuid4().hex}.png"
    file_path = PLOTS_DIR / file_name
    plt.savefig(file_path)
    plt.close()

    # URL relative to /static
    return f"/static/plots/{file_name}"

def generate_explanation(question: str, sql: str, df: pd.DataFrame) -> str:
    """
    Ask LLM to explain the result in business language.
    """
    preview = df.head(10).to_markdown(index=False)
    prompt = f"""
You are a senior data analyst.

User question:
{question}

SQL query executed:
```sql
{sql}
