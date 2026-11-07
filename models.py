
from database.connection import get_connection
from models import create_tables
def create_tables():

    query = """
    CREATE TABLE IF NOT EXISTS benchmark_results (
        id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        algorithm VARCHAR(100) NOT NULL,
        category VARCHAR(50) NOT NULL,
        input_size INTEGER NOT NULL CHECK (input_size >= 0),
        distribution VARCHAR(30),
        repetitions INTEGER NOT NULL CHECK (repetitions > 0),
        average_time DOUBLE PRECISION NOT NULL,
        median_time DOUBLE PRECISION NOT NULL,
        minimum_time DOUBLE PRECISION NOT NULL,
        maximum_time DOUBLE PRECISION NOT NULL,
        correct BOOLEAN NOT NULL,
        target BIGINT,
        created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)

    print("Benchmark results table is ready.")

if __name__ == "__main__":
    create_tables()
