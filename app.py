
import streamlit as st
import pandas as pd


from database.models import create_tables
from database.repository import ( save_benchmark_result, get_benchmark_results)

from engine.analyzer import (Sorting_algorithm, Searching_algorithm, analyze_sorting_algorithm, analyze_searching_algorithm, analyze_multiple_sorting_algorithms)
from engine.input_generator import generate_input
from visualization.charts import (plot_execution_time, plot_input_size_vs_time)



st.set_page_config(page_title = " Time Complexity Analyzer " , layout = "wide")

try:
    create_tables()
except Exception as error:
    st.error(f"Database initialization failed: {error}")
    st.stop()

st.title(" Time Complexity Analyzer ")
st.write(f"Benchmark algorithms, validate their correctness and compare their measured execution times ")

st.sidebar.header("Benchmark Settings")

category = st.sidebar.selectbox(" Algorithm Category ",["Sorting", "Searching"])

if category == "Sorting":
    algorithm_options = list(Sorting_algorithm.keys())
else:
    algorithm_options = list(Searching_algorithm.keys())



selected_algorithms = st.sidebar.multiselect("Select Algorithms", algorithm_options, default=algorithm_options[:2])

min_size = st.sidebar.number_input(" Minimum Input Size", min_value = 1, max_value = 10000, value = 100, step = 100)
max_size = st.sidebar.number_input("Maximum Input Size", min_value = 1, max_value = 10000, value = 1000, step = 100)

number_of_sizes = st.sidebar.slider("Number of Input Sizes", min_value = 2, max_value = 10, value = 4)
distribution = st.sidebar.selectbox("Input Distribution", ["random", "sorted", "reverse"])

repetitions = st.sidebar.slider("Repetitions", min_value = 1,max_value = 15,value =  9)

seed = st.sidebar.number_input("Random Seed", min_value = 0, max_value = 100000, value = 42)

run_benchmark = st.sidebar.button("Run Benchmark", type = "primary")

if run_benchmark:
    if not selected_algorithms:
        st.error("Please select at least one algorithm ")

    elif min_size > max_size:
        st.error( "Minimum input size cannot exceed maximum input size")

    else:
        sizes = sorted(set(int(size) for size in pd.Series( range(number_of_sizes)).map(
                    lambda i: round( min_size + i * (max_size - min_size) / (number_of_sizes - 1)))))

        results = []
        progress = st.progress(0)
        total_runs = len(selected_algorithms) * len(sizes)
        completed = 0

        try:
            for i in sizes:

                if category == "Sorting":
                    algorithms = [ Sorting_algorithm[name] for name in selected_algorithms]
                    size_results = analyze_multiple_sorting_algorithms (algorithms = algorithms, size = i, distribution = distribution, repetitions = repetitions, seed = int(seed))
                    results.extend(size_results)
                    
                else:
                    data = generate_input(size = i, distribution = distribution, seed = int(seed))

                    if "Binary Search" in selected_algorithms:
                        data.sort()

                    target = data[len(data) // 2] if data else 0

                    for i in selected_algorithms:
                        algorithm = Searching_algorithm[i]

                        result = analyze_searching_algorithm( algorithm = algorithm, data = data, target = target, repetitions = repetitions)
                        result["distribution"] = distribution
                        results.append(result)
                
            
                completed += len(selected_algorithms)
                progress.progress( min(completed / total_runs, 1.0))

        except Exception as error:
            st.error(f"Benchmark failed: {error}")
            st.stop()
        try:
            saved_ids = []

            for result in results:
                saved_id = save_benchmark_result(result)
                saved_ids.append(saved_id)

            st.success(
                f"Benchmark completed! Saved {len(saved_ids)} "
                "results to PostgreSQL."
            )

        except Exception as error:
            st.error(f"Could not save benchmark results: {error}")

        results_df = pd.DataFrame(results)
        st.subheader("Benchmark Results")
        st.success("Benchmark completed successfully!")     

        display_columns = ["algorithm", "input_size", "correct", "average_time", "median_time", "minimum_time", "maximum_time"]

        st.dataframe(results_df[display_columns] , use_container_width = True)
        st.subheader("Average Execution Time")

        chart_results = results_df.to_dict(orient = "records")
        st.pyplot(plot_execution_time(chart_results),use_container_width = True)

        st.subheader("Input Size vs Execution Time")
        st.pyplot(plot_input_size_vs_time(chart_results), use_container_width = True)

        csv_data = results_df.to_csv(index = False).encode("utf-8")
        st.download_button(label = "Download Results as CSV", data = csv_data, file_name = "benchmark_results.csv", mime = "text/csv")

else:
    st.info("Choose your benchmark settings in the sidebar and click Run Benchmark to begin")

    st.subheader("What this dashboard provides")
    col1, col2, col3 = st.columns(3)

    col1.metric("Algorithm Categories", "2")
    col2.metric("Sorting Algorithms", len(Sorting_algorithm))
    col3.metric("Searching Algorithms", len(Searching_algorithm))

st.divider()
st.header("Saved Benchmark History")

try:
    history = get_benchmark_results(limit=100)

    if history:
        history_df = pd.DataFrame(history)
        
        st.dataframe(history_df, use_container_width = True, hide_index = True)
        csv_data = history_df.to_csv(index=False).encode("utf-8")

        st.download_button(label = "Download Saved History as CSV", data = csv_data, file_name = "benchmark_history.csv",mime = "text/csv")
    else:
        st.info("No saved benchmark results yet.")

except Exception as error:
    st.error(f"Could not load benchmark history: {error}")
