import os


class Settings:
    APP_NAME = "PROJECT API"
    APP_VERSION = "1.0.0"

    HOST = "0.0.0.0"
    PORT = int(os.getenv("PORT", "8000"))
    DEBUG = False

    HF_TOKEN = os.getenv("HF_TOKEN", "")
    HF_BASE_URL = "https://router.huggingface.co/v1"

    AI_MODEL = "openai/gpt-oss-120b"


settings = Settings()
