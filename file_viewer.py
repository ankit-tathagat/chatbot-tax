from PyPDF2 import PdfReader
import os
import streamlit as st
data_dir = os.path.join(os.curdir,'data_tax')
# pdf_files = sorted([x for x in os.listdir(data_dir) if 'DS_Store' not in x])
# pdf_files
# file = 'Torrent_Pharmaceuticals_Ltd_vs_The_Deputy_Commissioner_Of_Income_on_22_February_2022.PDF'
# path = data_dir + "\\" + file
# print(path)

def get_path(file):
    path = data_dir + "\\" + file 
    return path

def read_pdf(file): 
    path = get_path(file)      
    pdf_reader = PdfReader(path)
    # if st.button("Read PDF"):
    for page in range(len(pdf_reader.pages)):
        st.write(pdf_reader.pages[page].extract_text())

def download_pdf(file):
    # Add a file selector
    file_path = get_path(file)

    # If a file is selected, show a download button
    if file_path is not None:
        with open(file_path, "rb") as f:
            pdf_data = f.read()

    st.download_button(
        label="Download PDF",
        data= pdf_data,
        file_name=file_path.split('/')[-1],
        mime="application/pdf"
    )