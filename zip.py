import gzip
import streamlit as st

st.title("Compress Files")

uploaded_file = st.file_uploader(
    "File to Compress",
    "txt",
)
if uploaded_file is not None:
    data = uploaded_file.read()
    compressed_data = gzip.compress(data)
    st.download_button(
        "Download Compressed File",
        compressed_data,
        f"{uploaded_file.name}.gz",
    )
