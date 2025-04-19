import streamlit as st
import streamlit_authenticator as stauth

# Define credentials
names = ["User1", "User2"]
usernames = ["user1", "user2"]
passwords = ["password1", "password2"]

# Hash passwords
hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, cookie_name="sheSafe", key="123")

name, authentication_status = authenticator.login("Login", "main")

if authentication_status:
    st.write(f"Welcome {name}!")
else:
    st.warning("Please log in to access the app.")
