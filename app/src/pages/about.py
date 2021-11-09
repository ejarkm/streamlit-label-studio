import streamlit as st

from ..utils import Page


class About(Page):
    def write(self):
        var = "worked?"
        st.title("Page 2")
        st.session_state[__name__] = var
