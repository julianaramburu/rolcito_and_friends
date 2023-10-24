import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)