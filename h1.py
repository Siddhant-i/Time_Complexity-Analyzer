
import streamlit as st

st.title("My dashboard")

st.write("Real time starts coming here ")
x = st.slider("pick a number - ", 1, 100)

st.write("You picked", x)