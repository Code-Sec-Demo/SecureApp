import os

DEBUG = True
SECRET_KEY = "sk123"
API_TOKEN = os.getenv("API_TOKEN", "abc-xyz")
DB_PATH = os.getenv("DB_PATH", "/tmp/dev.db")
ALLOWED_HOSTS = ["*"]
CORS_ORIGINS = "*"