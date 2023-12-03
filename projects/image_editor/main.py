import streamlit as st
from PIL import Image, ImageFilter

st.markdown("<h1 style='text-align: center;'>Image Editor</h1>", unsafe_allow_html=True)
st.divider()

# main
img = st.file_uploader(label="Upload your image", type=["png", "jpeg", "jpg"])

img_place = st.empty()
info = st.empty()
size = st.empty()
mode = st.empty()
format_ = st.empty()

if img:
    working_img = Image.open(img)

    # show image
    img_place.image(img)

    info.markdown(
        "<h2 style='text-align: center;'>Information</h2>", unsafe_allow_html=True
    )
    size.markdown(f"<h6>Size: {working_img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {working_img.mode}</h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6>Format: {working_img.format}</h6>", unsafe_allow_html=True)

    # Resizing
    st.markdown("<h2 style='text-align: center;'>Resizing</h2>", unsafe_allow_html=True)
    width = st.number_input("Width", value=working_img.width)
    height = st.number_input("Height", value=working_img.height)

    # Rotating
    st.markdown("<h2 style='text-align: center;'>Rotating</h2>", unsafe_allow_html=True)
    degree = st.number_input("Degree", min_value=0, max_value=360, step=10)

    # Filters
    st.markdown(
        "<h2 style='text-align: center;'>Filtering</h2>", unsafe_allow_html=True
    )
    filter_ = st.selectbox(
        "Filters", options=["None", "BLUR", "DETAIL", "EMBOSS", "SMOOTH", "SHARPEN"]
    )

    # Button
    btn = st.button("Submit", type="primary")

    if btn:
        edited_img = working_img.resize((width, height)).rotate(degree)
        if filter_ != "None":
            if filter_ == "BLUR":
                edited_img = edited_img.filter(ImageFilter.BLUR)
            elif filter_ == "DETAIL":
                edited_img = edited_img.filter(ImageFilter.DETAIL)
            elif filter_ == "EMBOSS":
                edited_img = edited_img.filter(ImageFilter.EMBOSS)
            elif filter_ == "SMOOTH":
                edited_img = edited_img.filter(ImageFilter.SMOOTH)
            elif filter_ == "SHARPEN":
                edited_img = edited_img.filter(ImageFilter.SHARPEN)

        st.image(edited_img)
