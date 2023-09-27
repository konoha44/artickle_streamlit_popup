import streamlit as st
from constants import CODE_FOR_PAGE_1 as code
from utils import long_duration_function, check_if_button_clicked

st.title("Streamlit Application WithOut Popup")

user_name = st.text_input("Enter your name", "Ivan", key="user_name")
favorite_emoji = st.selectbox(
    "Select your favorite emoji", ["😀", "😂", "😍", "😎", "🤔"], key="favorite_emoji"
)

# if button has alreade been clicked then st.session_state.get("submit") is not None
# if button has not been clicked then user has to click on it to define st.session_state.get("submit")
if check_if_button_clicked():
    result = long_duration_function(user_name, favorite_emoji)
    st.success(result, icon="🎉")
    del st.session_state["counter"], st.session_state["computed"]


with st.expander("Code of this page"):
    st.code(code.strip(), language="python", line_numbers=False)
