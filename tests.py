# Contoh 
from perhitungan_jarak_koordinat import cari_rute_terdekat

# Contoh penggunaan fungsi
lokasi = ['Jakarta', 'Bandung', 'Surabaya']
titik_awal = 'Jakarta'
titik_akhir = 'Bandung'
rute_terdekat = cari_rute_terdekat(titik_awal, titik_akhir, lokasi)
print(f"Rute terdekat dari {titik_awal} ke {titik_akhir} adalah {rute_terdekat}")

