""" Define all the environment variables here"""
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file(s)
load_dotenv()

# Define the environment variables
ENV = os.getenv('ENV', 'N/A')
DEBUG = os.getenv('DEBUG', 'N/A')
PORT = os.getenv('PORT', 'N/A')
HOST = os.getenv('HOST', 'N/A')
GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID', 'N/A')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE', 'N/A')
STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME', 'N/A')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'N/A')
OPENAI_API_SECRET = os.getenv('OPENAI_API_SECRET', 'N/A')
OPENAI_API_URL = os.getenv('OPENAI_API_URL', 'N/A')
OPENAI_API_VERSION = os.getenv('OPENAI_API_VERSION', 'N/A')
