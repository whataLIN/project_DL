import streamlit as st
from widget.sidebar import sidebar

with st.sidebar:
    sidebar()

st.write("나는 야만인이다")