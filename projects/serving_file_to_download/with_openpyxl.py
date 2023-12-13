import io
import streamlit as st
from openpyxl import Workbook


def generate_excel_content():
    # Your logic to generate the Excel content using openpyxl
    wb = Workbook()
    ws = wb.active

    # Add data to the worksheet
    data = [["Column1", "Column2"], [1, "AXXX"], [2, "BXX"], [3, "CXX"], [4, "DXX"]]

    for row in data:
        ws.append(row)

    return wb


def main():
    st.title("Download Excel File Example")

    # Button to trigger the download
    wb = generate_excel_content()

    # Save the Excel file to a stream buffer
    bio = io.BytesIO()
    wb.save(bio)
    bio.seek(0)

    # Provide a download link for the Excel file
    st.download_button(
        label="Click to Download",
        data=bio,
        file_name="example_openpyxl.xlsx",
        key="download_button",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


if __name__ == "__main__":
    main()
