from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    APP_TITLE: str = "Bilim Al"
    APP_VERSION: str = "2.0.0"

    # Email настройки
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME", "")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD", "")
    MAIL_FROM: str = os.getenv("MAIL_USERNAME", "")
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_PORT: int = 587

settings = Settings()