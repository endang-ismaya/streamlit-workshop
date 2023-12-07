import streamlit as st
import pandas as pd

st.title("Displaying Input")

# Button
st.markdown("### Button")
btn_primary = st.button(label="Primary", type="primary")
btn_secondary = st.button(label="Secondary", type="secondary")

if btn_primary:
    st.markdown("<p style='color: red;'>Hello from Primary</p>", unsafe_allow_html=True)
if btn_secondary:
    st.markdown(
        "<p style='color: grey;'>Hello from Secondary</p>", unsafe_allow_html=True
    )

st.divider()

# Checkbox
st.markdown("### CheckBox")
chk = st.checkbox(label="Remember Us")

if chk:
    st.write("I will always remember you!")

st.divider()

# Radio Buttons
st.markdown("### Radio Buttons")
df = pd.read_csv("data/sample.csv")

radio = st.radio("Choose a column", options=df.columns[1:], index=0, horizontal=False)
st.write(f"You choose '{radio}'")
st.line_chart(df, x="year", y=[radio])

st.divider()

# SelectBox
st.markdown("### SelectBox")
select = st.selectbox(label="Choose a column", options=df.columns[1:], index=0)

st.divider()

# Multi Select
st.markdown("### MultiSelect")
m_select = st.multiselect(
    "Choose as many columns as you want",
    options=df.columns[1:],
    default=["col1"],
    max_selections=3,
)
st.write(m_select)
st.divider()

# Slider
st.markdown("### Slider")
slider = st.slider(label="Pick a number", min_value=0, max_value=100, value=30, step=10)
st.write(slider)
st.divider()

# Text Input
st.markdown("### Text Input")
txt_name = st.text_input(label="What's your name?", placeholder="John Doe")
st.write(txt_name)
st.divider()

# Number
st.markdown("### Number Input")
txt_num = st.number_input(label="Pick a number", min_value=0, max_value=100)
st.write(f"You pick {txt_num}")
st.divider()

# Text Area
st.markdown("### Text Area")
txt_area = st.text_area(label="Description", height=250)
st.divider()
