import streamlit as st
import PyPDF2
import os.path
import pathlib
from streamlit_extras.switch_page_button import switch_page
import time

global START_TIME 
START_TIME = 0
st.set_page_config(
    page_title="Upload File(s)",
    page_icon="🗃",
)

st.write("# Upload your PDF file here!")
# Upload PDF file
uploaded_file = st.file_uploader("", type="pdf")

def upload():
    if uploaded_file is None:
        st.session_state["upload_state"] = "Upload a file first!"
    else:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        num_pages = len(pdf_reader.pages)

        # Create a new PDF file writer
        pdf_writer = PyPDF2.PdfWriter()
        
        # Copy each page to the new file
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
            
        # Save the new file
        output_filename = f"./data/{uploaded_file.name}_copy.pdf"
        with open(output_filename, "wb") as f:
            pdf_writer.write(f)        
        st.session_state["upload_state"] = "Saved " + " successfully!"
        

col1, _, _, _, _, _, col7 = st.columns([1]*6+[1.02], gap = "medium")

with col1:
    if st.button('Search'):
        switch_page("Search")

with col7:
    upload = st.button("Upload", on_click=upload)
    
# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)
# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1, text=progress_text)
# time.sleep(10)
# START_TIME = 0

if upload:
    with st.spinner('Uploading...'):
        time.sleep(5)
        START_TIME += 5
    st.success('Upload was successful!', icon="✅")

if START_TIME == 5:
    with st.spinner('Processing file...'):
        time.sleep(10)    
    st.success('Processing Completed! Go to Search to start searching', icon="✅")
    START_TIME += 10

START_TIME = 0