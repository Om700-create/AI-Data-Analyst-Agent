
---

## 🔟 FastAPI App – `app/main.py`

This is the core: API, CORS, static files, `/ask` endpoint.

```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .db import get_table_schema, run_sql_query
from .schemas import AskQueryRequest, AskQueryResponse, ResultPreview
from .services.nl2sql import generate_sql_from_question
from .services.analysis import safe_plot_from_dataframe, generate_explanation

app = FastAPI(
    title="AI Data Analyst Agent",
    description="Ask questions in natural language, get SQL + charts + explanations.",
    version="0.1.0",
)

# CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (index.html + plots)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def root():
    return {
        "message": "AI Data Analyst Agent API. Go to /docs for Swagger UI or /static/index.html for the web UI."
    }

@app.post("/ask", response_model=AskQueryResponse)
def ask_query(payload: AskQueryRequest):
    """
    Main endpoint:
    1. Get table schema
    2. Generate SQL from question
    3. Run SQL
    4. Generate plot
    5. Ask LLM for explanation
    """
    try:
        schema_text = get_table_schema(payload.table)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading schema: {e}")

    # Step 1: NL -> SQL
    try:
        sql = generate_sql_from_question(
            question=payload.question,
            table_schema=schema_text,
            table_name=payload.table,
        )
        if not sql.lower().startswith("select"):
            raise ValueError("Generated SQL does not start with SELECT.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating SQL: {e}")

    # Step 2: Execute SQL
    try:
        df = run_sql_query(sql)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing SQL: {e}")

    # Step 3: Plot
    plot_url = safe_plot_from_dataframe(df)

    # Step 4: Explanation
    try:
        explanation = generate_explanation(payload.question, sql, df)
    except Exception as e:
        explanation = f"Failed to generate explanation: {e}"

    # Prepare preview (limit rows to avoid huge payloads)
    preview_rows = df.head(20).values.tolist()
    preview_cols = list(df.columns)

    result_preview = ResultPreview(columns=preview_cols, rows=preview_rows)

    return AskQueryResponse(
        question=payload.question,
        generated_sql=sql,
        result_preview=result_preview,
        plot_url=plot_url,
        explanation=explanation,
        meta={
            "row_count": int(df.shape[0]),
            "columns": preview_cols,
        },
    )
