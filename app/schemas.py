from pydantic import BaseModel
from typing import List, Any, Optional, Dict

class AskQueryRequest(BaseModel):
    question: str
    table: str = "sales"  # default table

class ResultPreview(BaseModel):
    columns: List[str]
    rows: List[List[Any]]

class AskQueryResponse(BaseModel):
    question: str
    generated_sql: str
    result_preview: ResultPreview
    plot_url: Optional[str]
    explanation: str
    meta: Dict[str, Any] = {}
