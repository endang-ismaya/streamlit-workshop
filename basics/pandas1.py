import streamlit as st
import pandas as pd

tbl1 = pd.DataFrame({"Col 1": [1, 2, 3, 4, 5, 6, 7], "Col 2": [6, 7, 8, 9, 10, 11, 12]})
st.table(tbl1)

st.dataframe(tbl1)
