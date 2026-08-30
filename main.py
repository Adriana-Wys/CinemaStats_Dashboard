from src.api import search_movie
from src.api import get_movie
from src.utils import display_movie
from src.utils import convert_db_movie
from src.database import connect_database
from src.database import create_database
from src.database import get_favorites
import streamlit as st

create_database()
connect_database()

st.set_page_config (
    page_title="CinemaStats_Dashboard",
    page_icon="📽️",
    layout="wide"
)

page = st.sidebar.radio(
    "Navigation",
    ["🔍 Search", "💖 Favorites"]
)

if page == "🔍 Search":
    st.title("📽️ CinemaStats_Dashboard")
    st.write("Search for a movie")
    movie_name = st.text_input("Title", placeholder="Enter the movie title...")
    if "movie" not in st.session_state:
        st.session_state.movie = None
    if st.button("🔍 Search"):
        if not movie_name.strip():
            st.warning("Please enter a movie title.")
        else:
            results = search_movie(movie_name)
            movie = get_movie(results)
            if movie:
                st.session_state.movie = movie
            else:
                st.error("Movie not found.")
    if st.session_state.movie:
        display_movie(st.session_state.movie)

if page == "💖 Favorites":
    st.title("💖 Favorite Movies")
    favorites = get_favorites()
    for movie in favorites:
        movie = convert_db_movie(movie)
        display_movie(movie, show_favorite_button=False)


