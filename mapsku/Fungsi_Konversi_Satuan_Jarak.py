# Fungsi untuk konversi kilometer ke meter.
#JABBAR
def konversi_satuan_jarak(ukuran, jenis="meter"):
    konversi = {
        "km": ukuran / 1000,
        "dm": ukuran * 10,
        "cm": ukuran * 100,
        "mm": ukuran * 1000,
        "miles": ukuran / 1609.34,
        "kaki": ukuran / 0.3048,
        "yard": ukuran / 0.9144
    }

    return round(konversi.get(jenis, ukuran), 3)


