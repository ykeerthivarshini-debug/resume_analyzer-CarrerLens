import streamlit as st

st.title("Resume Analyzer - CareerLens")
st.write("Welcome! This is the official Streamlit interface for resume analysis.")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "txt"])
if uploaded_file is not None:
    st.success("Resume uploaded successfully!")
