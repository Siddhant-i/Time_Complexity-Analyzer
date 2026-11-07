# Time Complexity Analyzer

## About the Project

Time Complexity Analyzer is a Python-based application developed using Streamlit. It helps users understand how algorithms work, analyze their time complexity, and compare their performance.

The project consists of two main modules: Algorithm Analyzer and Code Analyzer. The Algorithm Analyzer allows users to run and compare different algorithms, while the Code Analyzer examines Python code and estimates its time complexity.

## Features

### Algorithm Analyzer
- Supports different categories of algorithms.
- Includes Sorting, Searching algorithms.
- Allows users to select multiple algorithms for comparison.
- Measures execution time for different input sizes.
- Supports random, sorted, and reverse-sorted inputs.
- Checks the correctness of algorithm outputs.
- Displays performance comparisons through graphs.

### Code Analyzer
- Allows users to enter Python code for analysis.
- Detects loops and nested loops.
- Detects sorting operations.
- Estimates the time complexity of the given code.
- Displays analysis results with explanations.

## How It Works

### Algorithm Analyzer

1. Select an algorithm category.
2. Choose the algorithms you want to compare.
3. Set the input size and other benchmarking parameters.
4. Select the input distribution.
5. Run the benchmark.
6. The application executes the selected algorithms and measures their execution time.
7. The results are displayed through performance graphs and comparisons.

### Code Analyzer

1. Enter or paste Python code into the analyzer.
2. The application examines the code using Python's AST module.
3. It checks for loops, nested loops, recursion, and sorting operations.
4. Based on the detected patterns, it estimates the possible time complexity.
5. The analysis results and explanations are displayed.

## Technologies Used

- Python
- Streamlit
- NumPy
- Pandas
- Matplotlib
  
## Project Structure

```text
Time-Complexity-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── algorithms/
    |-- sorting.py
│   ├── searching.py
├── engine/
│   ├── analyzer.py
│   └── benchmark.py
│
└── other project files
```

## Installation and Execution

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Open the project directory**

```bash
cd Time-Complexity-Analyzer
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

For Windows:

```bash
venv\Scripts\activate
```

**5. Install the required libraries**

```bash
pip install -r requirements.txt
```

**6. Run the application**

```bash
streamlit run app.py
```

The application will open in your default web browser.

## Time Complexity

The project focuses on commonly used time complexities:

| Complexity | Description |
|---|---|
| O(1) | Constant Time |
| O(log n) | Logarithmic Time |
| O(n) | Linear Time |
| O(n log n) | Linearithmic Time |
| O(n²) | Quadratic Time |
| O(2ⁿ) | Exponential Time |

## Future Improvements

- Add more algorithms and algorithm categories.
- Improve time and space complexity analysis.
- Improve code analysis and complexity estimation.
- Provide suggestions for optimizing inefficient code.
- Add support for more programming languages.
- Improve performance graphs and reporting features.

## Author

**Siddhant Raghuvanshi**
