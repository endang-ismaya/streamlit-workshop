import streamlit as st
import pandas as pd

# utils
import base64
import time

timestr = time.strftime("%Y%m%d-%H%M%S")


def text_downloader(raw_text):
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = f"new_txt_{timestr}.txt"

    href = (
        f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">'
        + "Download here!</a>"
    )
    st.markdown(href, unsafe_allow_html=True)


def csv_downloader(data):
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()
    new_filename = f"new_txt_{timestr}.csv"

    href = (
        f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">'
        + "Download here!</a>"
    )
    st.markdown(href, unsafe_allow_html=True)


class FileDownloader:
    """docstring for FileDownloader"""

    def __init__(self, data, fname, fext) -> None:
        self.data = data
        self.fname = fname
        self.fext = fext

    def download(self):
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename = f"{self.fname}_{timestr}.{self.fext}"

        href = (
            f'<a href="data:file/{self.fext};base64,{b64}" download="{new_filename}">'
            + "Download here!</a>"
        )
        st.markdown(href, unsafe_allow_html=True)


def main():
    """Main point of app"""

    mnu = ["Home", "CSV", "About"]
    choice = st.sidebar.selectbox("Menu", mnu)

    match choice:
        case "Home":
            st.subheader("Home")
            my_text = st.text_area("Your message...")

            if st.button("Save"):
                # text_downloader(my_text)
                fd = FileDownloader(data=my_text, fname="message", fext="txt")
                fd.download()

        case "CSV":
            st.subheader("Data Frame from CSV")
            df = pd.read_csv(r"data/tips.csv")
            st.dataframe(df)

            if st.button("Save"):
                # csv_downloader(df)
                fd = FileDownloader(data=df.to_csv(), fname="data", fext="csv")
                fd.download()

        case "About":
            st.subheader("About")


if __name__ == "__main__":
    main()
