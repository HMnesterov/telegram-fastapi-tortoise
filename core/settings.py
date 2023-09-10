from pydantic import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    DB_CONNECTION: str
    DB_MIGRATE_PATH: str
    WEBHOOK_URL: str
    #REDIS_CONNECTION: str
    #ACCESS_TOKEN_EXPIRE_MINUTES: int
    #SECRET_KEY: str
    #ALGORITM: str

    class Config:
        env_file = "env/.env"
        env_file_encoding = "utf-8"


settings = Settings()
