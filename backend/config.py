from pydantic import BaseModel
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Reading App API"
    API_V1_STR: str = "/api/v1"
    
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/reading_app"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()