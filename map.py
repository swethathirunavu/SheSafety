import streamlit as st
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium

st.title("🗺️ Nearest Police Stations")

location = st.text_input("Enter Your Location (City)")

if location:
    geolocator = Nominatim(user_agent="sheSafeApp")
    location = geolocator.geocode(location)
    
    if location:
        st.write(f"Displaying police stations near {location.address}")
        map_ = folium.Map(location=[location.latitude, location.longitude], zoom_start=12)

        # For demo, adding a static police station
        folium.Marker([location.latitude + 0.01, location.longitude + 0.01], popup="Police Station").add_to(map_)

        st_folium(map_, width=700)
    else:
        st.warning("Could not find location.")
