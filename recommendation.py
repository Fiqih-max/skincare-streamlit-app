import streamlit as st
from data_utils import get_recommendations
import pandas as pd

def app(df, similarity_matrix):
    # Header dengan styling
    st.markdown("""
    <div style='text-align: center; padding: 20px; background: linear-gradient(90deg, #FF6B6B, #4ECDC4); 
                border-radius: 10px; margin-bottom: 30px;'>
        <h1 style='color: white; font-size: 2.5em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
            🔎 Hasil Rekomendasi Produk Skincare
        </h1>
        <p style='color: white; font-size: 1.1em; margin: 10px 0 0 0; opacity: 0.9;'>
            Temukan produk skincare yang sempurna untuk Anda
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom CSS untuk styling keseluruhan
    st.markdown("""
    <style>
    .product-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.5);
    }
    
    .product-title {
        color: #2c3e50;
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 15px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .product-info {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    
    .info-item {
        display: flex;
        align-items: center;
        padding: 5px 0;
        font-size: 1em;
        color: #34495e;
    }
    
    .info-icon {
        margin-right: 10px;
        font-size: 1.2em;
    }
    
    .price-highlight {
        background: linear-gradient(45deg, #FF6B6B, #FFE66D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    
    .rating-stars {
        color: #f39c12;
        font-weight: bold;
    }
    
    .similarity-score {
        background: linear-gradient(45deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 1.1em;
    }
    
    .info-message {
        text-align: center;
        padding: 30px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        color: white;
        font-size: 1.1em;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    .warning-message {
        text-align: center;
        padding: 25px;
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        border-radius: 15px;
        color: #721c24;
        font-size: 1.1em;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    .success-header {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)
    
    if 'selected_product' in st.session_state and 'top_n' in st.session_state:
        selected_product = st.session_state['selected_product']
        top_n = st.session_state['top_n']

        rekomendasi, skor = get_recommendations(selected_product, df, similarity_matrix, top_n=top_n)

        if rekomendasi is not None and not rekomendasi.empty:
            # Success message dengan styling
            st.markdown(f"""
            <div class="success-header">
                <h3 style="margin: 0; color: #2c3e50;">
                    🎉 Berikut {top_n} produk yang mirip dengan <em>{selected_product}</em>:
                </h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Menampilkan rekomendasi dengan card design
            for i, row in rekomendasi.iterrows():
                rating = row.get('Rating')
                if pd.isna(rating) or rating == '':
                    rating_display = "No Rating"
                    rating_color = "#95a5a6"
                else:
                    rating_display = f"{rating:.1f} ⭐"
                    rating_color = "#f39c12"

                # Ambil skor kemiripan
                similarity_score = skor[i] if i < len(skor) else 0
                similarity_percentage = similarity_score * 100  # Convert to percentage

                st.markdown(f"""
                <div class="product-card">
                    <div class="product-title">
                        {i+1}. {row['Product Name'].title()}
                    </div>
                    <div class="product-info">
                        <div class="info-item">
                            <span class="info-icon">🏷️</span>
                            <strong>Merek:</strong> &nbsp;{row['Brand'].title()}
                        </div>
                        <div class="info-item">
                            <span class="info-icon">📦</span>
                            <strong>Kategori:</strong> &nbsp;{row['Category']}
                        </div>
                        <div class="info-item">
                            <span class="info-icon">💧</span>
                            <strong>Bahan Utama:</strong> &nbsp;{row['Main Ingredients']}
                        </div>
                        <div class="info-item">
                            <span class="info-icon">💰</span>
                            <strong>Harga:</strong> &nbsp;<span class="price-highlight">${row['Price ($)']}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-icon">⭐</span>
                            <strong>Rating:</strong> &nbsp;<span class="rating-stars" style="color: {rating_color};">{rating_display}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-icon">🎯</span>
                            <strong>Skor Kemiripan:</strong> &nbsp;<span class="similarity-score">{similarity_score:.3f} ({similarity_percentage:.1f}%)</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="warning-message">
                <h3>⚠️ Oops!</h3>
                <p>Produk tidak ditemukan atau tidak cukup data untuk rekomendasi.</p>
                <p>Silakan coba dengan produk lain atau periksa kembali pilihan Anda.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="info-message">
            <h3>📝 Langkah Selanjutnya</h3>
            <p>Silakan pilih produk dan preferensi terlebih dahulu di halaman <strong>Preference</strong>.</p>
            <p>Setelah itu, Anda dapat melihat rekomendasi produk skincare yang sesuai dengan kebutuhan Anda!</p>
        </div>
        """, unsafe_allow_html=True)