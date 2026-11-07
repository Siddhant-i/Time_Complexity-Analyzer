
import pytest

from database.models import create_tables
from database.repository import(save_benchmark_result, get_benchmark_results)


@pytest.fixture
def sample_result():
    """Create sample benchmark data for testing."""

    return {
        "algorithm": "Test Sort",
        "category": "Sorting",
        "input_size": 100,
        "distribution": "random",
        "repetitions": 3,
        "average_time": 0.001,
        "median_time": 0.0009,
        "minimum_time": 0.0008,
        "maximum_time": 0.0013,
        "correct": True,
        "target": None,
    }


def test_create_tables():
    create_tables()


def test_save_benchmark_result(sample_result):
    saved_id = save_benchmark_result(sample_result)

    assert saved_id is not None
    assert isinstance(saved_id, int)


def test_get_benchmark_results():
    results = get_benchmark_results(limit=5)

    assert isinstance(results, list)


def test_get_benchmark_results_invalid_limit():
    with pytest.raises(ValueError):
        get_benchmark_results(limit=0)

    with pytest.raises(ValueError):
        get_benchmark_results(limit=-1)
