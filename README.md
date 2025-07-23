# AI-Agent-to-Answer-E-commerce-Data-Questions

Project Overview
This project implements a Natural Language Interface over e-commerce advertising datasets
using Large Language Models (LLMs) and SQL databases. Users can ask natural language
questions related to ad sales, total sales, and product eligibility. The system generates
corresponding SQL queries, executes them on the imported datasets, and returns the results.

Datasets Provided
Three CSV files are used as the data source:
ad_sales.csv.csv

Contains daily product-level advertising metrics including date, item_id, ad_sales,
impressions, ad_spend, clicks, and units_sold.
total_sales.csv.csv
Contains total sales data by product and date, including fields like total_sales and
total_units_ordered.
eligibility.csv.csv
Contains product eligibility status with timestamps and messages.

Key Technologies
Python 3.8+
SQLite for local database storage of CSV data
Pandas for CSV loading and manipulation
FastAPI for REST API interface
Large Language Model (LLM) interface (e.g., Gemini 2.5, OpenAI, or Ollama) for question-to-SQL translation

Setup Instructions
1. Clone or download the project folder and create a virtual environment.
2. Place the three CSV files (ad_sales.csv.csv, total_sales.csv.csv, eligibility.csv.csv) in
the project root directory.
3. Install required packages:
pip install -r requirements.txt
4. Load CSV data into SQLite database:
Run the provided data loading script (data_loader.py):
python data_loader.py
This creates an SQLite database, ecommerce.db, with three tables: ad_sales, total_sales, and
eligibility.
5. Start the API server:
uvicorn main:app --reload
6. API Endpoint
POST requests to /ask with JSON body:
{
"question": "What is my total sales?",
"want_plot": false
}
The system returns the generated SQL query and the query result in JSON.
Supported Sample Questions
What is my total sales?
Returns the sum of total sales across all products and dates.
Calculate the RoAS (Return on Ad Spend).
Calculates ROAS = total ad sales divided by total ad spend.
Which product had the highest CPC (Cost Per Click)?
Identifies the product with the highest cost per click (ad_spend / clicks).
Total sales of item 4
Returns the total sales filtered for product/item ID 4.
CPC for a given date and item_id
Send a POST request with a question:
curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d '{"question
Example response:
{
"question": "What is my total sales?",
"sql_generated": "SELECT SUM(total_sales) AS total_sales FROM total_sales;",
"result": [{"total_sales": 1004904.56}]
}
For questions or issues, contact the development team.
This README can be enhanced with deployment instructions or environment variable
configurations, depending on your hosting setup.
⁂
Example Usage
Notes
The LLM prompt is designed to generate SQL queries using SUM and other aggregates
Whenever the query asks for aggregated metrics.
Filtering by product/item IDs is handled by detecting item references in questions or by
prompt instructions.
The system safely handles division by zero for CPC and ROAS calculations using SQL
NULLIF.
You can extend the system by adding more datasets and improving natural language
understanding of the LLM.
Contact
