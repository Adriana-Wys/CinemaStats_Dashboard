from src.api import search_movie
from src.database import add_favorite
import streamlit as st

def display_movie(movie):
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
        add_fav = st.button("Add to favorites 💖")
        if add_fav:
            add_favorite(movie)
            st.success("Movie added to favorites!")

def get_language_name(code):
    LANGUAGES = {
        "en": "English",
        "pl": "Polish",
        "fr": "French",
        "de": "German",
        "ja": "Japanese",
        "ko": "Korean",
        "es": "Spanish"
    }
    return LANGUAGES.get(code,"Unknown")

