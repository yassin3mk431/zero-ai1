import streamlit as st
import google.generative_ai as genai
from PIL import Image

st.set_page_config(page_title="ZERO AI WORLD", layout="centered")
st.title("🤖 ZERO: THE TWIN AI")

genai.configure(api_key="AIzaSyBxYGRpnMggCdPY9pA2rtyWBib7N9KLJlc")
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_file = st.file_uploader("Upload Image...", type=["jpg", "png", "jpeg"])

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask ZERO..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Wait..."):
            try:
                if uploaded_file:
                    img = Image.open(uploaded_file)
                    response = model.generate_content([prompt, img])
                else:
                    response = model.generate_content(prompt)
                
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error("Error connected to API. Please check your Key.")
