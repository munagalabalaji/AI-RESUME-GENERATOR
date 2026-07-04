import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-1298471203984710293847')
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # Database
    DB_DIR = os.path.join(BASE_DIR, 'database')
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR, exist_ok=True)
    db_url = os.environ.get('DATABASE_URL')
    if db_url:
        if db_url.startswith('sqlite:///'):
            db_path = db_url[10:]
            if not os.path.isabs(db_path):
                db_url = f"sqlite:///{os.path.join(BASE_DIR, db_path)}"
        SQLALCHEMY_DATABASE_URI = db_url
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(DB_DIR, 'resume_generator.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Uploads
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size
    
    # API Keys
    GEMINI_API_KEY = os.environ.get('Q.Ab8RN6ICRelOdsNHEyRXo8Cy5Psn0syZ-9Vtj12fAimxNuQ8pw')
    
    # Admin settings
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@resumegen.com')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')
