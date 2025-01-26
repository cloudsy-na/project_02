import requests
import pandas as pd

# URL endpoint
url = "https://sirup.lkpp.go.id/sirup/caripaketctr/search"

# Payload untuk filtering
payload = {
    "tahunAnggaran": "2024",
    "lokasi": "14956",  # ID lokasi
    "start": 0,         # Offset awal
    "length": 25000,       # Jumlah data per halaman
    "order[0][column]": 5,  # Urutan berdasarkan kolom 5
    "order[0][dir]": "DESC",  # Arah pengurutan DESC
    "search[value]": "",     # Pencarian global (kosongkan jika tidak perlu)
    "search[regex]": "false",
}

# Header (opsional, sesuaikan dengan kebutuhan)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
}

# Kirim permintaan POST
response = requests.post(url, data=payload, headers=headers)

# Periksa status respons
if response.status_code == 200:
    data = response.json()  # Parsing JSON
    df = pd.DataFrame(data)
    # print(df)  # Cetak data hasil crawling
else:
    print(f"Error: {response.status_code}")

# Ekstrak kolom ketiga (berisi dictionary) dan ubah menjadi DataFrame baru
df_extracted = pd.json_normalize(df["data"])

# Pilih kolom yang diinginkan
df_filtered = df_extracted[['lokasi', 'paket','pagu','jenisPengadaan','metode','pemilihan','kldi','satuanKerja']]

# Tampilkan DataFrame hasil
print(df_filtered)

df_filtered.to_excel("result_14956.xlsx")
