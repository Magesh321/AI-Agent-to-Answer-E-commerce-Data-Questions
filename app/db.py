import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect("ecommerce.db")
    cur = conn.cursor()

    with open("sql/init_tables.sql", "r") as f:
        cur.executescript(f.read())

    pd.read_csv("data/ad_sales.csv.csv").to_sql("ad_sales", conn, if_exists="replace", index=False)
    pd.read_csv("data/total_sales.csv.csv").to_sql("total_sales", conn, if_exists="replace", index=False)
    pd.read_csv("data/eligibility.csv.csv").to_sql("eligibility", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
