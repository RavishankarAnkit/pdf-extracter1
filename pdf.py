import streamlit as st
import fitz  # PyMuPDF

st.title("PDF Text Extractor")

# Upload PDF
uploaded_file = st.file_uploader("Upload PDF File", type=["pdf"])

if uploaded_file is not None:

    # Open PDF
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    full_text = ""

    # Read all pages
    for page in doc:
        full_text += page.get_text()

    st.subheader("Extracted Text")

    # Show extracted text
    st.text_area("PDF Content", full_text, height=400)
