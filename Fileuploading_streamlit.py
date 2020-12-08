import streamlit as st

uploaded_file = st.file_uploader("Choose an image", ["jpg","jpeg","png"]) #image uploader
st.write('Or')
use_default_image = st.checkbox('Use default maze')