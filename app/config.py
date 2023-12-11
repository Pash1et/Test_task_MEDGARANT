from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DOCS_URL: str = Field(default="/docs")

    DB_HOST: str = Field(default="localhost")
    DB_PORT: int = Field(default=5432)
    DB_USER: str = Field(default="postgres")
    DB_PASS: str = Field(default="postgres")
    DB_NAME: str = Field(default="postgres")

    @property
    def DATABASE_URL(self):
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    WORK_DAY_START: int = Field(default=9)
    WORK_DAY_END: int = Field(default=21)
    WORK_DAY_WINDOW: int = Field(default=30)


settings = Settings()
