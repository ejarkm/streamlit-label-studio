from datetime import datetime
import streamlit as st
from streamlit_labelstudio import st_labelstudio
import boto3
import pandas as pd
from PIL import Image
import io
import time



from src.config.config_labelstudio import (
    LABEL_CONFIG,
    LABEL_USER,
    LABEL_INTERFACES,
)
from src.config.config_aws import (
    AWS_BUCKET,
    AWS_REGION_NAME,
    AWS_ENDPOINT_URL,
    AWS_ACCESS_KEY,
    AWS_SECRET_KEY,
)

datetime_now = datetime.now().strftime("%Y%m%d%H%M%S")

st.set_page_config(layout="wide")
st.title("Western Blot")
st.session_state[__name__] = "test"
print(st.session_state)


client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION_NAME,
    endpoint_url=AWS_ENDPOINT_URL,
)


uploaded_image = st.file_uploader("Upload an image", type=None)

if uploaded_image is not None or st.session_state.get("image", None) is not None:
    if uploaded_image is None:
        uploaded_image = st.session_state.get("uploaded_image")
    
    st.session_state["uploaded_image"] = uploaded_image
    image = Image.open(uploaded_image)
    width, height = image.size
    image = image.resize((width, height))
    file_extension = uploaded_image.type.split("/")[1]
    Image.Image.save(image, f"tmp.{file_extension}")

    file_name = f"{datetime_now}_{uploaded_image.name}"
    client.upload_file(f"tmp.{file_extension}", AWS_BUCKET, file_name)

    response = client.generate_presigned_url(
        "get_object",
        Params={"Bucket": AWS_BUCKET, "Key": file_name},
        ExpiresIn=100,
    )

    task = {
        "completions": [],
        "predictions": [],
        "id": 1,
        "data": {"image": response},
    }

    results_raw = st_labelstudio(LABEL_CONFIG, LABEL_INTERFACES, LABEL_USER, task)

    if results_raw is not None:
        areas = [v for k, v in results_raw['areas'].items()]

        results = []
        for a in areas:
            results.append({'id':a['id'], 'x':a['x'], 'y':a['y'], 'width':a['width'], 'height':a['height'], 'label':a['results'][0]['value']['rectanglelabels'][0]})

        print(st.table(results))
