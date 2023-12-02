import streamlit as st
import requests
from bs4 import BeautifulSoup

# page info
st.set_page_config(page_title="Web Scraper", page_icon="🔍", layout="centered")

st.markdown("<h1 style='text-align: center;'>Web Scraper</h1>", unsafe_allow_html=True)

term = None
with st.form(key="f_search"):
    term = st.text_input(label="Enter your keyword")
    st.form_submit_button(label="Search")

placeholder = st.empty()
if term:
    req = requests.get(f"https://unsplash.com/s/photos/{term}")
    soup = BeautifulSoup(req.content)
    rows = soup.find_all("div", class_="ripi6")

    col1, col2 = placeholder.columns(2)
    for idx, row in enumerate(rows):
        figures = row.find_all("div", class_="MorZF")

        # MorZF

        for index, figure in enumerate(figures):
            # print(figure)
            # print("\n\n")

            img = figure.find("img")
            img_1 = img["srcset"].split("?")[0]

            if index % 2 == 0:
                col2.image(img_1)
                # btn_download = col2.button(
                #     label="Download", key=f"{idx}_{index}", type="primary"
                # )
                # if btn_download:
                #     st.info("Download OK")
            else:
                col1.image(img_1)
                # btn_download = col1.button(label="Download", key=f"{idx}_{index}")
                # if btn_download:
                #     st.info("Download OK")
