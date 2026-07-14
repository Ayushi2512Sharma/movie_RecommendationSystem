import os
import pickle
from urllib import response
import requests
import pandas as pd
import numpy as np

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sklearn.metrics.pairwise import linear_kernel
from dotenv import load_dotenv

load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

OMDB_BASE = "https://www.omdbapi.com/"

if not OMDB_API_KEY:
    raise RuntimeError(
        "OMDB_API_KEY not found. Add it inside .env file"
    )

app = FastAPI(
    title="Movie Recommendation API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DF_PATH = os.path.join(BASE_DIR, "df.pkl")
TFIDF_MATRIX_PATH = os.path.join(BASE_DIR, "tfidf_matrix.pkl")
INDICES_PATH = os.path.join(BASE_DIR, "indices.pkl")

with open(DF_PATH, "rb") as f:
    movies = pickle.load(f)

with open(TFIDF_MATRIX_PATH, "rb") as f:
    tfidf_matrix = pickle.load(f)

with open(INDICES_PATH, "rb") as f:
    indices = pickle.load(f)

print(type(indices))
print(len(indices))
print(len(movies))
print(movies["title"].head(10))
print(list(indices.keys())[:10])

def get_movie_details(movie_name):

    url = f"{OMDB_BASE}?t={movie_name}&apikey={OMDB_API_KEY}"
    response = requests.get(url)

    data = response.json()

    if data["Response"] == "True":
        return data

    return None

def recommend(movie_name, top_n=10):

    movie_name = movie_name.lower()

    print("Movie:", movie_name)
    print("Movie exists:", movie_name in indices)
    print("First 20 keys:")
    print(list(indices.keys())[:20])


    if movie_name not in indices:
        return []

    idx = indices[movie_name]


    cosine_sim = linear_kernel(
        tfidf_matrix[idx:idx+1],
        tfidf_matrix
    ).flatten()

    sim_scores = list(enumerate(cosine_sim))

    sim_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )

    sim_scores = sim_scores[1:top_n+1]

    movie_indices = [i[0] for i in sim_scores]

    recommendations = []

    for i in movie_indices:

        title = movies.iloc[i]["title"]
        print("Recommended title:", title)

        details = get_movie_details(title)
        print(details is not None)
    
        if details:

            recommendations.append({

                "Title": details["Title"],
                "Year": details["Year"],
                "Genre": details["Genre"],
                "IMDb Rating": details["imdbRating"],
                "Poster": details["Poster"],
                "Plot": details["Plot"]

            })

    return recommendations

@app.get("/")
def home():
    return {
        "message": "Movie Recommendation API Running Successfully"
    }

@app.get("/movie")

def movie(movie_name: str):

    details = get_movie_details(movie_name)

    if details is None:

        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )

    return details

@app.get("/search")
def search_movies(movie_name: str):

    url = f"https://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={movie_name}"

    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        return data["Search"]
    else:
        return []
    
@app.get("/recommend")
def movie_recommendation(
    movie_name: str = Query(...),
    top_n: int = Query(10)
):
    recommendations = recommend(movie_name, top_n)
    return {
        "Movie": movie_name,
        "Recommendations": recommendations
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True

    )