import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('stream 入門1')

st.write('interactive widgets')

left_column, right_column = st.columns(2)

button =left_column.button("右コラムに表示")

if button:
    right_column.write("ここは右カラムです")


expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")
expander.write("問い合わせ内容を書く2")


#text = st.text_input("あなたの好きな趣味は")
#condition = st.slider("調子は", 0, 100, 50)

#"趣味は", text, 'です'
#"コンディション: ",condition, "です"
