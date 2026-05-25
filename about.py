import streamlit as st

def app():
    # Custom CSS yang lebih sederhana dan kompatibel
    st.markdown("""
    <style>
    /* Card Styling */
    .info-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        color: white;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .white-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid #e0e0e0;
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #2c3e50;
    }
    
    .gradient-title {
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .feature-item {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        margin-bottom: 0.8rem;
        border-radius: 8px;
        border-left: 4px solid #ffd700;
    }
    
    .stat-box {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: white;
        display: block;
    }
    
    .stat-label {
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    .developer-section {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        border-radius: 15px;
        padding: 2rem;
        color: white;
        text-align: center;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header Section
    st.markdown("""
    <div class="main-header">
        <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">🌟 Skincare Recommendation System</h1>
        <p style="font-size: 1.2rem; opacity: 0.9;">Sistem Rekomendasi Produk Skincare Berbasis AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Statistics Section dalam satu card
    st.markdown("""
    <div class="info-card">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
            <div class="stat-box">
                <span class="stat-number">8K+</span>
                <div class="stat-label">Produk Skincare</div>
            </div>
            <div class="stat-box">
                <span class="stat-number">99%</span>
                <div class="stat-label">Akurasi Rekomendasi</div>
            </div>
            <div class="stat-box">
                <span class="stat-number">AI</span>
                <div class="stat-label">Powered Technology</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # About Application Section
    st.markdown("""
    <div class="white-card">
        <h2 class="card-title">🎯 Tentang Aplikasi</h2>
        <p style="font-size: 1rem; line-height: 1.6; color: #34495e;">
            Aplikasi ini merupakan sistem rekomendasi produk skincare yang canggih, dibangun menggunakan 
            <strong>Streamlit</strong> sebagai framework web dan menerapkan algoritma <strong>Item-Based Collaborative Filtering</strong> 
            dengan metrik <strong>Cosine Similarity</strong> untuk menghasilkan rekomendasi yang akurat dan personal.
            <br><br>
            Dataset yang kami gunakan mencakup lebih dari <strong>8.000 produk skincare</strong> dari berbagai brand 
            ternama dengan atribut lengkap meliputi nama produk, merek, kategori, ingrediens utama, dan rentang harga.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown("""
    <div class="info-card">
        <h2 class="gradient-title">✨ Fitur Unggulan</h2>
        <div class="feature-item">
            <strong>🔍 Pencarian Intelligent:</strong> Temukan produk skincare dengan mudah berdasarkan nama, brand, atau kategori
        </div>
        <div class="feature-item">
            <strong>🎯 Rekomendasi Personal:</strong> Algoritma AI memberikan rekomendasi yang disesuaikan dengan preferensi Anda
        </div>
        <div class="feature-item">
            <strong>📊 Analisis Similarity:</strong> Menggunakan Cosine Similarity untuk mengukur kemiripan antar produk
        </div>
        <div class="feature-item">
            <strong>💰 Filter Harga:</strong> Temukan produk sesuai dengan budget Anda
        </div>
        <div class="feature-item">
            <strong>📱 Responsive Design:</strong> Tampilan yang optimal di semua perangkat
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Technology Section
    st.markdown("""
    <div class="white-card">
        <h2 class="card-title">⚙️ Teknologi yang Digunakan</h2>
        <p style="font-size: 1rem; line-height: 1.6; color: #34495e;">
            Aplikasi ini dibangun dengan teknologi modern dan terdepan:
            <br><br>
            <strong>🐍 Python:</strong> Bahasa pemrograman utama untuk pengembangan algoritma<br>
            <strong>🌊 Streamlit:</strong> Framework untuk membangun aplikasi web interaktif<br>
            <strong>🧮 Pandas & NumPy:</strong> Library untuk manipulasi dan analisis data<br>
            <strong>📈 Scikit-learn:</strong> Framework machine learning untuk implementasi algoritma<br>
            <strong>🎨 CSS3:</strong> Styling modern untuk tampilan yang menarik
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Developer Section
    st.markdown("""
    <div class="developer-section">
        <h2 style="font-size: 1.8rem; margin-bottom: 1rem;">👨‍💻 Mohamad Fiqih Aldiyanto</h2>
        <div style="font-size: 1.1rem; line-height: 1.6;">
            <strong>NIM:</strong> 2110651015<br>
            <strong>Program Studi:</strong> Teknik Informatika<br>
            <strong>Universitas:</strong> Universitas Muhammadiyah Jember<br><br>
            <em>"Mengembangkan solusi teknologi untuk membantu orang menemukan produk skincare yang tepat"</em>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9rem; padding: 1rem;">
        © 2025 Skincare Recommendation System. Dibuat dengan ❤️ menggunakan Streamlit
    </div>
    """, unsafe_allow_html=True)