import streamlit as st

st.title("🤖 SheSafe Chatbot")

st.write("How can I help you today?")

user_input = st.text_input("Ask a question:")

if user_input:
    if "safety" in user_input.lower():
        st.write("Safety tip: Always trust your instincts and avoid isolated areas.")
    elif "help" in user_input.lower():
        st.write("Help is on the way! An SOS alert has been sent.")
    else:
        st.write("I'm here to help. Ask me something related to safety!")
