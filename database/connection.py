

import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row

Base_direct = Path(__file__).resolve().parent.parent
load_dotenv(Base_direct / ".env")


def get_connection():
    """Connect to PostgreSQL and return the connection"""

    required_settings = [ "DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD"]

    missing = [i for i in required_settings if not os.getenv(i)]

    if missing:
        raise RuntimeError(f"Missing database settings: {', '.join(missing)} \n Check your project's .env file.")

    connection = psycopg.connect(host = os.getenv("DB_HOST") , port = int(os.getenv("DB_PORT")),
        dbname = os.getenv("DB_NAME"), user = os.getenv("DB_USER"), password = os.getenv("DB_PASSWORD"), row_factory = dict_row)
    
    return connection


if __name__ == "__main__":
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT version();")
                result = cursor.fetchone()
                print("PostgreSQL connection successful!")
                print(result["version"])

    except Exception as error:
        print("Database connection failed")
        print(error)
