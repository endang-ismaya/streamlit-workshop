import streamlit as st
import streamlit.components.v1 as cmp

text = "State Y"
if "click" not in st.session_state:
    st.session_state.click = False
else:
    if st.session_state.click is False:
        text = "State X"
        st.session_state.click = True
    else:
        text = "State Y"
        st.session_state.click = False

st.button(text)

cmp.iframe(
    "https://lottie.host/embed/6c269c7a-ebef-49f4-abc8-45f0c1b3b4f5/ffcE5lr9vg.json"
)
cmp.iframe(
    "https://lottie.host/embed/5d574a16-6a23-4176-a97b-364233d32193/VYVGfZu1Bn.json"
)

st.image("data/images/Animation - 1703839876319.gif")
