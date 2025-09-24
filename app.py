import streamlit as st
from utils import square_number

st.title("Mini CI/CD Demo App 🚀")

num = st.number_input("Enter a number:", value=2)
if st.button("Square it"):
    result = square_number(num)
    st.success(f"The square of {num} is {result}")
