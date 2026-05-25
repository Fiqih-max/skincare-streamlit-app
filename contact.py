import streamlit as st

def app():
    st.title("📬 Kontak Kami")
    st.markdown("""
    Jika Anda memiliki pertanyaan, saran, atau ingin berkolaborasi, silakan hubungi kami melalui formulir di bawah ini.
    """)

    with st.form(key='contact_form'):
        name = st.text_input("Nama")
        email = st.text_input("Email")
        message = st.text_area("Pesan")

        submit_button = st.form_submit_button(label='Kirim')

    if submit_button:
        if not name or not email or not message:
            st.error("Mohon isi semua kolom.")
        else:
            st.success("Terima kasih sudah menghubungi kami! Kami akan membalas secepatnya.")
