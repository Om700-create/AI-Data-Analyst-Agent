# 📊 AI Data Analyst Agent
📊 AI Data Analyst Agent

An end-to-end AI-powered Data Analyst that converts natural-language questions into SQL, executes them on a database, visualizes the results, and explains insights like a senior data analyst.

This project is designed as a top-tier portfolio project for Data Science, AI, and Business Analytics roles.

🖥️ Live UI Preview (Light Theme)

🌙 Dark Theme UI (Premium Look)

🎞️ GIF Demo (Storyboard Style for GitHub Profile)

This simulated GIF-style storyboard shows how the agent processes data step-by-step.





![My Custom UI](assets/my_screenshot<img width="607" height="614" alt="Screenshot 2025-11-24 005224" src="https://github.com/user-attachments/assets/390d5c94-b06a-4a53-babb-c4c04cc0bb44" />
.png)




![My Screenshot](my_image.<img width="916" height="617" alt="Screenshot 2025-11-24 005257" src="https://github.com/user-attachments/assets/1f927216-7243-465f-a082-ee036e7d44f0" />
png)

🚀 Features

🔹 Natural Language → SQL using LLM

🔹 Automatic SQL execution on SQLite

🔹 Auto-generated charts (bar, line)

🔹 AI-generated business insights

🔹 Modern UI (light + dark themes)

🔹 Clean FastAPI backend

🔹 Modular structure ready for deployment

📁 Folder Structure
ai-data-analyst-agent/
│  README.md
│  requirements.txt
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

⚙️ Installation
1️⃣ Clone
git clone https://github.com/yourname/ai-data-analyst-agent.git
cd ai-data-analyst-agent

2️⃣ Install
pip install -r requirements.txt

3️⃣ Setup Database
python data/init_db.py

4️⃣ Add HuggingFace API Keys

Create .env:

HF_API_TOKEN=your_token_here
HF_MODEL_ID=mistralai/Mistral-7B-Instruct-v0.2

5️⃣ Run Server
uvicorn app.main:app --reload

6️⃣ Access

UI → http://127.0.0.1:8000/static/index.html

API Docs → http://127.0.0.1:8000/docs

🧠 How It Works

User asks a question

LLM converts text → SQL

SQL runs on the database

DataFrame → chart auto-generated

LLM writes business insights

📈 Example Output

Question:

What is the total revenue by region?

Generated SQL:

SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region;


Insights:

North is the highest-performing region

East shows consistent revenue

West underperforms

South is moderate

🎯 Resume-Ready Description

AI Data Analyst Agent — End-to-End AI Project
Built an AI agent that interprets natural language queries, generates SQL, visualizes analytics, and produces business insights using LLMs. Developed with FastAPI, SQLAlchemy, Pandas, Matplotlib, and HuggingFace models. Includes a modern UI and full automation pipeline.

🛠️ Tech Stack

FastAPI

SQLite + SQLAlchemy

HuggingFace LLM

Pandas

Matplotlib

HTML/CSS/JS

🤝 Contributing

PRs are welcome!
You can improve UI, add models, or enhance charts.

📜 License (MIT)
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
