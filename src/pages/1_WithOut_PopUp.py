from utils import long_duration_function
import streamlit as st

st.title("Streamlit Application WithOut Popup")

user_name = st.text_input("Enter your name", "Ivan")
favorite_emoji = st.selectbox("Select your favorite emoji", ["😀", "😂", "😍", "😎", "🤔"])

if st.button("Submit"):
    result = long_duration_function(user_name, favorite_emoji)
    st.success(result, icon="🎉")

code = """
from utils import long_duration_function
import streamlit as st

st.title("Streamlit Application WithOut Popup")

user_name = st.text_input("Enter your name", "Ivan")
favorite_emoji = st.selectbox(
    "Select your favorite emoji", ["😀", "😂", "😍", "😎", "🤔"]
)

if st.button("Submit"):
    result = long_duration_function(user_name, favorite_emoji)
    st.success(result, icon="🎉")
"""
with st.expander("Code of this page"):
    st.code(code.strip(), language="python", line_numbers=False)
