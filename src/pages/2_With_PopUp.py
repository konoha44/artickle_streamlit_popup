from utils import long_duration_function, pop_up_window, pop_up_window_click
import streamlit as st

st.title("Streamlit Application WithOut Popup")

user_name = st.text_input("Enter your name", "Ivan")
favorite_emoji = st.selectbox("Select your favorite emoji", ["😀", "😂", "😍", "😎", "🤔"])

if st.button("Submit"):
    placeholder = st.empty()
    placeholder.write(pop_up_window(), unsafe_allow_html=True)
    pop_up_window_click(activate=True)

    result = long_duration_function(user_name, favorite_emoji)

    pop_up_window_click(activate=False)
    placeholder.empty()

    st.success(result, icon="🎉")

code = """"""
with st.expander("Code of this page"):
    st.code(code.strip(), language="python", line_numbers=False)
