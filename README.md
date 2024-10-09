# Perhitungan_jarak_dan_sistem_koordinat

Perhitungan_jarak_dan_sistem_koordinat adalah sebuah package Python yang dirancang untuk membantu Programer melakukan perhitungan jarak dan sistem koordinat dan berbagai fitur lainnya.

## Fitur

1. Fungsi untuk Menghitung Jarak Tengah Antar Koordinat
2. ⁠⁠Fungsi untuk Mengubah Derajat ke Radian
3. ⁠Fungsi untuk Menghitung jarak ke titik pusat
4. ⁠Fungsi untung Menghitung estimasi waktu
5. ⁠Fungsi Menyaring Wilayah Berdasarkan Radius Tertentu
6. ⁠Fungsi Mencari Titik Terdekat
7. ⁠Fungsi Menentukan Jarak Total untuk Beberapa Titik
5. Fungsi Mengubah satuan jarak

## Instalasi

Untuk menginstal package ini, Anda dapat menggunakan `pip`:

```bash
pip install Perhitungan_jarak_dan_sistem_koordinat
```
CONTOH PENGGUNAAN PACKAGE
```bash

#1. Fungsi untuk Menghitung Jarak Tengah Antar Koordinat
# Koordinat Makassar dan Jakarta
lat_makassar = -5.147665
lon_makassar = 119.432731
lat_jakarta = -6.208763
lon_jakarta = 106.845599
# Memanggil fungsi hitung_midpoint
mid_lat, mid_lon = midpoint(lat_makassar, lon_makassar, lat_jakarta, lon_jakarta)
print(f"Titik tengah antara Makassar dan Jakarta adalah: {mid_lat}, {mid_lon}")


#2. ⁠⁠Fungsi untuk Mengubah Derajat ke Radian
from perhitungan_jarak_koordinat.degrees_to_radians import drjt_rd
hasil = drjt_rd(90, 0)
print(hasil)


#3. ⁠Fungsi untuk Menghitung jarak ke titik pusat
from perhitungan_jarak_koordinat.distance_to_center import distance
# Koordinat Unhas Tamalanrea
lat_unhas = -5.1333128
lon_unhas = 119.4884481
# Koordinat Unhas Gowa
lat_unhas_gowa = -5.23026
lon_unhas_gowa = 119.4995591
# Menghitung jarak menggunakan fungsi distance
jarak = distance(lat_unhas, lon_unhas, lat_unhas_gowa, lon_unhas_gowa)
print(f"Jarak dari unhas ke unhas_gowa adalah {jarak:.1f} km")

#4. ⁠Fungsi untung Menghitung estimasi waktu
from estimate_travel_time import e2t

#Input jarak dan kecepatan
jarak = 120  # kilometer
kecepatan = 60  # kilometer per jam
waktu_tempuh = e2t(jarak, kecepatan)
print(f"Waktu tempuh untuk jarak {jarak} km dengan kecepatan {kecepatan} km/jam adalah: {waktu_tempuh}")

#5. ⁠Fungsi Menyaring Wilayah Berdasarkan Radius Tertentu
from perhitungan_jarak_koordinat.filter_by_radius import saring_radius, filtered
# Daftar lokasi dengan nama kota dan koordinat (latitude, longitude)
locations = {
    "Surabaya": (-7.250445, 112.768845),
    "Medan": (3.595196, 98.672226),
    "Makassar": (-5.147665, 119.432732),
    "Bandung": (-6.917464, 107.619123),
    "Banjarmasin": (-3.316694, 114.590111)
}
# Titik pusat Jakarta dan radius 1000 km
center_lat = -6.208763
center_lon = 106.845599
radius = 1000  # dalam kilometer
# Memanggil fungsi untuk menyaring lokasi
hasil_filter = filtered(locations, center_lat, center_lon, radius)
# Output hasil filter
print("Kota dalam radius", radius, "km dari Jakarta:")
for kota in hasil_filter:
    print(kota)


#6. ⁠Fungsi Mencari Titik Terdekat
from perhitungan_jarak_koordinat.find_nearest_poins import titik_terdekat
titik_pusat = (140.705001, -4.568315)  # Jayapura
kumpulan_titik = [
    ("Sorong", (140.366211, -3.721235)),  # Sorong
    ("Manokwari", (137.166722, -4.043775)),  # Manokwari
    ("Timika", (138.174971, -3.830016))   # Timika
]
titik_terdekat = titik_terdekat(titik_pusat, kumpulan_titik)
print(f"Titik terdekat dari Jayapura adalah {titik_terdekat[0]} dengan koordinat {titik_terdekat[1]}")


#7. ⁠Fungsi Menentukan Jarak Total untuk Beberapa Titik
from perhitungan_jarak_koordinat.calculate_total_distance import jarak_total
# Daftar titik yang ingin dihitung jaraknya
titik_input = [(1, 2),  # Gowa (rumah)
               (4, 6),  # Makassar
               (7, 3),  # Maros
               (1, 2)]  # Kembali ke Gowa
# Memanggil fungsi dan menyimpan total jarak
total_jarak = jarak_total(titik_input)
# Mencetak total jarak
print("Total jarak dari Gowa ke Makassar, Maros, dan kembali ke Gowa adalah:", total_jarak)


#8. Fungsi Mengubah satuan jarak
from perhitungan_jarak_koordinat.km_to_m import konv_m
hasil_km = konv_m(5, "km")
print(f"5 meter dalam kilometer: {hasil_km} km")

```
Kontribusi
Kami sangat menyambut kontribusi dari komunitas open source. Berikut adalah langkah-langkah untuk berkontribusi:

1. Fork repositori ini.
2. Clone repositori ke mesin lokal Anda.
3. Buat branch baru:
```bash
git checkout -b fitur-baru
```
4. Lakukan perubahan dan commit:
```bash
git commit -m "Menambahkan fitur baru"
```
5. Push branch ke GitHub:
```bash
git push origin fitur-baru


