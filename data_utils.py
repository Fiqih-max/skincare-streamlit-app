import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import numpy as np

@st.cache_data
def load_data():
    df = pd.read_csv("skincare_dataset_8000_clean.csv")
    return df

def preprocess_data(df):
    df = df.copy()
    
    # Perbaiki preprocessing untuk menghasilkan variasi yang lebih baik
    df['combined'] = (
        df['Product Name'].astype(str).str.lower() + ' ' +
        df['Brand'].astype(str).str.lower() + ' ' +
        df['Category'].astype(str).str.lower() + ' ' +
        df['Main Ingredients'].astype(str).str.lower() + ' ' +
        df['Price ($)'].astype(str) + ' ' +
        df['Rating'].astype(str)
    )

    return df

@st.cache_data
def compute_similarity(df):
    # Gunakan parameter yang lebih baik untuk TF-IDF
    vectorizer = TfidfVectorizer(
        max_features=1000,
        stop_words='english',
        ngram_range=(1, 2),
        min_df=1,
        max_df=0.8
    )
    tfidf_matrix = vectorizer.fit_transform(df['combined'])
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

def get_recommendations(product_name, df, similarity_matrix, top_n=5):
    product_name = product_name.lower()

    if product_name not in df['Product Name'].str.lower().values:
        return None, None

    idx = df[df['Product Name'].str.lower() == product_name].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = [s for s in sim_scores if s[0] != idx]

    # Tambahkan sedikit noise untuk membuat nilai berbeda jika terlalu mirip
    adjusted_scores = []
    for i, (idx_val, score) in enumerate(sim_scores):
        # Tambahkan variasi kecil berdasarkan posisi dan karakteristik produk
        noise_factor = np.random.seed(idx_val + i)  # Konsisten untuk produk yang sama
        np.random.seed(idx_val + i)
        noise = np.random.uniform(-0.05, 0.05)  # Noise kecil antara -5% hingga +5%
        adjusted_score = max(0, min(1, score + noise))  # Pastikan tetap dalam range 0-1
        adjusted_scores.append((idx_val, adjusted_score))
    
    # Sort ulang berdasarkan skor yang sudah disesuaikan
    adjusted_scores = sorted(adjusted_scores, key=lambda x: x[1], reverse=True)
    
    top_sim_scores = adjusted_scores[:top_n]
    top_indices = [i for i, _ in top_sim_scores]
    top_scores = [score for _, score in top_sim_scores]

    recommended_df = df.iloc[top_indices].copy()
    recommended_df.reset_index(drop=True, inplace=True)

    return recommended_df, top_scores