import streamlit as st
import time

# progress
st.header("st.progress")
st.caption("Display a progress bar")

my_bar = st.progress(0)


def run_progress():
    for i in range(1, 121, 20):
        time.sleep(0.5)
        i = min(i, 100)
        my_bar.progress(i)


# spinner
with st.spinner("Something is processing..."):
    run_progress()

st.button(label="Run Again", disabled=True)
