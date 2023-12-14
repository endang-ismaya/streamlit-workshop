import streamlit as st
import pandas as pd
import time

timestr = time.strftime("%Y%m%d-%H%M%S")


def home_page():
    """Home Page"""
    st.header("Home Page")
    data_file = st.file_uploader("Upload CSV", type=["csv"])

    if data_file:
        df = pd.read_csv(data_file)

        # saving form
        with st.form(key="editor_form"):
            edited_df = st.data_editor(df)

            btn_save = st.form_submit_button("Save")

        if btn_save:
            new_filename = f"{data_file.name}_edited_{timestr}.csv"
            final_dt = edited_df.to_csv()
            print(edited_df)

            st.download_button(
                label="Download data as csv",
                data=final_dt,
                file_name=new_filename,
                mime="text/csv",
            )


def about_page():
    """About Page"""
    st.header("About Page")


def main():
    """Main point of the app"""
    st.title("Data Editor App")

    mnu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", mnu)

    match choice:
        case "Home":
            home_page()

        case "About":
            about_page()

        case _:
            raise NotImplementedError("Page not found.")


if __name__ == "__main__":
    main()
