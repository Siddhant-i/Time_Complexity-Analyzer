

import pytest

from algorithms.sorting import(bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort)

from algorithms.searching import(linear_search, binary_search)

from algorithms.array import (find_maximum , reverse_array, two_sum, remove_duplicates_sorted)

from algorithms.mathematical import gcd, is_prime

from algorithms.string_matching import naive_string_match

from engine.validator import validate_sorting, validate_searching


Sorting_algorithms = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort]


@pytest.mark.parametrize("algorithm", Sorting_algorithms)
@pytest.mark.parametrize("data, expected", [
        ([5, 2, 8, 1], [1, 2, 5, 8]),
        ([], []),
        ([4], [4]),
        ([3, 3, 1, 1], [1, 1, 3, 3]),
        ([-2, 5, 0, -1], [-2, -1, 0, 5]), ],)

def test_sorting_algorithms(algorithm, data, expected):
    original = data.copy()
    result = algorithm(data)

    assert result == expected
    assert data == original 
    assert validate_sorting(data, result)

def test_linear_search_found():
    assert linear_search([10, 20, 30], 20) == 1

def test_linear_search_not_found():
    assert linear_search([10, 20, 30], 99) == -1

def test_binary_search_found():
    assert binary_search([10, 20, 30, 40], 30) == 2

def test_binary_search_not_found():
    assert binary_search([10, 20, 30], 99) == -1

def test_search_validation():
    data = [10, 20, 30]

    assert validate_searching(data, 20, 1)
    assert validate_searching(data, 99, -1)
    assert not validate_searching(data, 20, -1)

def test_find_maximum():
    assert find_maximum([4, 9, 2, 7]) == 9

def test_find_maximum_empty():
    with pytest.raises(ValueError):
        find_maximum([])

def test_reverse_array():
    assert reverse_array([1, 2, 3]) == [3, 2, 1]

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_not_found():
    assert two_sum([1, 2, 3], 20) is None

def test_remove_duplicates_sorted():
    assert remove_duplicates_sorted([1, 1, 2, 3, 3]) == [1, 2, 3]

def test_gcd():
    assert gcd(12, 18) == 6


@pytest.mark.parametrize( "number, expected",
    [(2, True), (9, False), (1, False), (17, True), (-5, False)] )
def test_is_prime(number, expected):
    assert is_prime(number) == expected

def test_naive_string_match():
    assert naive_string_match("aaaa", "aa") == [0, 1, 2]
