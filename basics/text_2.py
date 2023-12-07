import streamlit as st

# title
st.title(body="App Title")

# header
st.header(body="Main Header")

# subheader
st.subheader(body="Sub Header")

# markdown
st.markdown(body="**This is a markdown** _text_")
st.markdown(body="### Header 3 here")

# caption
st.caption(body="caption is here too")

# code block
st.code(
    body="""
import pandas as pd
import openpyxl

def read_excel(my_file):
    pd.read_csv(my_file)
""",
    language="python",
)

# preformatted text
st.text("pre-formatted text")

# latex
st.latex("Big O(n^2)")

# divider
st.divider()

# write any
st.write("Footer and Header")
st.write("<b>Big Bold</b>", unsafe_allow_html=True)
