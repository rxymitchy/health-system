import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'dev-key-123'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///health.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False