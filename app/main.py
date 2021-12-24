import streamlit as st

from src.pages import PAGES


def main():
    """Main function of the App"""
    st.set_page_config(layout="wide")
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]()
    page.write()


if __name__ == "__main__":
    main()
