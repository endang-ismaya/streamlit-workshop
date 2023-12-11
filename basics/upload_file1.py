import os
import streamlit as st


st.title("Uploading a file into internal folder")
st.caption("folder data")

uploaded_file = st.file_uploader(label="Upload a KGET log file", type=["log"])
btn_save = st.button(label="Save file")

if btn_save:
    if uploaded_file is not None:
        with st.spinner(text="uploading..."):
            with open(os.path.join("./data", uploaded_file.name), mode="wb") as f:
                f.write(uploaded_file.getbuffer())

        st.success(body="File upload successfully")
    else:
        st.warning("Please upload a valid log file.")
