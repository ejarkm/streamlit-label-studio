import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import boto3
from datetime import datetime


from ..utils import Page


from src.config.config_aws import (
    AWS_BUCKET,
    AWS_REGION_NAME,
    AWS_ENDPOINT_URL,
    AWS_ACCESS_KEY,
    AWS_SECRET_KEY,
)


class Upload(Page):
    def __init__(self):
        pass

    def write(self):
        st.title("Western Blot")
        uploaded_image = st.file_uploader(
            "Upload an image", type=["jpg", "png", "jpeg"]
        )
        if (
            uploaded_image is not None
            or st.session_state.get("image", None) is not None
        ):
            if uploaded_image is None:
                uploaded_image = st.session_state.get("uploaded_image")
            image = Image.open(uploaded_image)
            file_extension = uploaded_image.type.split("/")[1]
            image.save(f"tmp.{file_extension}")

            st.image(image)

            client = boto3.client(
                "s3",
                aws_access_key_id=AWS_ACCESS_KEY,
                aws_secret_access_key=AWS_SECRET_KEY,
                region_name=AWS_REGION_NAME,
                endpoint_url=AWS_ENDPOINT_URL,
            )

            datetime_now = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f"{datetime_now}_{uploaded_image.name}"
            client.upload_file(f"tmp.{file_extension}", AWS_BUCKET, file_name)

            presigned_url = client.generate_presigned_url(
                "get_object",
                Params={"Bucket": AWS_BUCKET, "Key": file_name},
                ExpiresIn=10000,
            )

            st.session_state["uploaded_image"] = uploaded_image
            st.session_state["image"] = image
            st.session_state["presigned_url"] = presigned_url
