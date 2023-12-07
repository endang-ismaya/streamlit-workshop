import streamlit as st
import pandas as pd

st.title("Displaying Data")

df = pd.read_csv("data/sample.csv", dtype="int")

st.write("DataFrame")
st.dataframe(df)
st.write(df)

st.write("Table")
st.table(df)

st.write("Metric")
st.metric(label="Metric label", value=900, delta=-20, delta_color="normal")
