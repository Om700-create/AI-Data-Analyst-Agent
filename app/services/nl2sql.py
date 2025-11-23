import requests
from ..config import HF_API_TOKEN, HF_MODEL_ID

HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

def call_llm(prompt: str, max_new_tokens: int = 256) -> str:
    """
    Generic helper to call HF text generation.
    """
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_new_tokens,
            "temperature": 0.2,
            "do_sample": False
        }
    }
    response = requests.post(HF_API_URL, headers=HEADERS, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()
    # HF returns a list of dicts: [{"generated_text": "..."}]
    if isinstance(data, list) and len(data) > 0:
        return data[0].get("generated_text", "")
    return str(data)

def extract_sql_from_text(text: str) -> str:
    """
    Extract SQL from LLM output. We expect it to return either plain SQL
    or something like:

    SELECT ...
    FROM sales
    WHERE ...

    We keep it simple: take lines from first 'SELECT' to the end of statement.
    """
    lines = text.splitlines()
    sql_lines = []
    recording = False
    for line in lines:
        if "select" in line.lower():
            recording = True
        if recording:
            sql_lines.append(line.strip())
    sql = " ".join(sql_lines)
    # Remove trailing markdown fences if any
    sql = sql.replace("```sql", "").replace("```", "").strip()
    return sql

def generate_sql_from_question(question: str, table_schema: str, table_name: str = "sales") -> str:
    """
    Convert a natural language question into SQL using LLM.
    """
    prompt = f"""
You are an expert data analyst. Your job is to write a single valid SQLite SQL query only.

Table schema:
{table_schema}

Rules:
- Only use the table: {table_name}
- Use valid SQLite syntax.
- Do not use JOINs or other tables.
- Do not explain. Return only the SQL.

Question: {question}

SQL:
"""
    raw_output = call_llm(prompt)
    sql = extract_sql_from_text(raw_output)
    return sql
