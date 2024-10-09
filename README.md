
# Perhitungan_jarak_dan_sistem_koordinat

`Perhitungan_jarak_dan_sistem_koordinat` adalah sebuah package Python yang dirancang untuk membantu programmer melakukan perhitungan jarak dan sistem koordinat, serta berbagai fitur terkait lainnya.

## Fitur

- **Fungsi untuk Menghitung Jarak Tengah Antar Koordinat**
- **Fungsi untuk Mengubah Derajat ke Radian**
- **Fungsi untuk Menghitung Jarak ke Titik Pusat**
- **Fungsi untuk Menghitung Estimasi Waktu**
- **Fungsi Menyaring Wilayah Berdasarkan Radius Tertentu**
- **Fungsi Mencari Titik Terdekat**
- **Fungsi Menentukan Jarak Total untuk Beberapa Titik**
- **Fungsi Mengubah Satuan Jarak**

## Instalasi

Untuk menginstal package ini, Anda dapat menggunakan pip:

```bash
pip install Perhitungan_jarak_dan_sistem_koordinat
```

## Contoh Penggunaan Package

### 1. Fungsi midpoint

Fungsi ini menghitung titik tengah antara dua koordinat (latitude dan longitude).

```python
# Koordinat Makassar dan Jakarta
lat_makassar = -5.147665
lon_makassar = 119.432731
lat_jakarta = -6.208763
lon_jakarta = 106.845599

# Memanggil fungsi hitung_midpoint
mid_lat, mid_lon = midpoint(lat_makassar, lon_makassar, lat_jakarta, lon_jakarta)
print(f"Titik tengah antara Makassar dan Jakarta adalah: {mid_lat}, {mid_lon}")
```

### 2. Fungsi drjt_rd

Fungsi ini mengonversi nilai dalam derajat ke radian, yang sering diperlukan dalam perhitungan trigonometri.

```python
from perhitungan_jarak_dan_sistem_koordinat.degrees_to_radians import drjt_rd

hasil = drjt_rd(90, 0)
print(hasil)  # Output: 1.5708
```

### 3. Fungsi distance

Fungsi ini menghitung jarak antara dua titik berdasarkan koordinat latitude dan longitude mereka.

```python
from perhitungan_jarak_dan_sistem_koordinat.distance_to_center import distance

# Koordinat Unhas Tamalanrea
lat_unhas = -5.1333128
lon_unhas = 119.4884481
# Koordinat Unhas Gowa
lat_unhas_gowa = -5.23026
lon_unhas_gowa = 119.4995591

# Menghitung jarak menggunakan fungsi distance
jarak = distance(lat_unhas, lon_unhas, lat_unhas_gowa, lon_unhas_gowa)
print(f"Jarak dari Unhas ke Unhas Gowa adalah {jarak:.1f} km")
```

### 4. Fungsi e2t

Fungsi ini memperkirakan waktu tempuh berdasarkan jarak dan kecepatan yang diberikan.

```python
from perhitungan_jarak_dan_sistem_koordinat.estimate_travel_time import e2t

# Input jarak dan kecepatan
jarak = 120  # kilometer
kecepatan = 60  # kilometer per jam
waktu_tempuh = e2t(jarak, kecepatan)
print(f"Waktu tempuh untuk jarak {jarak} km dengan kecepatan {kecepatan} km/jam adalah: {waktu_tempuh}")
```

### 5. Fungsi saring_radius

Fungsi ini menyaring lokasi-lokasi yang berada dalam radius tertentu dari titik pusat yang diberikan.

```python
from perhitungan_jarak_dan_sistem_koordinat.filter_by_radius import saring_radius, filtered

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
```

### 6. Fungsi titik_terdekat

Fungsi ini menemukan titik terdekat dari titik pusat yang diberikan dari kumpulan titik yang tersedia.

```python
from perhitungan_jarak_dan_sistem_koordinat.find_nearest_points import titik_terdekat

titik_pusat = (140.705001, -4.568315)  # Jayapura
kumpulan_titik = [
    ("Sorong", (140.366211, -3.721235)),  # Sorong
    ("Manokwari", (137.166722, -4.043775)),  # Manokwari
    ("Timika", (138.174971, -3.830016))   # Timika
]

titik_terdekat = titik_terdekat(titik_pusat, kumpulan_titik)
print(f"Titik terdekat dari Jayapura adalah {titik_terdekat[0]} dengan koordinat {titik_terdekat[1]}")
```

### 7. Fungsi jarak_total

Fungsi ini menghitung total jarak dari sekumpulan titik dengan urutan tertentu.

```python
from perhitungan_jarak_dan_sistem_koordinat.calculate_total_distance import jarak_total

# Daftar titik yang ingin dihitung jaraknya
titik_input = [(1, 2),  # Gowa (rumah)
               (4, 6),  # Makassar
               (7, 3),  # Maros
               (1, 2)]  # Kembali ke Gowa

# Memanggil fungsi dan menyimpan total jarak
total_jarak = jarak_total(titik_input)

# Mencetak total jarak
print("Total jarak dari Gowa ke Makassar, Maros, dan kembali ke Gowa adalah:", total_jarak)
```

### 8. Fungsi konv_m

Fungsi ini mengonversi jarak dari satuan tertentu ke satuan lainnya, seperti dari meter ke kilometer.

```python
from perhitungan_jarak_dan_sistem_koordinat.km_to_m import konv_m

hasil_km = konv_m(5, "km")
print(f"5 meter dalam kilometer: {hasil_km} km")
```
