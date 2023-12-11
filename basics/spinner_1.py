import streamlit as st


def main():
    st.title("Disable Button After Click Example")

    # Initialize session state
    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False

    # Button to trigger an action
    if not st.session_state.button_clicked:
        button_clicked = st.button("Click me to disable", key="disable_button")

        # Check if the button is clicked
        if button_clicked:
            print("clicked")
            st.session_state.button_clicked = True
            st.success("Button clicked!")
    else:
        st.warning("Button is disabled after click.")


if __name__ == "__main__":
    main()
