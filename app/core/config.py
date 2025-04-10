from pydantic_settings import BaseSettings, SettingsConfigDict


class CustomBaseSettings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        case_sensitive=True, extra="ignore", env_file=".env"
    )


settings = CustomBaseSettings()
