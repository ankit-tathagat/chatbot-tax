import streamlit as st
import redis

# Create Redis connection

# from database import get_redis_connection
r = r = redis.Redis(host='localhost', port=6379, db=0)

def upload_pdf_file():
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        r.set(uploaded_file.name, uploaded_file.read())
        st.success("File uploaded successfully")

def view_pdf_file():
    keys = r.keys()
    selected_file = st.selectbox("Select a file to view", keys)
    if selected_file:
        file_data = r.get(selected_file)
        st.write(file_data)
        st.download_button(
            label="Download PDF",
            data=file_data,
            file_name=selected_file,
            mime="application/pdf"
        )

def main():
    st.title("PDF File Uploader")
    st.sidebar.header("Navigation")
    pages = {
        "Upload PDF file": upload_pdf_file,
        "View PDF file": view_pdf_file,
    }
    page = st.sidebar.selectbox("Select a page", tuple(pages.keys()))
    pages[page]()

if __name__ == "__main__":
    main()
