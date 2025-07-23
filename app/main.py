from fastapi import FastAPI
from pydantic import BaseModel
from app.sql_generator import question_to_sql
from app.utils import execute_sql
from app.db import init_db

app = FastAPI()

class Query(BaseModel):
    question: str

@app.on_event("startup")
def setup():
    init_db()

@app.post("/ask")
def ask_agent(q: Query):
    sql = question_to_sql(q.question)
    result = execute_sql(sql)
    return {
        "question": q.question,
        "sql_generated": sql,
        "result": result
    }