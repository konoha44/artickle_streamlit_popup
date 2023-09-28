import streamlit as st
from constants import CODE_FOR_PAGE_2 as code
from utils import (
    long_duration_function,
    pop_up_window,
    pop_up_window_click,
    on_click_2_page,
)

st.title("Streamlit Application With Popup")

user_name = st.text_input("Enter your name", "Ivan")
favorite_emoji = st.selectbox("Select your favorite emoji", ["😀", "😂", "😍", "😎", "🤔"])


if st.button(
    "Submit",
    type="primary",
    disabled=st.session_state.get("disable", False),
    on_click=on_click_2_page,
    help="If button is disabled, please push button 'Re-run' or change input data.",
    use_container_width=True,
    key="submit",
):
    # create st.empty() container
    placeholder = st.empty()

    # insert part with popup initialization button for our HTML page to container
    placeholder.write(pop_up_window(), unsafe_allow_html=True)

    # activate pop overlay by clicking on button
    pop_up_window_click(activate=True)

    # Run long-duration function
    result = long_duration_function(user_name, favorite_emoji)

    # Deactivate pop overlay by clicking on the close button
    pop_up_window_click(activate=False)

    # Clean st.empty() container
    placeholder.empty()

    st.success(result, icon="🎉")

    del st.session_state["counter"], st.session_state["disable"]

    if st.button("Re-run"):
        st.experimental_rerun()

with st.expander("Code of this page"):
    st.code(code.strip(), language="python", line_numbers=False)
