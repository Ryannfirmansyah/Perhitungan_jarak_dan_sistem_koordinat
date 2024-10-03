from distance_to_center import hitung_jarak_ke_titik_pusat

# Koordinat Jakarta
latitude_jakarta = -6.2088
longitude_jakarta = 106.8456

# Koordinat Bandung
latitude_bandung = -6.9147
longitude_bandung = 107.6098

# Panggil fungsi hitung_jarak_ke_titik_pusat
jarak = hitung_jarak_ke_titik_pusat(latitude_jakarta, longitude_jakarta, latitude_bandung, longitude_bandung)

print(f"Jarak antara Jakarta dan Bandung adalah {jarak} km.")