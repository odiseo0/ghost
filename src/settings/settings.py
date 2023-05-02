from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    OPENAI_API_KEY: SecretStr


settings = Settings()
