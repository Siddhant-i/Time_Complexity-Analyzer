
import streamlit as st
import subprocess
import sys

from code_analyzer.code_input import get_code_input
from code_analyzer.error_checker import check_errors
from code_analyzer.loop_detector import detect_loops
from code_analyzer.condition_checker import check_conditions
from code_analyzer.complexity_analyzer import analyze_complexity
from code_analyzer.code_explainer import explain_result

st.set_page_config(page_title = "Time complexity Code analyzer", layout = "wide")

st.title("Time complexity Code analyzer")
st.write("Write code, run it, and check its time complexity")

code = get_code_input()
col1, col2 = st.columns(2)

with col1:
    run = st.button("Run Code", use_container_width = True)

with col2:
    analyze = st.button("Check Code Complexity", use_container_width = True)

if run:
    try:
        result = subprocess.run(
            [sys.executable, "-c", code],
            capture_output = True, text = True, timeout = 4)

        if result.returncode == 0:
            st.subheader("Code Result")
            st.code(result.stdout or "No output", language = "text")
        else:
            st.error("Problem in your code")
            st.code(result.stderr, language = "text")

    except subprocess.TimeoutExpired:
        st.error("Code took too long Timeout break!")

    except Exception as error:
        st.error(str(error))

if analyze:
    errors = check_errors(code)

    if errors:
        st.subheader("Problems in Your Code")
        for i in errors:
            st.error(
                f"Line {i['line']}: {i['message']}"
            )
    else:
        st.success("No problems found by the basic checks.")

    loops = detect_loops(code)
    result = analyze_complexity(code)
    explanation = explain_result(result)

    st.subheader("Analysis Results")

    col1, col2, col3= st.columns(3)

    col1.metric("Loops Found", len(loops))
    col3.metric("Time Complexity", result["complexity"])

    st.subheader("Loops Found")

    if loops:
        for i in loops:
            st.write(f"Line {i['line']}: {i['type']} loop")
    else:
        st.write("No loops found.")

    st.subheader("Time consumption Issues ?")
    st.write(explanation["simple_explanation"])
