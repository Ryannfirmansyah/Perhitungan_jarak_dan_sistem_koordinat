# (points, reference_point): Fungsi untuk mencari titik terdekat dari kumpulan titik.
#ANGEL

def cari_rute_terdekat(titik_awal, titik_akhir, lokasi):
    # Membuat dictionary untuk menyimpan lokasi dan jaraknya
    jarak = {
        'Jakarta': {'Bandung': 150, 'Surabaya': 700},
        'Bandung': {'Jakarta': 150, 'Surabaya': 550},
        'Surabaya': {'Jakarta': 700, 'Bandung': 550}
    }

    # Mencari rute terdekat antara dua titik lokasi
    rute_terdekat = min(jarak[titik_awal], key=jarak[titik_awal].get)

    # Kembalikan rute terdekat
    return rute_terdekat

