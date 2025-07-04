# 🎬 Netflix-style Movie Recommendation System

This project recommends movies similar to what you love using content-based filtering (TF-IDF + cosine similarity) and visualizes them with TMDB posters — all in a Netflix-style UI built with Streamlit.

## 🚀 Features
- 🔍 Enter a movie to get smart recommendations
- ⭐ View Top-Rated Movies
- 🔥 Discover Popular Titles
- 🎨 Auto-fetched movie posters via TMDB

## 📁 Files
- `app.py` – Main Streamlit app
- `model.py` – Recommendation logic
- `utils.py` – Poster fetching via TMDB
- `movies.csv` – Cleaned data (you add this)
- `requirements.txt` – Libraries needed

## 🛠 Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/movie-recommender.git
   cd movie-recommender
   ```

2. Install packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## 📦 Dataset
Source: [TMDb 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
