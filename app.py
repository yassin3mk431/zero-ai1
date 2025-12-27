import streamlit as st
import google.generative_ai as genai
from PIL import Image

st.set_page_config(page_title="ZERO AI", layout="centered")
st.title("🤖 ZERO AI")

genai.configure(api_key="AIzaSyBxYGRpnMggCdPY9pA2rtyWBib7N9KLJlc")
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Ask ZERO"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        if file:
            img = Image.open(file)
            res = model.generate_content([prompt, img])
        else:
            res = model.generate_content(prompt)
        st.markdown(res.text)
        st.session_state.messages.append({"role": "assistant", "content": res.text})
