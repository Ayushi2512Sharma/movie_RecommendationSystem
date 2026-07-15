# movie_RecommendationSystem

# 🎬 Movie Recommendation System

An end-to-end Machine Learning based Movie Recommendation System that recommends similar movies using **Content-Based Filtering**. The application is built with **FastAPI** for the backend and **Streamlit** for the frontend, providing an interactive user experience with movie details, posters, ratings, and recommendations.

--

## 🚀 Live Demo

🌐 **Live Application:** https://ayushi-movie-recommender.streamlit.app/

⚡ **Backend API:** https://ayushi-movie-recommendation-api.onrender.com

---

## 📌 Features

- 🔍 Search any movie by title
- 🎯 Get top similar movie recommendations
- 🎬 Movie posters
- ⭐ IMDb ratings
- 📖 Movie plot and genre information
- 🔥 Trending movie section
- 🌐 FastAPI REST API
- 🎨 Interactive Streamlit user interface
- ☁️ Fully deployed application

---

## 🧠 Machine Learning Approach

This project uses **Content-Based Recommendation**.

### Steps

1. Data Cleaning & Preprocessing
2. Feature Engineering
3. TF-IDF Vectorization
4. Cosine Similarity Calculation
5. Recommendation Generation

Movies with similar content are recommended based on textual similarity.

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### API
- OMDb API

### Deployment
- Render (Backend)
- Streamlit Community Cloud (Frontend)

---

## 📂 Project Structure

```text
Movie_RecommendationSystem/
│
├── app.py                 # Streamlit Frontend
├── main.py                # FastAPI Backend
├── requirements.txt
├── df.pkl
├── tfidf.pkl
├── tfidf_matrix.pkl
├── indices.pkl
├── .env
└── README.md
```

---

## 📸 Screenshots

### 🏠 Home Page

![Home Page](screenshots/home.png)

---

### 🔍 Movie Search

![Search](screenshots/search.png)

---

### 🎯 Recommendations

![Recommendations](screenshots/recommendation.png)

---

### 🔥 Trending Movies

![Trending](screenshots/trending.png)

## 📊 Recommendation Workflow

```text
User Search
      │
      ▼
Movie Title
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Top Similar Movies
      │
      ▼
OMDb API
      │
      ▼
Movie Details + Poster
      │
      ▼
Displayed in Streamlit
---
