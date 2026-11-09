
import os
from pathlib import Path

import psycopg
import streamlit as st
from dotenv import load_dotenv
from psycopg.rows import dict_row

Base_direct = Path(__file__).resolve().parent.parent
load_dotenv(Base_direct / ".env")


def get_setting(key):
    """Read settings from Streamlit Secrets or local .env"""

    try:
        value = st.secrets.get(key)
        if value:
            return value
    except Exception:
        pass

    return os.getenv(key)


def get_connection():
    """Connect to PostgreSQL and return the connection"""

    required_settings = [
        "DB_HOST",
        "DB_PORT",
        "DB_NAME",
        "DB_USER",
        "DB_PASSWORD"
    ]

    settings = {
        key: get_setting(key)
        for key in required_settings
    }

    missing = [
        key for key, value in settings.items()
        if not value
    ]

    if missing:
        raise RuntimeError(
            f"Missing database settings: {', '.join(missing)}"
        )

    connection = psycopg.connect(
        host=settings["DB_HOST"],
        port=int(settings["DB_PORT"]),
        dbname=settings["DB_NAME"],
        user=settings["DB_USER"],
        password=settings["DB_PASSWORD"],
        row_factory=dict_row,
        sslmode="require"
    )

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
