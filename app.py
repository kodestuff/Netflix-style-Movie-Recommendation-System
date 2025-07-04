import streamlit as st
from model import recommend_movies, top_rated_movies, popular_movies
from utils import fetch_poster

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title('🎬 Movie Recommender System')

user_input = st.text_input('Enter a movie name')

if user_input:
    recommendations = recommend_movies(user_input)

    if isinstance(recommendations, list) and recommendations:
        st.subheader("👉 You may also like:")
        cols = st.columns(len(recommendations))
        for idx, movie in enumerate(recommendations):
            with cols[idx]:
                st.image(fetch_poster(movie['tmdbId']), caption=movie['title'], use_column_width=True)
    else:
        st.warning("⚠️ Movie not found in database or no recommendations.")

st.markdown('## ⭐ Top Rated Movies')
top_rated = top_rated_movies()
if top_rated:
    cols = st.columns(len(top_rated))
    for i, movie in enumerate(top_rated):
        with cols[i]:
            st.image(fetch_poster(movie['tmdbId']), caption=movie['title'], use_column_width=True)

st.markdown('## 🔥 Popular Movies')
popular = popular_movies()
if popular:
    cols = st.columns(len(popular))
    for i, movie in enumerate(popular):
        with cols[i]:
            st.image(fetch_poster(movie['tmdbId']), caption=movie['title'], use_column_width=True)
