import os 
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPEN_AI_KEY=os.getenv('OPEN_AI_KEY')
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
    AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
    VECTOR_DB_PATH = 'vector_db'
    