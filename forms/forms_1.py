import streamlit as st

st.markdown(
    "<h1 style='text-align: center;'>User Registration</h1>", unsafe_allow_html=True
)

# form = st.form("Form 1")
# form.text_input(label="First name")
# form.form_submit_button(label="Submit")


with st.form(key="registration_form"):
    col1, col2 = st.columns(spec=2)
    fname = col1.text_input(label="Firstname")
    lname = col2.text_input(label="Lastname")

    email = st.text_input(label="Email")
    password = st.text_input(label="Password", type="password")
    confirm_password = st.text_input(label="Confirm Password", type="password")

    day, month, year = st.columns(spec=3)
    day.text_input(label="Day")
    month.text_input(label="Month")
    year.text_input(label="Year")

    form_state = st.form_submit_button(label="Submit")

    if form_state:
        if not fname and not lname:
            st.warning("Firstname and Lastname are required fields")
        else:
            st.success("Registration has been submitted")
            print(st.session_state.registration_form)
