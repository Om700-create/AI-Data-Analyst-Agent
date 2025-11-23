# 📊 AI Data Analyst Agent

Ask questions in natural language → Get SQL → Run analysis → View charts → Read business insights

An end-to-end, production-ready AI Agent that turns natural-language business questions into executable SQL queries — then automatically visualizes results and explains insights like a senior data analyst.

This project demonstrates LLM-powered analytics automation, the kind top 1% Data Scientists showcase on their resumes.

🖼️ Project Preview

Below is how the application looks after deployment:

🚀 Key Features
🔹 Natural Language → SQL Conversion

Ask questions like:

“What is the total revenue by region?”
The agent generates valid SQL automatically.

🔹 Automated Query Execution

SQL is run on a structured SQLite analytics database.

🔹 Auto-Generated Visualizations

It creates bar charts, line charts, or statistical summaries based on the result.

🔹 Business Insights (LLM-generated)

The AI explains the results in clear business language.

🔹 Clean FastAPI Backend

Modular, production-ready structure.

🔹 Stylish Frontend UI

Simple, clean interface anyone can use.

📁 Project Structure
ai-data-analyst-agent/
│  requirements.txt
│  README.md
│
├─ data/
│   sample_sales.csv
│   analytics.db
│   init_db.py
│
├─ app/
│   main.py
│   config.py
│   db.py
│   schemas.py
│
│   ├─ services/
│   │    nl2sql.py
│   │    analysis.py
│   │
│   └─ static/
│        plots/
│        index.html

⚙️ Installation & Setup
1️⃣ Clone the project
git clone https://github.com/yourname/ai-data-analyst-agent.git
cd ai-data-analyst-agent

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Create database
python data/init_db.py


This generates analytics.db populated with sample sales data.

4️⃣ Add your HuggingFace API Token

Create a .env file:

HF_API_TOKEN=your_huggingface_token
HF_MODEL_ID=mistralai/Mistral-7B-Instruct-v0.2

5️⃣ Run the app
uvicorn app.main:app --reload

6️⃣ Open in browser

API Docs → http://127.0.0.1:8000/docs

Web UI → http://127.0.0.1:8000/static/index.html

🧠 How It Works (Pipeline)
1. User asks a natural-language question

Example:

“Show total revenue by product”

2. LLM converts question → SQL

Example output:

SELECT product, SUM(revenue) AS total_revenue
FROM sales
GROUP BY product;

3. App executes SQL on SQLite database

Pandas reads the result into a DataFrame.

4. A chart is automatically generated

Saved to static/plots/.

5. LLM generates business insights

You get bullet-point explanations tailored to the question and dataset.

💡 Example Output

Input Question:

“What is the total revenue by region?”

Generated SQL:

SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region


Chart:
(Shown in UI — auto-created from results)

Business Insights:

The North region generated the highest revenue.

East shows strong growth with consistent sales.

West lags behind significantly, indicating low market penetration.

🎯 Resume-Ready Project Description

Use this in your resume:

AI Data Analyst Agent — End-to-End Project
Built an AI-powered Data Analyst Agent that converts natural-language questions into SQL, executes them on a structured analytics DB, and returns tables, charts, and narrative insights. Integrated HuggingFace LLMs for NL→SQL and insight generation. Developed with FastAPI, SQLAlchemy, Pandas, and a clean HTML UI for business users.

🔧 Tech Stack

Backend: FastAPI, SQLAlchemy, Pandas

LLM: HuggingFace Inference API (Mistral 7B Instruct)

Database: SQLite

Frontend: HTML/CSS, JS

Visualization: Matplotlib

Deployment-ready: Modular structure & static file support

🤝 Contributing

Pull requests, improvements, and UI enhancements are welcome.

📜 License

MIT