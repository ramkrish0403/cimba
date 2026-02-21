from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "cimba"
    debug: bool = False
    log_level: str = "INFO"
    host: str = "0.0.0.0"
    port: int = 8000

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
