import streamlit as st
import cv2


from ..utils import Page

def show_clicked(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.putText(main_img, text='Clicked', org=(x,y),
            fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0),
            thickness=2, lineType=cv2.LINE_AA)


class Home(Page):
    def write(self):
        var = "worked"
        st.title("Page 1")
        st.session_state[__name__] = var

        main_img = cv2.imread("/home/ejar/Documents/GitEjar/WesternBlot/app/src/images/perspective.jpg")
        
        ox, oy = 50, 50
        
        dot = cv2.imread("/home/ejar/Documents/GitEjar/WesternBlot/app/src/images/red_dot.png")

        h, w, _ = dot.shape

        # print(cv2.EVENT_LBUTTONDOWN)

        # main_img[oy:oy+h, ox:ox+w] = dot
        # st.image(main_img, caption="Perspective", use_column_width=True)

        # cv2.setMouseCallback('main_img',show_clicked)

        # TODO: Add drawable canvas
        # TODO: Add the contour detection for automatic rotation
        # TODO: Add Scale
        # TODO: Add Automatic boxes detection
        # TODO: Add Protein table
