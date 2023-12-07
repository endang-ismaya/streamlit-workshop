import streamlit as st
import time


# bar = st.progress(2)
# for i in range(100):
#     time.sleep(0.04)
#     bar.progress(i + 1)
# with st.spinner("Wait for it..."):
#     time.sleep(5)
# st.balloons()
# st.snow()
def simulate_background_process():
    # Simulating a time-consuming process
    for _ in range(5):
        time.sleep(1)


# Streamlit app
def main():
    st.title("Streamlit Spinner Example")
    btn_pl = st.empty()

    # Initialize session state
    if "is_running" not in st.session_state:
        st.session_state.is_running = False

    # Button to trigger the background process
    if not st.session_state.is_running:
        run_button = btn_pl.button("Run Background Process", key="run_button")

        if run_button:
            btn_pl.empty()
            st.session_state.is_running = True
            with st.spinner("Running in the background..."):
                # Call your time-consuming function here
                simulate_background_process()
            st.success("Background process completed!")
            # st.session_state.is_running = False
            del st.session_state["is_running"]
    else:
        st.warning("Please wait, background process is still running...")


if __name__ == "__main__":
    main()
