import streamlit as st

def app():
    # Custom CSS untuk styling modern dan stabil
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
    }
    
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-top: 1rem;
    }
    
    .welcome-card {
        background: white;
        padding: 2.5rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid #e9ecef;
        margin: 2rem 0;
        text-align: center;
    }
    
    .welcome-text {
        font-size: 1.3rem;
        line-height: 1.6;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 1px solid #e9ecef;
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        color: #667eea;
    }
    
    .feature-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.8rem;
    }
    
    .feature-desc {
        color: #64748b;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    .cta-section {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(79, 172, 254, 0.3);
    }
    
    .cta-text {
        font-size: 1.6rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .navigation-hint {
        background: linear-gradient(145deg, #fff3cd, #ffeaa7);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #f59e0b;
        margin: 2rem 0;
    }
    
    .hint-text {
        color: #92400e;
        font-weight: 500;
        font-size: 1.1rem;
        margin: 0;
    }
    
    .separator {
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 2px;
        margin: 2rem 0;
        opacity: 0.7;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        .main-subtitle {
            font-size: 1rem;
        }
        .welcome-text {
            font-size: 1.1rem;
        }
        .feature-icon {
            font-size: 3rem;
        }
        .cta-text {
            font-size: 1.4rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header utama
    st.markdown("""
    <div class="main-header">
        <div class="main-title">🧴 Sistem Rekomendasi Produk Skincare</div>
        <div class="main-subtitle">Temukan produk skincare yang tepat untuk kulit Anda</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Welcome section
    st.markdown("""
    <div class="welcome-card">
        <div class="welcome-text">
            Selamat datang di sistem rekomendasi produk skincare.<br><br>
            Gunakan sistem ini untuk mendapatkan rekomendasi produk skincare yang sesuai dengan preferensi Anda.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Separator
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)
    
    # Feature cards menggunakan Streamlit columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Rekomendasi Personal</div>
            <div class="feature-desc">Dapatkan rekomendasi produk yang disesuaikan dengan jenis kulit dan kebutuhan spesifik Anda</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <div class="feature-title">Analisis Mendalam</div>
            <div class="feature-desc">Sistem cerdas yang menganalisis preferensi dan memberikan hasil rekomendasi terbaik</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💡</div>
            <div class="feature-title">Mudah Digunakan</div>
            <div class="feature-desc">Interface yang intuitif dan mudah digunakan untuk semua kalangan pengguna</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("""
    <div class="cta-section">
        <div class="cta-text">Mulai perjalanan skincare Anda sekarang!</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation hint
    st.markdown("""
    <div class="navigation-hint">
        <p class="hint-text">
            💡 Navigasi menggunakan menu di samping untuk mulai menggunakan fitur-fitur aplikasi
        </p>
    </div>
    """, unsafe_allow_html=True)