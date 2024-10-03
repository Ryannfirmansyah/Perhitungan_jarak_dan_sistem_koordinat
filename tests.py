from perhitungan_jarak_koordinat import hitung_jarak_ke_titik_pusat

#koordinat
lat1, lon1 = -5.134884, 119.486325 
lat2, lon2 = -5.125064, 119.488556 

jarak = hitung_jarak_ke_titik_pusat(lat1, lon1, lat2, lon2)
print(f"Jarak dari sanggar pramuka ke kost DINAAAAAAAAAA : {jarak:.2f} km")
jarak_km = jarak
jarak_m = jarak_km * 1000

print(f"Jarak dari sanggar pramuka ke kost blablabla : {jarak_m:.2f} m")

