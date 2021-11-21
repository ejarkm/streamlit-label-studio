import cv2
import pandas as pd
import streamlit as st
from numpy import greater
from PIL import Image
from streamlit_drawable_canvas import st_canvas

from ..utils import Page


class Home(Page):
    def write(self):
        var = "worked"
        st.title("Western Blot")
        st.session_state[__name__] = var

        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

        image = Image.open(uploaded_image)
        st.write(image)

        st.image(image)

        st.button("Blot")


        
