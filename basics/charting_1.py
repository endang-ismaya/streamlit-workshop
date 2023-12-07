import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Displaying Chart")

df = pd.read_csv("data/sample.csv")

# streamlit line plot
st.line_chart(df, x="year", y=["col1", "col2", "col3"])

# streamlit area chart
st.area_chart(df, x="year", y=["col1", "col2", "col3"])

# streamlit bar chart
st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

# streamlit map
geo_df = pd.read_csv("data/sample_map.csv")
st.map(geo_df)

# Matplotlib
st.divider()

fig, ax = plt.subplots()

ax.plot(df.year, df.col1)
ax.set_title("My Figure Title")
ax.set_xlabel("Year")
ax.set_ylabel("Values")
fig.autofmt_xdate()

st.pyplot(fig)
