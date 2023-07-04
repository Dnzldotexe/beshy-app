"""
This module displays text on the user screen when changes are made
"""
# Importing streamlit
import streamlit as st

# Caching the fetched data every 0.01 second
@st.cache_data(ttl=0.01)

def display_text(txt: str):
    """
    Displays a block of text on the page
    """
    st.write(txt)
