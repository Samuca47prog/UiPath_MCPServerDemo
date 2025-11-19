# tests/conftest.py
import os
from dotenv import load_dotenv

# Load the project .env once for all tests
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
