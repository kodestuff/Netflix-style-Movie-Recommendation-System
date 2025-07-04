import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

af = pd.read_csv('movies.csv')

tfidf = TfidfVectorizer(stop_words='english')
af['overview'] = af['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(af['overview'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(af.index, index=af['title'].str.lower()).drop_duplicates()

def recommend_movies(title, num=5):
    idx = indices.get(title.lower())
    if idx is None:
        return []
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num+1]
    movie_indices = [i[0] for i in sim_scores]
    return af[['title', 'tmdbId']].iloc[movie_indices].to_dict(orient='records')

def top_rated_movies(num=5):
    filtered = af[af['vote_count'] >= 1000]
    top = filtered.sort_values(by='vote_average', ascending=False).head(num)
    return top[['title', 'tmdbId']].to_dict(orient='records')

def popular_movies(num=5):
    if 'popularity' not in af.columns:
        top = af.sort_values(by='vote_count', ascending=False).head(num)
    else:
        top = af.sort_values(by='popularity', ascending=False).head(num)
    return top[['title', 'tmdbId']].to_dict(orient='records')
