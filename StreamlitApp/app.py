import streamlit as st
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title='OpenCV', layout='wide',
                   initial_sidebar_state='collapsed')

st.title("OpenCV Application")

up_file = st.sidebar.file_uploader("upload file")
options = st.sidebar.multiselect(
    "Select options", ['original', 'black and white'])
checkbox = st.checkbox("Show Histogram")


if up_file is not None:
    img = up_file.read()
    decoded = cv.imdecode(np.frombuffer(img, np.uint8), -1)
    decoded = cv.cvtColor(decoded, cv.COLOR_RGB2BGR)
    for op in options:
        if op == 'original':
            st.image(decoded, caption=str(decoded.shape[:2]))
        if op == 'black and white':

            bw = cv.cvtColor(decoded, cv.COLOR_BGR2GRAY)
            st.image(bw, caption=str(bw.shape))
            plt.hist(bw.ravel(), 256, [0, 255])
            st.pyplot()
else:
    st.warning("No file uploaded")
