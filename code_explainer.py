

def explain_result(result):

    complexity = result["complexity"]

    explanations = {
        "O(1)": "Constant - The algorithm/code execution time is independent of its input size even if it grows",
        "O(n)": "Linear - AS, the input size increases so, the execution time of an algorithm inc in a direct proportion",

        "O(n^2)": "Quadratic - Two loops inside each other\n The execution time is square of its input size",
        "O(log n)": "Logarithmic - The code reduces the amount of work at each step",

        "O(n log n)": "Linearithmic - The execution time grows slightly faster than linear time because the algorithm performs log n work for each of the n elements",
        "O(n^3)": "Three nested loops can make the code take a lot of time",
        
        # O(n^2) -> \(O(n^2)\)
        "O(2^n)": "The work can grow very quickly as the input increases",
        "O(n!)": "The code will try every possible order of the combinations, which takes a lot of time",

        "Cannot analyze": "The code has a syntax error and could not be checked its Time Complexity",
        "Needs further ananlysis" : "The analyzer could not confidently identify the time complexity. The code may contain a more complicated loop or recursive pattern.",
        
        "O(n * m)": "Nested loops use different input sizes. The total work depends on both n and m.",
    }

    return {
        "complexity": complexity,
        "simple_explanation": explanations.get(complexity, "The time complexity could not be explained clearly")
    }
