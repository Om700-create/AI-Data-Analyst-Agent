from pathlib import Path
import os
from dotenv import load_dotenv

# Load .env if present
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
if ENV_PATH.exists():
    load_dotenv(ENV_PATH)

# SQLite DB path
DB_PATH = BASE_DIR / "data" / "analytics.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

# Hugging Face LLM config
HF_API_TOKEN = os.getenv("HF_API_TOKEN", "YOUR_HF_API_TOKEN_HERE")
HF_MODEL_ID = os.getenv("HF_MODEL_ID", "mistralai/Mistral-7B-Instruct-v0.2")

# Basic safety for missing token
if HF_API_TOKEN == "YOUR_HF_API_TOKEN_HERE":
    print("⚠️ Warning: Please set HF_API_TOKEN in a .env file or environment variable.")
