import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

SERPAPI_KEY = os.getenv("SERPAPI_KEY")  # Put API key here if not using .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Put API key here if not using .env
GOOGLE_SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")  # Path to your service account JSON file
