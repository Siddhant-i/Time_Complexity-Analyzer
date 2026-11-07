

import matplotlib.pyplot as plt

def plot_execution_time(results):
    
    if not results:
        raise ValueError("Result cannot be empty")
    
    algorithms = [item["algorithm"] for item in results]
    times = [item["average_time"] * 1000 for item in results]
    
    fig, ax = plt.subplots(figsize =(10, 5))
    
    ax.bar(algorithms, times)
    ax.set_title("Algorithm Execution Time comparison Graph")
    ax.set_xlabel("Algorithm")
    ax.set_ylabel("Average Execution Time (milliseconds)")
    
    ax.tick_params(axis = "x", labelrotation = 30)
    fig.tight_layout()
    
    return fig



def plot_input_size_vs_time(results):

    if not results:
        raise ValueError("Results cannot be empty")

    grouped_results = {}

    for item in results:
        algorithm = item["algorithm"]
        size = item["input_size"]
        execution_time = item["average_time"] * 1000

        grouped_results.setdefault(algorithm, []).append((size, execution_time))

    fig, ax = plt.subplots(figsize = (10, 5))

    for algorithm, measurements in grouped_results.items():
        measurements.sort(key=lambda point: point[0])

        sizes = [point[0] for point in measurements]
        times = [point[1] for point in measurements]

        ax.plot(sizes, times, marker = "o", label = algorithm)
 
    ax.set_title("Input Size vs Execution Time")
    ax.set_xlabel("Input Size")
    ax.set_ylabel("Average Execution Time (milliseconds)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.tight_layout()

    return fig


def plot_timing_distribution(result):

    times = result.get("times", [])

    if not times:
        raise ValueError("The result must contain individual timing measurements")

    times_ms = [elapsed * 1000 for elapsed in times]
    fig, ax = plt.subplots(figsize = (8, 4))
    
    run_numbers = list(range(1, len(times_ms) + 1))
    ax.plot(run_numbers, times_ms, marker = "o")

    ax.set_title(f"Timing Variation: {result['algorithm']}")
    ax.set_xlabel("Run Number")
    ax.set_ylabel("Execution Time (milliseconds)")
    ax.set_xticks(run_numbers)
    ax.grid(True, alpha = 0.3)

    fig.tight_layout()

    return fig

