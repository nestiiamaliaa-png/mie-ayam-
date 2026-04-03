import streamlit as st
import matplotlib.pyplot as plt

# CONFIG
st.set_page_config(page_title="Virtual Lab Mie Ayam", page_icon="🍜")

st.title("🍜 Berapa Kalori Mie Ayam yang Kamu Makan Hari Ini?")
st.markdown("### Eksplorasi kalori menggunakan konsep integral dalam kehidupan nyata ✨")

st.write("---")

# =========================
# INPUT DASAR
# =========================
porsi = st.number_input("🍽️ Jumlah mangkok/porsi", 1, 10, 1)

mie_gram = st.selectbox(
    "🍜 Jumlah mie (gram)",
    ["100 gr", "200 gr", "300 gr", "400 gr", "500 gr atau lebih"]
)

minyak = st.selectbox(
    "🛢️ Minyak bawang (sdm)",
    ["0.5", "1", "2", "3", "lebih dari 3"]
)

# =========================
# SAYUR
# =========================
st.subheader("🥬 Sayuran")

sawi = st.selectbox("Jumlah sawi (lembar)", ["1", "2", "3", "lebih"])
daun_bawang = st.selectbox("Daun bawang (sdm)", ["0.5", "1", "2", "3", "lebih"])

# =========================
# AYAM
# =========================
st.subheader("🍗 Ayam")

ayam = st.selectbox("Ayam cincang (sdm)", ["1", "2", "3", "4", "5", "lebih"])

# =========================
# TOPPING
# =========================
st.subheader("🍢 Topping")

def input_topping(nama):
    pakai = st.radio(f"{nama}?", ["Tidak", "Ya"], horizontal=True)
    jumlah = 0
    if pakai == "Ya":
        jumlah = st.selectbox(f"Jumlah {nama}", ["1", "2", "3", "lebih"])
    return jumlah

ceker = input_topping("Ceker 🍗")
bakso = input_topping("Bakso 🧆")
telur = input_topping("Telur (ayam/puyuh) 🥚")

krupuk = st.radio("Krupuk pangsit?", ["Tidak", "Ya"], horizontal=True)
krupuk_jumlah = 0
if krupuk == "Ya":
    krupuk_jumlah = st.selectbox("Krupuk (sdm)", ["1", "2", "3", "lebih"])

bawang_goreng = st.radio("Bawang goreng?", ["Tidak", "Ya"], horizontal=True)
bawang_jumlah = 0
if bawang_goreng == "Ya":
    bawang_jumlah = st.selectbox("Bawang goreng (sdm)", ["1", "2", "3", "lebih"])

# =========================
# SAOS
# =========================
st.subheader("🌶️ Saos")

def input_saos(nama):
    pakai = st.radio(f"{nama}?", ["Tidak", "Ya"], horizontal=True)
    jumlah = 0
    if pakai == "Ya":
        jumlah = st.selectbox(f"{nama} (sdm)", ["0.5", "1", "2", "3", "4", "5", "lebih"])
    return jumlah

sambal = input_saos("Sambal")
kecap = input_saos("Kecap")
saos_tomat = input_saos("Saos tomat")

# =========================
# KONVERSI NILAI
# =========================
def konversi(x):
    if x == "lebih": return 4
    if x == "lebih dari 3": return 4
    return float(x)

# =========================
# DATA KALORI
# =========================
kalori = {
    "mie": 1.5,  # per gram
    "minyak": 120,  # per sdm
    "sawi": 5,
    "daun_bawang": 3,
    "ayam": 50,
    "ceker": 150,
    "bakso": 80,
    "telur": 70,
    "krupuk": 120,
    "bawang": 50,
    "sambal": 20,
    "kecap": 40,
    "saos": 30
}

# =========================
# PERHITUNGAN
# =========================
total = 0
detail = {}

# mie
mie_val = int(mie_gram.split()[0]) if "lebih" not in mie_gram else 500
detail["Mie"] = mie_val * kalori["mie"]

# lainnya
detail["Minyak"] = konversi(minyak) * kalori["minyak"]
detail["Sawi"] = konversi(sawi) * kalori["sawi"]
detail["Daun bawang"] = konversi(daun_bawang) * kalori["daun_bawang"]
detail["Ayam"] = konversi(ayam) * kalori["ayam"]

detail["Ceker"] = konversi(ceker) * kalori["ceker"]
detail["Bakso"] = konversi(bakso) * kalori["bakso"]
detail["Telur"] = konversi(telur) * kalori["telur"]
detail["Krupuk"] = konversi(krupuk_jumlah) * kalori["krupuk"]
detail["Bawang goreng"] = konversi(bawang_jumlah) * kalori["bawang"]

detail["Sambal"] = konversi(sambal) * kalori["sambal"]
detail["Kecap"] = konversi(kecap) * kalori["kecap"]
detail["Saos"] = konversi(saos_tomat) * kalori["saos"]

total = sum(detail.values()) * porsi

# =========================
# OUTPUT
# =========================
st.write("---")
st.subheader("🔥 Total Kalori")
st.success(f"{int(total)} kkal")

# kategori
if total < 400:
    st.success("🟢 Rendah kalori - aman untuk diet ringan")
elif total < 800:
    st.warning("🟡 Kalori sedang - masih aman tapi perlu kontrol")
else:
    st.error("🔴 Tinggi kalori - sebaiknya dikurangi 😅")

# =========================
# REKOMENDASI
# =========================
st.subheader("💡 Rekomendasi")

if total > 800:
    st.write("👉 Kurangi minyak, krupuk, dan topping tinggi lemak")
elif total < 400:
    st.write("👉 Bisa ditambah protein agar lebih seimbang")
else:
    st.write("👉 Komposisi sudah cukup seimbang 👍")

# =========================
# GRAFIK
# =========================
st.subheader("📊 Distribusi Kalori")

fig, ax = plt.subplots()
ax.pie(detail.values(), labels=detail.keys(), autopct='%1.1f%%')
st.pyplot(fig)

# =========================
# PENJELASAN INTEGRAL
# =========================
st.write("---")
st.subheader("📘 Penjelasan Matematis (Integral)")

st.markdown(f"""
Total kalori dihitung menggunakan pendekatan integral:

K_total = ∫ k(x) dx ≈ Σ k_i

Dimana setiap komponen makanan dianggap sebagai elemen kecil 
yang menyumbang energi.

Contoh dari input kamu:

- Mie: {detail["Mie"]:.1f} kkal  
- Minyak: {detail["Minyak"]:.1f} kkal  
- Ayam: {detail["Ayam"]:.1f} kkal  

Total = {int(total)} kkal

👉 Ini menunjukkan bahwa integral dalam kehidupan nyata bisa digunakan 
untuk menjumlahkan kontribusi energi dari berbagai komponen makanan.
""")

st.write("---")
st.caption("✨ Virtual Lab Matematika - Kelompokmu auto dilirik dosen 😎🔥")
