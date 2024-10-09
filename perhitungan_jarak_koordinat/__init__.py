<<<<<<< HEAD
=======

from calculate_distance import hitung_jarak_koordinat

# Koordinat titik pertama (x1, y1)
x1, y1 = 3, 4

# Koordinat titik kedua (x2, y2)
x2, y2 = 7, 1

# Panggil fungsi untuk menghitung jarak
jarak = hitung_jarak_koordinat(x1, y1, x2, y2)

# Tampilkan hasil
print(f"Jarak antara titik ({x1}, {y1}) dan ({x2}, {y2}) adalah {jarak} satuan.")

from filter_by_radius import saring_wilayah_dalam_radius

# Titik pusat
koordinat_pusat = (5, 5)

# Daftar titik yang akan disaring
daftar_titik = [(3, 4), (7, 8), (5, 3), (10, 10), (4, 4)]

# Radius (misalnya 3 satuan)
radius = 3

# Panggil fungsi untuk menyaring titik dalam radius tertentu
titik_dalam_radius = saring_wilayah_dalam_radius(koordinat_pusat, daftar_titik, radius)

# Tampilkan hasil
print(f"Titik-titik yang berada dalam radius {radius} dari {koordinat_pusat}: {titik_dalam_radius}")
>>>>>>> H071241090
