from calculate_total_distance import jt
# Membuat beberapa objek Titik

# Daftar titik yang ingin dihitung jaraknya
titik_input = [(0, 0), (3, 4), (6, 8), (9, 12)]

# Memanggil fungsi dan menyimpan total jarak
total_jarak = jt(titik_input)

# Mencetak total jarak
print("Total jarak dari titik-titik adalah:", total_jarak)