import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.sidebar.title('stream 入門1')

st.write('interactive widgets')

#if st.checkbox('show image') :
#	img = Image.open('sample.png')
#	st.image(img, caption='picture', use_column_width=True)

#option = st.selectbox(
#    '好きな数字を教えて', 
#    list(range(1,11))
#)
#'好きな数字は', option, 'です'

text = st.sidebar.text_input("あなたの好きな趣味は")
condition = st.sidebar.slider("調子は", 0, 100, 50)

"趣味は", text, 'です'
"コンディション: ",condition, "です"
