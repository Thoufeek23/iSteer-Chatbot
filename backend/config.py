from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TARGET_URL = os.getenv("TARGET_URL")
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
