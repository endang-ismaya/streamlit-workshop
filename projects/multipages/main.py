import streamlit as st


# Function to render the home page
def render_home():
    st.title("Multi-Page Streamlit App")
    st.write("This is the home page.")
    st.write("Click on the navigation bar to explore other pages.")


# Function to render the about page
def render_about():
    st.title("About Page")
    st.write("This is the about page.")
    st.write("Welcome to the about page of the multi-page Streamlit app.")


# Function to render the contact page
def render_contact():
    st.title("Contact Page")
    st.write("This is the contact page.")
    st.write("Feel free to reach out to us using the contact information below.")


# Main function to handle page navigation
def main():
    st.sidebar.title("Navigation")
    pages = ["Home", "About", "Contact"]
    choice = st.sidebar.radio("Go to", pages)

    if choice == "Home":
        render_home()
    elif choice == "About":
        render_about()
    elif choice == "Contact":
        render_contact()


if __name__ == "__main__":
    main()
