import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")

API_ENV = os.environ.get("API_ENV", "staging")
IS_DEPLOYED = API_ENV in ["production", "staging"]
