import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Matplotlib and Seaborn Visualization")

# load the data
df = pd.read_csv(r"data/tips.csv")
st.dataframe(df.head())

# Questions
# 1. Find number of Male and Female distribution (pie and bar)
# 2. Find distribution of Male and Female spent (boxplot and kdeplot)
# 3. Find distribution of average total_bill across each day by male and female
# 4. Find the relation between total_bill and tip on time (scatter plot)


# 1. Answer
st.markdown("---")

with st.container():
    st.markdown("#### 1. Find number of Male and Female distribution (pie and bar)")

    value_counts = df["sex"].value_counts()
    st.dataframe(value_counts)

    col1, col2 = st.columns(spec=2)

    # draw a pie chart
    with col1:
        st.subheader("Pie Chart")
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct="%0.2f%%", labels=["Male", "Female"])
        st.pyplot(fig=fig)

    # bar chart
    with col2:
        st.subheader("Bar Chart")
        fig, ax = plt.subplots()
        ax.bar(["Male", "Female"], value_counts)
        st.pyplot(fig=fig)


data_types = df.dtypes
cat_cols = data_types[data_types == "object"].index
st.markdown("---")

with st.container():
    feature = st.selectbox("Select the feature you want to display", options=cat_cols)
    value_counts = df[feature].value_counts()
    st.dataframe(value_counts)

    col1, col2 = st.columns(spec=2)
    # draw a pie chart
    with col1:
        st.subheader("Pie Chart")
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct="%0.2f%%", labels=value_counts.index)
        st.pyplot(fig=fig)

    # bar chart
    with col2:
        st.subheader("Bar Chart")
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts)
        st.pyplot(fig=fig)

# 2. Answer
st.markdown("---")
with st.container():
    st.markdown(
        "#### 2. Find distribution of Male and Female spent (boxplot and kdeplot)"
    )

    # charts
    charts = ("box", "violin", "kdeplot", "histogram")
    chart_selection = st.selectbox("Select the chart type", charts)

    # columns
    col1, col2 = st.columns(spec=2)
    with col1:
        fig, ax = plt.subplots()

        if chart_selection == "box":
            sns.boxplot(x="sex", y="total_bill", data=df, ax=ax)
        elif chart_selection == "violin":
            sns.violinplot(x="sex", y="total_bill", data=df, ax=ax)
        elif chart_selection == "kdeplot":
            sns.kdeplot(x=df["total_bill"], hue=df["sex"], ax=ax, fill=True)
        elif chart_selection == "histogram":
            sns.histplot(x="total_bill", hue="sex", data=df, ax=ax)

        st.pyplot(fig)


# 3. Answer
st.markdown("---")
with st.container():
    st.markdown(
        "#### 3. Find distribution of average total_bill across each day by male and female"
    )

    features_to_groupby = ["day", "sex"]
    feature = ["total_bill"]
    select_cols = feature + features_to_groupby

    avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()
    st.dataframe(avg_total_bill)

    # visual
    fig, ax = plt.subplots()
    avg_total_bill = avg_total_bill.unstack()
    avg_total_bill.plot(kind="bar", ax=ax)
    ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5))
    st.pyplot(fig)

st.markdown("---")
with st.container():
    # 1. include all categorical features
    # 2. bar, area, line
    # 3. stacked

    col1, col2, col3 = st.columns(spec=3)

    with col1:
        group_cols = st.multiselect(
            "Select the features", cat_cols, default=cat_cols[0]
        )
        features_to_groupby = group_cols
        n_features = len(features_to_groupby)

    with col2:
        chart_type = st.selectbox("Select Chart type", ("bar", "area", "line"))

    with col3:
        stack_opt = st.radio("Stacked", ("Yes", "No"))

        if stack_opt == "Yes":
            stacked = True
        else:
            stacked = False

    feature = ["total_bill"]
    select_cols = feature + features_to_groupby

    avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()
    if n_features > 1:
        for i in range(n_features - 1):
            avg_total_bill = avg_total_bill.unstack()

    avg_total_bill.fillna(0, inplace=True)

    # # visual
    fig, ax = plt.subplots()
    avg_total_bill.plot(kind=chart_type, ax=ax, stacked=stacked)
    ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5))
    ax.set_ylabel("Avg Total Bill")
    st.pyplot(fig)

    st.dataframe(avg_total_bill)

# 4. Find the relation between total_bill and tip on time (scatter plot)
st.markdown("---")
st.markdown("#### 4. Find the relation between total_bill and tip on time")

fig, ax = plt.subplots()
hue_type = st.selectbox("Select the feature to hue", cat_cols)

sns.scatterplot(x="total_bill", y="tip", hue=hue_type, ax=ax, data=df)
st.pyplot(fig)
