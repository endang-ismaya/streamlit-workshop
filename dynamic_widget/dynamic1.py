import streamlit as st

my_dict = {}
btn_del = {}


def add_text_input():
    new_input = st.text_input("Enter text:")
    return new_input


def delete_text(idx):
    print(my_dict[idx])
    print(btn_del[idx])
    del my_dict[idx]
    del btn_del[idx]


def create_widgets(num):
    for i, row in enumerate(num):
        with st.container():
            col1, col2 = st.columns([3, 1])
            my_dict[i] = col1.text_input(
                label="You can write a date",
                value=row,
                max_chars=5,
                label_visibility="hidden",
                key=f"date{i}",
            )
            col2.text("")
            col2.text("")
            btn_del[i] = col2.button(
                "Delete?", on_click=delete_text, args=(i,), key=f"btn_date{i}"
            )


def main():
    st.title("Dynamic Widget Example")

    # # Create a button to add new text input
    # if st.button("Add Text Input"):
    #     # Use st.session_state to keep track of the dynamically created inputs
    #     if "text_inputs" not in st.session_state:
    #         st.session_state.text_inputs = []

    #     # Add a new text input and store it in session state
    #     new_input = add_text_input()
    #     print(new_input)
    #     st.session_state.text_inputs.append(new_input)

    # # Display the entered values
    # if "text_inputs" in st.session_state:
    #     st.write("Entered Values:")
    #     for i, text_input in enumerate(st.session_state.text_inputs, start=1):
    #         st.write(f"{i}. {text_input}")
    print(my_dict)
    st.write(st.session_state)


if __name__ == "__main__":
    main()
