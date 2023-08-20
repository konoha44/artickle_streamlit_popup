from time import sleep

import streamlit as st
from streamlit.components.v1 import html


def long_duration_function(name: str, emoji: str) -> str:
    progress_text = "# Really Complicated Operation is in progress. Please wait..."
    my_bar = st.progress(0, text=progress_text)
    for i in range(1, 11):
        sleep(1)
        my_bar.progress(i * 10, text=progress_text)
    return f" Hello {name}, your favorite emoji is {emoji}!"


def read_file(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as file:
        return file.read().strip()


def pop_up_window_click(activate: bool = True) -> None:
    """Pop up window overlaping to disable user interaction"""
    if activate:
        html(read_file("./static/activate_popup_js_injection.html"))

    # deactivate and clean url
    else:
        html(read_file("./static/deactivate_popup_js_injection.html"))
        html(read_file("./static/clean_url_js_injection.html"))


def pop_up_window() -> str:
    """Read PopUp window overlaping to disable user interaction"""
    return read_file("./static/popup_window.html")
