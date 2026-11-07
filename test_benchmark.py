
import pytest
from engine.benchmarking import benchmark_algorithm


def test_benchmark_returns_expected_fields():

    result = benchmark_algorithm(algorithm = sorted, data = [5, 2, 4, 1, 3], repetitions = 3)
    expected_fields = {"algorithm", "repetitions", "times", "average_time", "minimum_time", "maximum_time", "median_time", "result"}

    assert expected_fields.issubset(result.keys())


def test_benchmark_result_is_correct():

    result = benchmark_algorithm(algorithm = sorted, data = [5, 2, 4, 1, 3], repetitions = 3)
    assert result["result"] == [1, 2, 3, 4, 5]


def test_benchmark_repetition_count():
    result = benchmark_algorithm(algorithm = sorted, data = [3, 1, 2], repetitions = 5)

    assert result["repetitions"] == 5
    assert len(result["times"]) == 5


def test_benchmark_times_are_non_negative():

    result = benchmark_algorithm(algorithm = sorted, data = [4, 2, 1, 3], repetition = 3)
    assert all(time >= 0 for time in result["times"])


def test_benchmark_statistics():
    result = benchmark_algorithm( algorithm = sorted, data = [5, 4, 3, 2, 1], repetitions = 5)

    times = result["times"]

    assert result["minimum_time"] == min(times)
    assert result["maximum_time"] == max(times)
    assert result["average_time"] == pytest.approx( sum(times) / len(times))
    assert result["median_time"] == pytest.approx( sorted(times)[len(times) // 2])


def test_benchmark_rejects_invalid_repetitions():

    with pytest.raises(ValueError):
        benchmark_algorithm(sorted, [3, 2, 1], repetitions=0)

    with pytest.raises(ValueError):
        benchmark_algorithm(sorted, [3, 2, 1], repetitions=-1)


def test_benchmark_rejects_non_callable_algorithm():

    with pytest.raises((TypeError, ValueError)):
        benchmark_algorithm( algorithm = 123, data = [3, 2, 1], repetitions = 3)
