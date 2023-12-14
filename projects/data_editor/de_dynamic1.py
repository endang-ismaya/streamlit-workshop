import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

if st.button("Get List from DF"):
    data_list = edited_df.values.tolist()
    st.write(type(data_list))  # type(data_list)classbuiltins.list(iterable=(), /)
    st.write(data_list)

    for data in data_list:
        print(data)
# favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
# st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
