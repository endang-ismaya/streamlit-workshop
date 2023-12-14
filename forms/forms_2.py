import streamlit as st


st.title("Displaying Form")

# form
btn_submit = None

with st.form("form_key"):
    st.write("What would you like to order?")

    appetizer = st.selectbox("Appetizers", options=["app_1", "app_2", "app_3"])
    main_course = st.selectbox("Main Course", options=["app_1", "app_2", "app_3"])
    dessert = st.selectbox("Dessert", options=["des_1", "des_2", "des_3"])

    spicy = st.checkbox("Spicy?")
    visit_date = st.date_input("When are you coming?")
    visit_time = st.time_input("At what time are you coming?")

    allergies = st.text_area("Any allergies?", placeholder="Leave your allergies here")

    btn_submit = st.form_submit_button("Submit", type="primary")


btn_cancel = st.button("Cancel Order", type="secondary")
if btn_cancel:
    btn_submit = None

st.write("Your order summary:")
if btn_submit:
    col1, col2 = st.columns(spec=2)

    col1.write("Appetizer: ")
    col2.write(appetizer)

    col1.write("Main course: ")
    col2.write(main_course)

    col1.write("Dessert: ")
    col2.write(dessert)

    col1.write("Spicy: ")
    col2.write("yes" if spicy else "no")

    col1.write("Date of visit: ")
    col2.write(visit_date)

    col1.write("Time of visit: ")
    col2.write(visit_time)

    col1.write("Alergies")
    col2.write(allergies)
