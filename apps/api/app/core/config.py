from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="API_", env_file=".env", extra="ignore")

    env: str = "development"
    host: str = "0.0.0.0"
    port: int = 8000
    database_url: str = Field(default="postgresql+psycopg://privacy:privacy@localhost:5432/privacy_platform")
    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "please-change-me"
    s3_endpoint: str = "http://localhost:9000"
    s3_bucket: str = "evidence"
    s3_access_key: str = "minio"
    s3_secret_key: str = "minio123"


settings = Settings()

