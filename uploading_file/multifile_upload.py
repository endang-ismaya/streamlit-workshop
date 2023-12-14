import os
import streamlit as st
from PIL import Image
from streamlit.runtime.uploaded_file_manager import UploadedFile


def load_image(imagefile):
    img = Image.open(imagefile)
    return img


def save_uploaded_file(uploaded_file: UploadedFile):
    print(uploaded_file.name)

    with open(os.path.join("data", uploaded_file.name), mode="wb") as f:
        f.write(uploaded_file.getbuffer())

    return st.success(f"Saved file in data: {uploaded_file.name}")


def main():
    st.title("Multiple File Upload")

    uploadedfiles = st.file_uploader(
        label="Upload multiple images",
        type=["png", "jpeg", "jpg"],
        accept_multiple_files=True,
    )

    if uploadedfiles:
        for file in uploadedfiles:
            save_uploaded_file(file)


if __name__ == "__main__":
    main()
