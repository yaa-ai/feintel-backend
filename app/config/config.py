import secrets
from typing import List
from pydantic import AnyHttpUrl, EmailStr
from pydantic_settings import BaseSettings
import os 


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # SECRET_KEY for JWT token generation
    # Calling secrets.token_urlsafe will generate a new secret everytime
    # the server restarts, which can be quite annoying when developing, where
    # a stable SECRET_KEY is prefered.

    # SECRET_KEY: str = secrets.token_urlsafe(32)
    SECRET_KEY: str = os.environ.get("JWT_SECRET_KEY",'')
    

# MONGO_USER=
# MONGO_PASSWORD=
    # database configurations
    MONGO_HOST: str=os.environ.get("MONGO_HOST")
    MONGO_PORT: int=os.environ.get("MONGO_PORT")
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_DB: str=os.environ.get("MONGO_DB")

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str

    FIRST_SUPERUSER: EmailStr=os.environ.get("FIRST_SUPERUSER")
    FIRST_SUPERUSER_PASSWORD: str=os.environ.get("FIRST_SUPERUSER_PASSWORD")

    # SSO ID and Secrets
    GOOGLE_CLIENT_ID: str = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: str = os.environ.get("GOOGLE_CLIENT_SECRET")
    FACEBOOK_CLIENT_ID: str = "None"
    FACEBOOK_CLIENT_SECRET: str = "None"
    SSO_CALLBACK_HOSTNAME: str = os.environ.get("SSO_CALLBACK_HOSTNAME")
    SSO_LOGIN_CALLBACK_URL: str = os.environ.get("http://localhost:5173/sso-login-callback")

    class Config:
        env_file = ".env.dev"
        # orm_mode = True


settings = Settings()
