# app.py

import streamlit as st
from home_depot import recommend  
st.markdown("""
    <style>
        .stApp {
        background-image: url("https://img.freepik.com/free-photo/abstract-brown-background-leaf-shadow-light-studio-empty-backdrop-product-display-scene-product-placement-3d-illustration_56104-1843.jpg?size=626&ext=jpg&ga=GA1.1.2008272138.1720569600&semt=ais_hybrid");
        background-size: cover;
        }
    </style>""", unsafe_allow_html=True)
# Page title
st.title('Home depot Product Recommendation System')

# Sidebar with user input
query = st.text_input('What exactly are you looking for:', " ")

# Button to trigger recommendation
if st.button('Recommend'):
    # Call recommend function
    result = recommend(query)
    
    # Display recommendation result
    st.subheader('Recommendation:')
    st.write(result)
