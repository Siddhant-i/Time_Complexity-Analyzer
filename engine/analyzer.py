
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


from algorithms.searching import linear_search, binary_search
from algorithms.sorting import (bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort)

from engine.input_generator import generate_input
from engine.validator import validate_sorting, validate_searching
from engine.benchmarking import benchmark_algorithm

Sorting_algorithm = {"Bubble Sort": bubble_sort, "Selection Sort": selection_sort, "Insertion Sort": insertion_sort, "Merge Sort": merge_sort, "Quick Sort": quick_sort}
Searching_algorithm = {"Linear Search": linear_search,"Binary Search": binary_search}

def analyze_sorting_algorithm(algorithm, size, distribution = "random", repetitions= 9 , seed=42):
    data = generate_input(size = size, distribution = distribution, seed = seed)
    
    result = algorithm(data)
    
    if not validate_sorting(data, result):
        raise ValueError(f"{algorithm.__name__} produced an incorrect sorting result")
        
    benchmark = benchmark_algorithm( algorithm = algorithm, data = data, repetitions = repetitions)
    
    if not validate_sorting(data, benchmark["result"]):
        raise ValueError(f"{algorithm.__name__} produced an incorrect benchmark result")
        
    return {
        "algorithm": algorithm.__name__,
        "category": "Sorting",
        "input_size": size,
        "distribution": distribution,
        "correct": True,
        "repetitions": repetitions,
        "average_time": benchmark["average_time"],
        "minimum_time": benchmark["minimum_time"],
        "maximum_time": benchmark["maximum_time"],
        "median_time": benchmark["median_time"],
    }

def analyze_searching_algorithm(algorithm, data, target, repetitions):
    if algorithm is binary_search and data != sorted(data):
        raise ValueError("Binary Search requires input sorted in ascending order")
        
    result = algorithm(data, target)

    if not validate_searching(data, target, result):
        raise ValueError(f"{algorithm.__name__} produced an incorrect search result")
        
    def search_operation(arr):
        return algorithm(arr, target)
    
    benchmark = benchmark_algorithm( algorithm = search_operation, data = data, repetitions = repetitions)
    
    if not validate_searching(data, target, benchmark["result"]):
        raise ValueError(f"{algorithm.__name__} produced an incorrect benchmark result")
    
    return {
        "algorithm": algorithm.__name__,
        "category": "Searching",
        "input_size": len(data),
        "target": target,
        "correct": True,
        "repetitions": repetitions,
        "average_time": benchmark["average_time"],
        "minimum_time": benchmark["minimum_time"],
        "maximum_time": benchmark["maximum_time"],
        "median_time": benchmark["median_time"],
    }

def analyze_multiple_sorting_algorithms(algorithms, size, distribution = "random", repetitions =  9, seed = 42):

    results = []
    for algorithm in algorithms:
        result = analyze_sorting_algorithm( algorithm = algorithm, size = size, distribution = distribution, repetitions = repetitions, seed = seed)
        results.append(result)

    return results



