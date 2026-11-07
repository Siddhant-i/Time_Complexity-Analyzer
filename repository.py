
from database.connection import get_connection
from database.models import create_tables


def save_benchmark_result(result):

    required_fields = ["algorithm","category","input_size","repetitions","average_time","median_time","minimum_time","maximum_time","correct"]
    missing = [i for i in required_fields if i not in result]

    if missing:
        raise ValueError(f"Missing benchmark fields: {', '.join(missing)}")

    create_tables()

    query = """
    INSERT INTO benchmark_results ( algorithm, category, input_size, distribution, repetitions, 
        average_time, median_time, minimum_time, maximum_time, correct, target)
        
    VALUES (
        %(algorithm)s,
        %(category)s,
        %(input_size)s,
        %(distribution)s,
        %(repetitions)s,
        %(average_time)s,
        %(median_time)s,
        %(minimum_time)s,
        %(maximum_time)s,
        %(correct)s,
        %(target)s
    )
    RETURNING id;
    """

    values = {
        "algorithm": result["algorithm"],
        "category": result["category"],
        "input_size": result["input_size"],
        "distribution": result.get("distribution"),
        "repetitions": result["repetitions"],
        "average_time": result["average_time"],
        "median_time": result["median_time"],
        "minimum_time": result["minimum_time"],
        "maximum_time": result["maximum_time"],
        "correct": result["correct"],
        "target": result.get("target"),
    }

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            saved_row = cursor.fetchone()

    return saved_row["id"]


def get_benchmark_results(limit=100):
    """Retrieve the most recent benchmark results."""

    if (not isinstance(limit, int) or isinstance(limit, bool) or limit < 1):
        raise ValueError("Limit must be a positive integer ")

    create_tables()

    query = """
    SELECT *
    FROM benchmark_results
    ORDER BY created_at DESC, id DESC
    LIMIT %s;
    """

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (limit,))
            return cursor.fetchall()


if __name__ == "__main__":
    try:
        results = get_benchmark_results()

        print(f"Retrieved {len(results)} benchmark records.")

        for result in results:
            print(
                result["id"],
                result["algorithm"],
                result["input_size"],
                result["average_time"],
            )

    except Exception as error:
        print("Could not retrieve benchmark results.")
        print(error)
