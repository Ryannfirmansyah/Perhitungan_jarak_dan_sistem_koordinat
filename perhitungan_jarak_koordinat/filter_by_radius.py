#(points, center_point, radius): Fungsi untuk menyaring wilayah berdasarkan radius tertentu.
#FERA

def saring_wilayah_dalam_radius(koordinat_titik_pusat, daftar_titik, radius):
    hasil = []
    x_pusat, y_pusat = koordinat_titik_pusat

    for (x, y) in daftar_titik:
        jarak = ((x - x_pusat) ** 2 + (y - y_pusat) ** 2) ** 0.5
        if jarak <= radius:
            hasil.append((x, y))

    return hasil