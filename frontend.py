import streamlit as st
import requests

st.title("Smart City Assistant")

question = st.text_input("Ask a question about your city:")

if st.button("Submit"):
    res = requests.post("http://localhost:8000/ask", json={"question": question})
    st.write("Answer:", res.json()["answer"])