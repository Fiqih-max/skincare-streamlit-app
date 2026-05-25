import streamlit as st

def app(df):
    # Header dengan styling
    st.markdown("""
    <div style='text-align: center; padding: 20px; background: linear-gradient(90deg, #667eea, #764ba2); 
                border-radius: 10px; margin-bottom: 30px;'>
        <h1 style='color: white; font-size: 2.5em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
            📝 Pilih Preferensi Produk Skincare
        </h1>
        <p style='color: white; font-size: 1.1em; margin: 10px 0 0 0; opacity: 0.9;'>
            Personalisasi rekomendasi skincare sesuai kebutuhan Anda
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom CSS untuk styling
    st.markdown("""
    <style>
    .preference-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .preference-section {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        border-left: 4px solid #667eea;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .section-title {
        color: #2c3e50;
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .success-message {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        color: #2c3e50;
        font-weight: bold;
    }
    
    .search-button {
        background: linear-gradient(45deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 30px !important;
        font-size: 1.1em !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
        margin: 20px 0 !important;
    }
    
    .search-button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
    }
    
    /* Custom styling untuk selectbox dan slider */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 8px;
        border: 2px solid rgba(102, 126, 234, 0.3);
    }
    
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #667eea, #764ba2);
    }
    
    /* Instruction box */
    .instruction-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        border-left: 4px solid #f39c12;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .instruction-title {
        color: #d35400;
        font-size: 1.1em;
        font-weight: bold;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .instruction-text {
        color: #8b4513;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Container utama
    st.markdown('<div class="preference-container">', unsafe_allow_html=True)
    
    # Instruction box
    st.markdown("""
    <div class="instruction-box">
        <div class="instruction-title">
            💡 Cara Menggunakan
        </div>
        <div class="instruction-text">
            1. Pilih produk skincare yang ingin Anda jadikan referensi<br>
            2. Tentukan berapa banyak rekomendasi yang diinginkan<br>
            3. Klik tombol "Cari Rekomendasi" untuk menyimpan preferensi<br>
            4. Buka halaman "Recommendation Result" untuk melihat hasil
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Section untuk pemilihan produk
    st.markdown("""
    <div class="preference-section">
        <div class="section-title">
            📌 Pilihan Produk Referensi
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    product_list = df['Product Name'].unique().tolist()
    selected_product = st.selectbox("📌 Pilih Produk Skincare untuk rekomendasi:", product_list)

    # Section untuk jumlah rekomendasi
    st.markdown("""
    <div class="preference-section">
        <div class="section-title">
            🔢 Jumlah Rekomendasi
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    top_n = st.slider("Jumlah rekomendasi yang diinginkan 1 - 10 :", min_value=1, max_value=10, value=5)

    # Tombol pencarian dengan styling
    st.markdown('<div style="text-align: center; margin: 30px 0;">', unsafe_allow_html=True)
    
    if st.button("🔍 Cari Rekomendasi"):
        st.session_state['selected_product'] = selected_product
        st.session_state['top_n'] = top_n
        
        # Success message dengan styling
        st.markdown(f"""
        <div class="success-message">
            <h3 style="margin: 0 0 10px 0;">✅ Preferensi Berhasil Tersimpan!</h3>
            <p style="margin: 0; font-size: 1.1em;">
                Produk: <strong>{selected_product}</strong><br>
                Jumlah Rekomendasi: <strong>{top_n} produk</strong>
            </p>
            <p style="margin: 15px 0 0 0; font-size: 1.0em; opacity: 0.8;">
                Pergi ke halaman <em>Recommendation Result</em> untuk melihat rekomendasi
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)