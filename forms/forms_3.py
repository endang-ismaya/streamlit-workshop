import streamlit as st


def main():
    st.title("Streamlit Form Example")

    # Create a form using st.form
    with st.form("user_input_form", clear_on_submit=True):
        # Text input field for the user's name
        user_name = st.text_input("Enter your name", key="user_name")

        # Number input field for the user's age
        user_age = st.number_input("Enter your age", min_value=0, key="user_age")

        # Checkbox for user's preferences
        user_preferences = st.checkbox(
            "I agree to the terms and conditions", key="user_agreement"
        )

        # Submit button to submit the form
        form_submit_button = st.form_submit_button("Submit")

    # Check if the form is submitted
    if form_submit_button:
        # Print the values entered in the form
        st.write("### Form Values:")
        st.write(f"Name: {user_name}")
        st.write(f"Age: {user_age}")
        st.write(f"Agreed to terms and conditions: {user_preferences}")
        st.write(st.session_state)


if __name__ == "__main__":
    main()
