## Deskripsi Tipe Data dan Contoh Penggunaan
# MAPSKU (Perhitungan_jarak_dan_sistem_koordinat)

MAPSKU adalah sebuah package Python yang dirancang untuk membantu programmer melakukan perhitungan jarak dan sistem koordinat, serta berbagai fitur terkait lainnya.

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
pip install mapsku
```
### Dalam modul Fungsi_Titik_Tengah
### 1. Fungsi `titik_tengah(lat_makassar: float, lon_makassar: float, lat_jakarta: float, lon_jakarta: float) -> tuple`
- **Parameter**:
  - `lat_makassar` (float): Latitude dari Makassar.
  - `lon_makassar` (float): Longitude dari Makassar.
  - `lat_jakarta` (float): Latitude dari Jakarta.
  - `lon_jakarta` (float): Longitude dari Jakarta.
- **Return**: Tuple (mid_lat: float, mid_lon: float) yang berisi latitude dan longitude titik tengah antara dua koordinat.
- **Contoh Penggunaan**:
  ```python
  mid_lat, mid_lon = titik_tengah(-5.147665, 119.432731, -6.208763, 106.845599)
  print(f"Titik tengah antara Makassar dan Jakarta adalah: {mid_lat}, {mid_lon}")
  ```
### Dalam modul Fungsi_Derajat_ke_Radian
### 2. Fungsi `derajat_ke_radian(degree: float) -> float`
- **Parameter**:
  - `degree` (float): Nilai derajat yang akan dikonversi ke radian.
- **Return**: float yang merupakan nilai dalam radian.
- **Contoh Penggunaan**:
  ```python
  hasil = derajat_ke_radian(90)
  print(hasil)  # Output: 1.5708
  ```
### Dalam modul Fungsi_Menghitung_Jarak
### 3. Fungsi `jarak_koordinat(lat1: float, lon1: float, lat2: float, lon2: float) -> float`
- **Parameter**:
  - `lat1` (float): Latitude dari titik pertama.
  - `lon1` (float): Longitude dari titik pertama.
  - `lat2` (float): Latitude dari titik kedua.
  - `lon2` (float): Longitude dari titik kedua.
- **Return**: float yang merupakan jarak antara dua titik dalam kilometer.
- **Contoh Penggunaan**:
  ```python
  jarak = jarak_koordinat(-5.1333128, 119.4884481, -5.23026, 119.4995591)
  print(f"Jarak dari Unhas ke Unhas Gowa adalah {jarak:.1f} km")
  ```
### Dalam modul Menghitung_estimasi_waktu
### 4. Fungsi `estimasi_waktu(jarak: float, kecepatan: float) -> float`
- **Parameter**:
  - `jarak` (float): Jarak yang akan ditempuh dalam kilometer.
  - `kecepatan` (float): Kecepatan dalam kilometer per jam.
- **Return**: float yang merupakan waktu tempuh dalam jam.
- **Contoh Penggunaan**:
  ```python
  waktu_tempuh = estimasi_waktu(120, 60)
  print(f"Waktu tempuh untuk jarak 120 km dengan kecepatan 60 km/jam adalah: {waktu_tempuh:.2f} jam")
  ```
### Dalam modul Fungsi_Menyaring_Radius
### 5. Fungsi `saring_radius(locations: dict, center_lat: float, center_lon: float, radius: float) -> list`
- **Parameter**:
  - `locations` (dict): Dictionary berisi nama lokasi sebagai kunci dan tuple (latitude, longitude) sebagai nilai.
  - `center_lat` (float): Latitude dari titik pusat.
  - `center_lon` (float): Longitude dari titik pusat.
  - `radius` (float): Radius dalam kilometer untuk penyaringan.
- **Return**: list yang berisi nama-nama lokasi yang berada dalam radius tertentu dari titik pusat.
- **Contoh Penggunaan**:
  ```python
  locations = {
      "Surabaya": (-7.250445, 112.768845),
      "Medan": (3.595196, 98.672226),
      "Makassar": (-5.147665, 119.432732),
      "Bandung": (-6.917464, 107.619123),
      "Banjarmasin": (-3.316694, 114.590111)
  }
  
  hasil_filter = filtered(locations, -6.208763, 106.845599, 1000)
  print("Kota dalam radius 1000 km dari Jakarta:")
  for kota in hasil_filter:
      print(kota)
  ```
### Dalam modul Fungsi_Titik_Terdekat
### 6. Fungsi `titik_terdekat(titik_pusat: tuple, kumpulan_titik: list) -> tuple`
- **Parameter**:
  - `titik_pusat` (tuple): Tuple berisi (longitude, latitude) dari titik pusat.
  - `kumpulan_titik` (list): List berisi tuple yang terdiri dari nama lokasi dan koordinatnya.
- **Return**: tuple yang berisi nama titik terdekat dan koordinatnya.
- **Contoh Penggunaan**:
  ```python
  titik_pusat = (140.705001, -4.568315)  # Jayapura
  kumpulan_titik = [
      ("Sorong", (140.366211, -3.721235)),
      ("Manokwari", (137.166722, -4.043775)),
      ("Timika", (138.174971, -3.830016))
  ]

  titik_terdekat = titik_terdekat(titik_pusat, kumpulan_titik)
  print(f"Titik terdekat dari Jayapura adalah {titik_terdekat[0]} dengan koordinat {titik_terdekat[1]}")
  ```
### Dalam modul Fungsi_Menemukan_Jarak_Total_untuk_Beberapa_Titik
### 7. Fungsi `jarak_total(titik_input: list) -> float`
- **Parameter**:
  - `titik_input` (list): List berisi tuple yang terdiri dari koordinat titik (longitude, latitude).
- **Return**: float yang merupakan total jarak dari sekumpulan titik dengan urutan tertentu dalam kilometer.
- **Contoh Penggunaan**:
  ```python
  titik_input = [(1, 2), (4, 6), (7, 3), (1, 2)]
  total_jarak = jarak_total(titik_input)
  print("Total jarak adalah:", total_jarak)
  ```
### Dalam modul Konversi_Satuan_Jarak
### 8. Fungsi `konversi_satuan_jarak(nilai: float, satuan: str) -> float`
- **Parameter**:
  - `nilai` (float): Nilai jarak yang akan dikonversi.
  - `satuan` (str): Satuan target untuk konversi (misalnya, "km" untuk kilometer).
- **Return**: float yang merupakan nilai dalam satuan yang diinginkan setelah konversi.
- **Contoh Penggunaan**:
  ```python
  hasil_km = konversi_satuan_jarak(5, "km")
  print(f"5 meter dalam kilometer: {hasil_km} km")
  ```
