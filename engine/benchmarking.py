"""file will measure how long an algorithm takes to execute, repeat the measurement multiple times, and calculate statistics"""


import time
import statistics

def benchmark_algorithm(algorithm, data, repetitions = 9):
    if not callable(algorithm):
        raise TypeError("Algorithm must be a callable function")
    
    if not isinstance(repetitions, int) or isinstance(repetitions, bool) or repetitions < 1:
        raise ValueError("Repetitions must be a positive integer")
    
    times = []
    result = None
    
    for i in range(repetitions):
        start_time = time.perf_counter()
        
        result = algorithm(data)
        end_time = time.perf_counter()
        
        elapsed_time = end_time - start_time
        times.append(elapsed_time)
        
    return {
        "algorithm": algorithm.__name__,
        "repetitions": repetitions,
        "times": times,
        "average_time": statistics.mean(times),
        "minimum_time": min(times),
        "maximum_time": max(times),
        "median_time": statistics.median(times),
        "result": result,
    }
    
    
