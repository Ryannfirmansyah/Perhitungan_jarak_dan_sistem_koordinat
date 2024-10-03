# (points): Fungsi untuk menghitung jarak total untuk beberapa titik
# SITI

class Titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Titik({self.x}, {self.y})"
    
def hitung_jarak_total(titik_titik):
    total_jarak = 0
    for i in range(len(titik_titik) - 1):
        x1, y1 = titik_titik[i].x, titik_titik[i].y
        x2, y2 = titik_titik[i + 1].x, titik_titik[i + 1].y
        jarak = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        total_jarak += jarak
    return total_jarak



    

