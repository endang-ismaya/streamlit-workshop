import streamlit as st
import openpyxl


def read_excel(file_path):
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(row)
        return data
    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
        return None


def main():
    st.title("Excel Reader App")

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        st.write("### Uploaded Excel File:")
        st.write(uploaded_file.name)

        data = read_excel(uploaded_file)

        if data is not None:
            st.write("### Excel Data:")
            st.write(data)


if __name__ == "__main__":
    main()
