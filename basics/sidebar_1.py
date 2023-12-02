import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

chart_opt = st.sidebar.radio("Select any graph", options=("Line", "Bar", "H-Bar"))

# create x axis
line_x = np.linspace(0, 10, 100)
bar_x = np.array([1, 2, 3, 4, 5])

if chart_opt.casefold() == "line".casefold():
    st.markdown(
        "<h1 style='text-align: center;'>Line Chart</h1>", unsafe_allow_html=True
    )
    fig = plt.figure()
    plt.style.use(
        "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle"
    )

    plt.plot(line_x, np.sin(line_x))
    plt.plot(line_x, np.cos(line_x), "--")
    st.write(fig)
elif chart_opt.casefold() == "bar".casefold():
    st.markdown(
        "<h1 style='text-align: center;'>Bar Chart</h1>", unsafe_allow_html=True
    )
    fig = plt.figure()
    plt.style.use(
        "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle"
    )

    plt.bar(bar_x, bar_x * 10)
    st.write(fig)
elif chart_opt.casefold() == "h-bar".casefold():
    st.markdown(
        "<h1 style='text-align: center;'>H-Bar Chart</h1>", unsafe_allow_html=True
    )
    fig = plt.figure()
    plt.style.use(
        "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle"
    )

    plt.barh(bar_x, bar_x * 10)
    st.write(fig)
