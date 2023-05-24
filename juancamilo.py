import json
import requests
import streamlit as st
from PIL import Image
import gspread
import pandas as pd





def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


image = Image.open('ruby.png')
image2 = Image.open('tabla.png')

st.title(':red[TOWN TALES]')
st.header('Por Juan Camilo y Jahir')

st.image(image, caption='ruby main character')

st.image(image2, caption = 'esquema general del proyecto')



