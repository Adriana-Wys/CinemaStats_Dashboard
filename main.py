from src.api import search_movie
from src.api import get_movie
from src.utils import display_movie
import streamlit as st

st.set_page_config (
    page_title="CinemaStats_Dashboard",
    page_icon="📽️",
    layout="wide"
)

st.title("📽️ CinemaStats_Dashboard")
st.write("Search for a movie")

movie = search_movie("Interstellar")

movie_name = st.text_input("Title", placeholder="Enter the movie title...")
if st.button("🔍 Search"):
    if not movie_name.strip():
        st.warning("Please enter a movie title.")
    else:
        results = search_movie(movie_name)
        movie = get_movie(results)
        if movie:
            display_movie(movie)
        else:
            st.error("Movie not found.")


