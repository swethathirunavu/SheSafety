import streamlit as st
from datetime import datetime
import smtplib

st.title("🔴 Emergency SOS Alert")

st.markdown("Send an emergency alert to your trusted contact instantly.")

name = st.text_input("Your Name")
location = st.text_input("Your Current Location / Area")
email = st.text_input("Trusted Contact's Email")

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def send_email(email, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    server.sendmail("your_email@gmail.com", email, message)
    server.quit()

if st.button("📨 Send SOS"):
    if name and location and email:
        message = f"SOS Alert from {name} at {location}. Time: {now}"
        send_email(email, message)
        st.success(f"SOS message sent successfully to {email}")
    else:
        st.warning("Please fill all fields.")
