from src.api import search_movie
from src.database import add_favorite, delete_favorite, is_favorite, add_watchlist, is_watchlist, add_watched, is_watched, delete_watchlist, delete_watched
import streamlit as st

def display_movie(movie, show_favorite_button=True, delete_from=None, show_watchlist_button=True, show_watched_button=True):
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
        col1, col2 = st.columns([1, 2])
        with col1:
            if show_favorite_button:
                if is_favorite(movie):
                    st.info("Already in favorites 💖")
                else:
                    add_fav = st.button("Add to favorites 💖", key=f"add_{movie['tmdb_id']}")
                    if add_fav:                      
                        add_favorite(movie)
                        if not is_watched(movie):
                            add_watched(movie)
                        if is_watchlist(movie):
                            delete_watchlist(movie)
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
        with col2:
            if show_watched_button:
                if is_watched(movie):
                    st.info("Already in Watched ✅")
                else:
                    add_watchedlist = st.button("Add to watched ✅", key=f"watched_{movie['tmdb_id']}")
                    if add_watchedlist:
                        delete_watchlist(movie)
                        add_watched(movie)
                        st.success("Movie added to watched")
                        st.rerun()
            if delete_from:
                            delete = st.button("Remove", key=f"delete{delete_from}_{movie['tmdb_id']}")
                            if delete:
                                if delete_from == "favorites":
                                    delete_favorite(movie)
                                elif delete_from == "watchlist":
                                    delete_watchlist(movie)
                                elif delete_from == "watched":
                                    delete_watched(movie)
                                st.success("Movie removed")
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