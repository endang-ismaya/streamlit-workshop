import streamlit as st
import time
from datetime import time as dtime

# checkbox
chk_1 = st.checkbox("Learn during weekend?", value=True)

if chk_1:
    st.write("Great!, You keep learning to be success")
else:
    st.write("Unfornately, we need you more and more...")


def on_change():
    st.write(f"Status: {st.session_state.chk_2}")


chk_state = st.checkbox("State", value=True, on_change=on_change, key="chk_2")

# radio button
radio1 = st.radio(
    "In which country do you live?",
    options=("Indonesia", "Malaysia", "India", "Singapure", "Thailand"),
)
# print(radio1)


# button
def on_click():
    print("on click event!")


btn1 = st.button("Click Me!", on_click=on_click)

# selection
select1 = st.selectbox(
    "What's your favorite programming language?",
    options=("JavaScript", "Python", "Java", "C++", "PHP", "C#"),
)
# print(select1)

# multiple selection
mselect1 = st.multiselect(
    "What's is your fav IDE?",
    options=("VSCode", "PyCharm", "Spyder", "Vim", "Idle", "Notepad++"),
)
# print(mselect1)

# uploading file
st.header("Uploading Files")
st.divider()

img1 = st.file_uploader("Please upload an image", type=["png", "jpeg", "jpg"])
if img1 is not None:
    st.image(img1)

images = st.file_uploader(
    "Please upload images", type=["png", "jpeg", "jpg"], accept_multiple_files=True
)
if images is not None:
    for img in images:
        st.image(img, width=200)

# slider
s_val = st.slider(label="VSWR Threshold", min_value=0, max_value=100, step=5)
st.write(s_val)

# text area
ta1 = st.text_area(label="Description")

# text input
ti1 = st.text_input(label="First Name:")
ti2 = st.text_input(label="Last Name")
dt1 = st.date_input(label="Enter your registration date: ")
tm1 = st.time_input(label="Time to vanish?", value=dtime(0, 0, 0))


def time_converter(value: str):
    m, s, ms = value.split(":")
    t_s = int(m) * 60 + int(s) + int(ms) / 1000
    return t_s


# progress bar
bar1 = st.progress(10)

if str(tm1) == "00:00:00":
    st.write("No Action")
else:
    sec = time_converter(str(tm1))
    bar1.progress(0)

    percentage = sec / 100
    prog_state = st.empty()

    for i in range(1, 101):
        bar1.progress(i)
        prog_state.write(f"{i} %")
        time.sleep(percentage)
