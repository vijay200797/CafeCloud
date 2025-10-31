from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    api_url: str = os.getenv('API_URL')
    database_url: str = os.getenv('DATABASE_URL')
    rabbit_mq_server: str = os.getenv('RABBIT_MQ_SERVER')
    rabbit_mq_port: str = os.getenv('RABBIT_MQ_PORT')
    rabbit_mq_user: str = os.getenv('RABBIT_MQ_USER')
    rabbit_mq_password: str = os.getenv('RABBIT_MQ_PASSWORD')

settings = Settings()