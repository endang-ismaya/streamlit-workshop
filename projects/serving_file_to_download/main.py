import streamlit as st
import pandas as pd
import io


def generate_text_content():
    # Your logic to generate the text content
    text_content = "Hello, this is the content of the text file.\nLine 2.\nLine 3."

    return text_content


def generate_excel_content():
    # Your logic to generate the Excel content
    data = {"Column1": [1, 2, 3, 4], "Column2": ["A", "B", "C", "D"]}
    df = pd.DataFrame(data)

    return df


def main():
    st.title("Download Text File Example")

    # Button to trigger the download
    # if st.button("Download Text File"):
    text_content = generate_text_content()

    # Provide a download link for the text file
    st.download_button(
        label="Download Text File",
        data=text_content.encode("utf-8"),
        file_name="example_text_file.txt",
        key="download_button1",
        mime="text/plain",
    )

    # Excel File
    df = generate_excel_content()

    # Create a stream buffer to store the Excel file
    excel_buffer = pd.ExcelWriter("example_excel_file.xlsx", engine="xlsxwriter")
    df.to_excel(excel_buffer, index=False)
    excel_buffer.close()

    # Provide a download link for the Excel file
    st.download_button(
        label="Click to Download",
        data=open("example_excel_file.xlsx", "rb").read(),
        file_name="example_excel_file.xlsx",
        key="download_button2",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    # using io
    bio = io.BytesIO()
    writer = pd.ExcelWriter(bio, engine="xlsxwriter")
    df.to_excel(writer, sheet_name="Sheet1")
    writer.close()
    bio.seek(0)

    st.download_button(
        label="Download Excel 2",
        data=bio,
        file_name="example_excel_file_bio.xlsx",
        key="download_button3",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


if __name__ == "__main__":
    main()
