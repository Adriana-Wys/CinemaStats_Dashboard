from src.api import search_movie
from src.database import add_favorite, delete_favorite, is_favorite, add_watchlist, is_watchlist
import streamlit as st

def display_movie(movie, show_favorite_button=True, show_delete_button=False, show_watchlist_button=True):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(f"{movie['poster']}")
    with col2: 
        st.title(f"🎞️ {movie['title']}")
        rating = round(movie['rating'],2)
        st.write(f"🌟 {rating}")
        st.write(f"📆 {movie['release_date']}")
        st.write(f"🌍 {movie['language']}")
        st.divider()
        st.subheader("Overview")
        st.write(f"📄 {movie['overview']}")
        if show_favorite_button:
            if is_favorite(movie):
                st.info("Already in favorites 💖")
            else:
                add_fav = st.button("Add to favorites 💖", key=f"add_{movie['tmdb_id']}")
                if add_fav:
                    add_favorite(movie)
                    st.success("Movie added to favorites!")
                    st.rerun()
        if show_watchlist_button:
            if is_watchlist(movie):
                st.info("Already on watchlist")
            else:
                add_towatch = st.button("Add to watchlist ⏳", key=f"watch_{movie['tmdb_id']}")
                if add_towatch:
                    add_watchlist(movie)
                    st.success("Movie added to watchlist")
                    st.rerun()
        if show_delete_button:
            del_fav = st.button("Remove", key=f"delete_{movie['tmdb_id']}")
            if del_fav:
                delete_favorite(movie)
                st.success("Movie removed from favorites")
                st.rerun()

def get_language_name(code):
    LANGUAGES = {
        "en": "English",
        "pl": "Polish",
        "fr": "French",
        "de": "German",
        "jp": "Japanese",
        "kr": "Korean",
        "es": "Spanish"
    }
    return LANGUAGES.get(code,"Unknown")

def convert_db_movie(movie):
    return {
        "tmdb_id": movie[1],
        "title": movie[2],
        "rating": movie[3],
        "release_date": movie[4],
        "language": movie[5],
        "poster": movie[6],
        "overview": movie[7] 
    }