import streamlit as st


def get_code_input():

    default_code = """for i in range(10):
                        print(i)"""

    code = st.text_area("Write the code here to cheak out complexity", value = default_code,
        height = 280)
    
    return code

