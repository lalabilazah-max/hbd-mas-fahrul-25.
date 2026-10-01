import streamlit as st
import time

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="HBD Mas Fahrul Fauzi 🎂",
    page_icon="🎂",
    layout="centered"
)

# =========================
# CSS TAMPILAN
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #ffe4ec, #fff5f8, #ffd6e5);
}

.main {
    max-width: 700px;
}

.judul {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #d63384;
    margin-top: 20px;
}

.nama {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #8f245d;
}

.umur {
    text-align: center;
    font-size: 25px;
    color: #555;
}

.kartu {
    background: rgba(255,255,255,0.85);
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    margin-top: 20px;
    margin-bottom: 20px;
}

.ucapan {
    font-size: 18px;
    line-height: 1.8;
    color: #333;
    text-align: center;
}

.emoji {
    text-align: center;
    font-size: 45px;
}

.footer {
    text-align: center;
    color: #888;
    margin-top: 30px;
    font-size: 14px;
}

div.stButton > button {
    width: 100%;
    border-radius: 20px;
    height: 55px;
    font-size: 18px;
    font-weight: bold;
    background-color: #d63384;
    color: white;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# =========================
# JUDUL
# =========================
st.markdown(
    '<div class="judul">🎂 HAPPY BIRTHDAY 🎂</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="nama">Mas Fahrul Fauzi</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="umur">✨ 25 Tahun ✨</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="emoji">🎈 🎁 🥳 💗 🎉</div>',
    unsafe_allow_html=True
)

# =========================
# UCAPAN
# =========================
st.markdown("""
<div class="kartu">
<div class="ucapan">

Hari ini bukan hari biasa... 🤍<br>
Karena hari ini seseorang yang spesial sedang bertambah usia.

<br><br>

🎉 <b>Selamat ulang tahun yang ke-25, Mas Fahrul Fauzi!</b> 🎉

<br><br>

Semoga di umur yang baru ini,
semua hal baik yang sedang diperjuangkan
bisa satu per satu menjadi kenyataan.

Semoga selalu diberikan kesehatan,
dilancarkan rezekinya,
dipermudah segala urusannya,
dan dikelilingi orang-orang yang tulus menyayangi.

<br><br>

Kalau tahun-tahun sebelumnya sudah banyak cerita,
semoga di umur 25 ini
ada lebih banyak cerita indah yang bisa dibuat. ✨

<br><br>

Tetap jadi Mas Fahrul yang baik,
yang kuat menghadapi semuanya,
dan jangan lupa bahagia. 🤍

<br><br>

<b>25 tahun bukan tentang semakin tua...</b><br>
tapi tentang semakin dekat dengan semua impian
yang ingin diwujudkan. 🌷

</div>
</div>
""", unsafe_allow_html=True)

# =========================
# TOMBOL KEJUTAN
# =========================
st.markdown(
    '<div class="emoji">🎁</div>',
    unsafe_allow_html=True
)

if st.button("💌 BUKA UCAPAN RAHASIA"):

    with st.spinner("Sebentar... ada sesuatu untuk Mas Fahrul 🤭"):
        time.sleep(2)

    st.balloons()

    st.markdown("""
    <div class="kartu">
    <div class="ucapan">

    💗 <b>Pesan kecil untuk Mas Fahrul</b> 💗

    <br><br>

    Di antara banyaknya orang yang ada di dunia ini,
    semoga Mas Fahrul selalu bertemu dengan orang-orang
    yang bisa menghargai, menjaga, dan menyayangi
    Mas Fahrul dengan tulus.

    <br><br>

    Jangan terlalu keras sama diri sendiri ya.
    Kalau capek, istirahat.
    Kalau sedih, nggak apa-apa.
    Kalau gagal, coba lagi.

    <br><br>

    Karena perjalanan hidup masih panjang.
    Masih banyak tempat yang belum didatangi,
    makanan yang belum dicoba,
    cerita yang belum dibuat,
    dan mimpi yang belum tercapai. ✨

    <br><br>

    Jadi...

    <br><br>

    <b>Selamat datang di usia 25 tahun! 🥳</b>

    <br><br>

    Semoga tahun ini menjadi salah satu
    tahun terbaik dalam hidup Mas Fahrul. 🤍

    <br><br>

    🎂 Happy Birthday, Mas Fahrul Fauzi! 🎂

    </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# PESAN TERAKHIR
# =========================
st.markdown("""
<div class="footer">
Made with 💗 specifically for Mas Fahrul Fauzi<br>
25th Birthday Celebration 🎂
</div>
""", unsafe_allow_html=True)