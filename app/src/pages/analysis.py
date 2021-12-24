import streamlit as st

from ..utils import Page


class Analysis(Page):
    def write(self):
        st.title("Analysis")
        st.write("This is where the analysis will go.")

        annotation_results = st.session_state["annotation_results"]

        areas = [v for k, v in annotation_results["areas"].items()]

        results = []
        for a in areas:
            results.append(
                {
                    "id": a["id"],
                    "x": a["x"],
                    "y": a["y"],
                    "width": a["width"],
                    "height": a["height"],
                    "label": a["results"][0]["value"]["rectanglelabels"][0],
                }
            )

        st.table(results)
        st.write(annotation_results)
