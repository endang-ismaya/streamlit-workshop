import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure
import altair as alt

DATA_PATH = r"data/csv/trees.csv"

st.title("SF Trees")
st.write(
    """This app analyzes trees in San Francisco using
    a dataset kindly provided by SF DPW"""
)
trees_df = pd.read_csv(DATA_PATH)
df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
df_dbh_grouped.columns = ["tree_count"]
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)


trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.sample(n=1000)
st.map(trees_df)


st.subheader("Plotly Chart")
trees_df = pd.read_csv(DATA_PATH)
fig = px.histogram(trees_df["dbh"])
st.plotly_chart(fig)


trees_df = pd.read_csv(DATA_PATH)
trees_df["age"] = (pd.to_datetime("today") - pd.to_datetime(trees_df["date"])).dt.days
st.subheader("Seaborn Chart")
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df["age"])
plt.xlabel("Age (Days)")
st.pyplot(fig_sb)
st.subheader("Matploblib Chart")
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df["age"])
plt.xlabel("Age (Days)")
st.pyplot(fig_mpl)


st.subheader("Bokeh Chart")
trees_df = pd.read_csv(DATA_PATH)
scatterplot = figure(title="Bokeh Scatterplot")
scatterplot.scatter(trees_df["dbh"], trees_df["site_order"])
st.bokeh_chart(scatterplot)
scatterplot.xaxis.axis_label = "dbh"


st.subheader("Altair Chart")
trees_df = pd.read_csv(DATA_PATH)
df_caretaker = trees_df.groupby(["caretaker"]).count()["tree_id"].reset_index()
df_caretaker.columns = ["caretaker", "tree_count"]
fig = alt.Chart(df_caretaker).mark_bar().encode(x="caretaker", y="tree_count")
st.altair_chart(fig)
