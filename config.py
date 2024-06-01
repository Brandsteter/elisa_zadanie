#Access to global variables
import os 
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER', 'default_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'default_password')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'default_db')

FILE_PATH = 'configClear_v2.json'