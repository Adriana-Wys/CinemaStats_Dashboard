from src.api import search_movie, get_movie
from src.utils import display_movie, convert_db_movie
from src.database import connect_database, create_database, get_favorites, count_favorites, count_watchlist, get_watchlist
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
    ["🔍 Search", "💖 Favorites", "⏳ To Watch"]
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
    st.write(f"{count_favorites()} Movies on favorites list")
    fav_movie_name = st.text_input("Search favorites", placeholder="Enter the movie title...")
    sort_option = st.selectbox("Sort favorites by:", ["Default", "Title", "Rating", "Release Date"])
    if sort_option == "Title":
        favorites = get_favorites("title")
    elif sort_option == "Rating":
        favorites = get_favorites("rating")
    elif sort_option == "Release Date":
        favorites = get_favorites("release_date")
    else:
        favorites = get_favorites()
    found = False
    for movie in favorites:
        movie = convert_db_movie(movie)
        if fav_movie_name.lower() in movie["title"].lower():
            found = True
            display_movie(movie, show_favorite_button=False, show_delete_button=True)
    if not found:
        st.info("No movies found in favorites")

if page == "⏳ To Watch":
    st.title("⏳ Watchlist")
    st.write(f"{count_watchlist()} Movies on watchlist")
    watchlist = get_watchlist()
    for movie in watchlist:
        movie = convert_db_movie(movie)
        display_movie(movie, show_favorite_button=True, show_delete_button=False, show_watchlist_button=False)