import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

import streamlit as st

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

def load_css():
    st.markdown("""
    <style>

    .stApp{
    background:linear-gradient(135deg,#0f172a,#1e293b);
    color:white;
}

    h1{
        color:#E50914;
    }
                
    .movie-card{
    background:#1f2937;
    padding:18px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.4);
    margin-bottom:20px;
    transition:0.3s;
}

.movie-card:hover{
    transform:scale(1.03);
}            

    </style>
    """, unsafe_allow_html=True)

load_css()

st.markdown("""
<h1 style="
text-align:center;
color:#E50914;
font-size:48px;
font-weight:bold;
margin-bottom:10px;">
🎬 Movie Recommendation System
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style="
text-align:center;
color:#D1D5DB;
margin-bottom:35px;">
Discover movies you'll love with AI-powered recommendations 🍿
</h4>
""", unsafe_allow_html=True)

st.markdown("### 🔍 Search Your Favorite Movie")

movie_name = st.text_input(
    "",
    placeholder="Type movie name here... (e.g. Inception)"
)

st.markdown("### 🎯 Number of Recommendations")

top_n = st.slider(
    "",
    min_value=5,
    max_value=20,
    value=10
)

if st.button(
    "🎬 Recommend Movies",
    use_container_width=True
):

    if movie_name == "":
        st.warning("Please enter a movie name.")
        st.stop()

    movie_response = requests.get(
        f"{BASE_URL}/movie",
        params={"movie_name": movie_name}
    )

    if movie_response.status_code != 200:
        st.error("Movie not found.")
        st.stop()

    movie = movie_response.json()

    st.markdown("## 🎥 Movie Details")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(movie["Poster"], use_container_width=True)

    with col2:

        st.markdown(f"## {movie['Title']}")

        st.markdown(
            f"""
    ⭐ **IMDb Rating:** {movie['imdbRating']}

    📅 **Year:** {movie['Year']}

    🎭 **Genre:** {movie['Genre']}

    🎬 **Director:** {movie['Director']}

    👥 **Actors:** {movie['Actors']}
    """
        )

        st.markdown("### 📖 Story")

        st.info(movie["Plot"])

        st.divider()
        search_response = requests.get(
            f"{BASE_URL}/search",
            params={"movie_name": movie_name}
    )

        search_movies = search_response.json()

        st.markdown("## 🎬 Movie Series")

        cols = st.columns(5)

        for i, movie in enumerate(search_movies):

            with cols[i % 5]:

                if movie["Poster"] != "N/A":
                    st.image(movie["Poster"], use_container_width=True)
                else:
                    st.write("🎬 Poster Not Available")

                st.caption(movie["Title"])

                st.caption(movie["Year"])

        rec_response = requests.get(
            f"{BASE_URL}/recommend",
            params={
                "movie_name": movie_name,
                "top_n": top_n
            }
        )
        st.write(rec_response.status_code)
        st.write(rec_response.text)
        data = rec_response.json()

        st.markdown("---")
        st.markdown("## 🍿 Recommended Movies")

        recommendations = data["Recommendations"]

        cols = st.columns(5)

        for i, movie in enumerate(recommendations):

            with cols[i % 5]:

                if movie["Poster"] != "N/A":
                    st.image(movie["Poster"], use_container_width=True)
                else:
                    st.write("🎬 Poster Not Available")

                st.markdown(
                    f"<h5 style='text-align:center; color:white;'>{movie['Title']}</h5>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"<p style='text-align:center;'>⭐ {movie['IMDb Rating']}</p>",
                    unsafe_allow_html=True
                )

                st.caption(f"📅 {movie['Year']}")

                st.caption(f"🎭 {movie['Genre']}")

                st.link_button(
                    "🎬 IMDb",
                    f"https://www.imdb.com/find?q={movie['Title']}"
                )

st.markdown("## 🔥 Trending Movies")

trending_movies = [
    "Oppenheimer",
    "Barbie",
    "Avatar",
    "Interstellar",
    "Inception",
    "Dune",
    "Joker",
    "Titanic",
    "The Dark Knight",
    "Avengers: Endgame"
]

cols = st.columns(5)

for i, title in enumerate(trending_movies):

    response = requests.get(
        f"{BASE_URL}/movie",
        params={"movie_name": title}
    )

    if response.status_code == 200:

        movie = response.json()

        with cols[i % 5]:

            if movie["Poster"] != "N/A":
                st.image(movie["Poster"], use_container_width=True)

            st.markdown(
                f"<p style='text-align:center; font-weight:bold; color:white;'>{movie['Title']}</p>",
                unsafe_allow_html=True
            )

