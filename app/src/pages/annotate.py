import streamlit as st
from src.config.config_labelstudio import LABEL_CONFIG, LABEL_INTERFACES, LABEL_USER
from streamlit_labelstudio import st_labelstudio

from ..utils import Page


class Annotate(Page):
    def write(self):

        task = {
            "id": 0,
            "data": {"image": st.session_state["presigned_url"]},
            "predictions": [
                {
                    "result": [
                        {
                            "id": "result1",
                            "source": "$image",
                            "type": "rectanglelabels",
                            "from_name": "label",
                            "to_name": "image",
                            "image_rotation": 0,
                            "value": {
                                "x": 1.0,
                                "y": 1.0,
                                "width": 1.0,
                                "height": 1.0,
                                "rectanglelabels": ["Band"],
                            },
                        }
                    ],
                    "model_version": "test",
                    "task": 0,
                }
            ],
        }
        annotation_results = st_labelstudio(
            LABEL_CONFIG, LABEL_INTERFACES, LABEL_USER, task
        )
        st.session_state["annotation_results"] = annotation_results
