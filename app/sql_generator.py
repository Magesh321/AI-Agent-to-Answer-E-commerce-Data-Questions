from app.llm_gemini import ask_llm
import re

def question_to_sql(question: str) -> str:
  
    q = question.lower().strip()

    prompt = f"""
You are an expert SQL assistant.

You have access to the following tables:
1. ad_sales(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)
2. eligibility(eligibility_datetime_utc, item_id, eligibility, message)
3. total_sales(date, item_id, total_sales, total_units_ordered)

When the question is about total sales or aggregated figures, your SQL MUST use aggregation functions like SUM(), AVG() etc.

Return ONLY the SQL query — do NOT provide any explanation or markdown.

Question: \"\"\"{question}\"\"\"
"""


    raw = ask_llm(prompt)

   
    cleaned = re.search(r"(SELECT[\s\S]+?;)", raw, re.IGNORECASE)
    if cleaned:
        return cleaned.group(1).strip()
    
   
    return raw.strip()
