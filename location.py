import streamlit as st
import geocoder

st.title("📍 Live Location")

g = geocoder.ip('me')
location = g.latlng

if location:
    st.write(f"Your location: Latitude: {location[0]}, Longitude: {location[1]}")
else:
    st.warning("Unable to detect location.")
