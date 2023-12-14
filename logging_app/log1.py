import streamlit as st
import logging
import datetime


@st.cache_data
def get_current_date() -> str:
    """Get Current Date YYYYMMDD"""
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d")


# logging config
LOGS_FORMAT = "%(levelname)s %(asctime)s.%(msecs)03d - %(message)s"
# logging.basicConfig(
#     level=logging.DEBUG,
#     format=LOGS_FORMAT,
# )
# logger = logging.getLogger(__name__)

# log to file
logf = logging.getLogger(__name__)
logf.setLevel(logging.DEBUG)

formatter = logging.Formatter(LOGS_FORMAT)
file_handler = logging.FileHandler(rf"data/logs/{get_current_date()}_activity.log")
file_handler.setFormatter(formatter)

if logf.hasHandlers():
    logf.handlers.clear()

logf.addHandler(file_handler)


def main():
    st.title("Adding logs to App")
    st.text("Track All Activities in App")

    mnu = ["Home", "EDA", "ML", "About"]
    choice = st.sidebar.selectbox("Select Your Navigation", mnu)

    match (choice):
        case "Home":
            st.subheader("Home Section")
            logf.info("Home Section")

        case "EDA":
            st.subheader("EDA Section")
            logf.info("EDA Section")

        case "ML":
            st.subheader("ML Section")
            logf.info("ML Section")

        case "About":
            st.subheader("About Section")
            logf.info("About Section")

        case _:
            st.subheader("Invalid Section")
            logf.info("Invalid Section")


if __name__ == "__main__":
    main()
