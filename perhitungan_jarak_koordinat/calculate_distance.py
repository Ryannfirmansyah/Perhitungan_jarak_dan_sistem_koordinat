#Fungsi untuk menghitung jarak antar koordinat.
#FERA

def hitung_jarak_koordinat(x1, y1, x2, y2):
    jarak = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # akar dari penjumlahan kuadrat selisih koordinat
    return jarak
