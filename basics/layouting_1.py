import streamlit as st
import pandas as pd

# Sidebar
with st.sidebar:
    st.write("Text in the sidebar")


# Columns
col1, col2, col3 = st.columns(spec=3)
col1.write("Text in Column-1")

slider = col2.slider("Choose a number", min_value=0, max_value=50)

df = pd.read_csv("data/sample.csv", dtype="int")
col3.write("DataFrame")
col3.dataframe(df)


# Tabs
tab1, tab2 = st.tabs(["Line Plot", "Bar Plot"])
with tab1:
    tab1.write("line plot")
    tab1.line_chart(df, x="year", y=["col1", "col2", "col3"])

with tab2:
    tab2.write("Bar Plot")
    tab2.bar_chart(df, x="year", y=["col1", "col2", "col3"])

# Expander (Collapsible Element)
with st.expander("Click to expand"):
    st.markdown("## What is Lorem Ipsum?")
    st.markdown(
        """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
    when an unknown printer took a galley of type and scrambled it to make a type specimen book.
    It has survived not only five centuries, but also the leap into electronic typesetting,
    remaining essentially unchanged.
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
    and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """
    )

# Container
with st.container():
    st.write("This is inside the container")

st.write("This is outside the container")
