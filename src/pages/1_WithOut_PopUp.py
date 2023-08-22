from utils import long_duration_function, on_click_1_page, warm_up_rerun
import streamlit as st

st.title("Streamlit Application WithOut Popup")

user_name = st.text_input("Enter your name", "Ivan")
favorite_emoji = st.selectbox("Select your favorite emoji", ["😀", "😂", "😍", "😎", "🤔"])

if st.button(
    "Submit",
    type="primary",
    use_container_width=True,
    key="submit",
    on_click=on_click_1_page,
):
    result = long_duration_function(user_name, favorite_emoji)
    st.success(result, icon="🎉")
    del st.session_state["counter"]

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
