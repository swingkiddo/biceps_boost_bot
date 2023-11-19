import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

HOST_PORT=os.getenv("HOST_PORT")
DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")

conn = psycopg2.connect(
    host="localhost",
    port=HOST_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cur = conn.cursor()
