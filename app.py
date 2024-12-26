"""
# My first app
Here's our first attempt at using data to create a table:
"""


import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

#judul program pertama pake title di streamlit

st.streamlit.title("kalkulator kecepatan")
# Menampilkan gambar lokal
st.title("welcome to our app")
st.image("Calculator.jpg", caption="picture", use_column_width=True)

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)