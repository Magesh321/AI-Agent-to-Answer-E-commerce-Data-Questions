import sqlite3
import pandas as pd

def execute_sql(sql_query: str):
    try:
        conn = sqlite3.connect("ecommerce.db")
        df = pd.read_sql_query(sql_query, conn)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
