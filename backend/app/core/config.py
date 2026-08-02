from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # -----------------------
    # Application
    # -----------------------
    APP_NAME: str
    APP_VERSION: str
    APP_ENV: str

    # -----------------------
    # API Keys
    # -----------------------
    GROQ_API_KEY: str = ""
    TAVILY_API_KEY: str = ""

    # -----------------------
    # Database
    # -----------------------
    DATABASE_URL: str

    # -----------------------
    # Vector Database
    # -----------------------
    CHROMA_DB_PATH: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()