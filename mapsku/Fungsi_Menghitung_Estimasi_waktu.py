def estimasi_waktu(jarak, kecepatan_rata_rata):
    """
    Fungsi untuk menghitung estimasi waktu perjalanan.
    
    Parameters:
    jarak (float): Jarak yang akan ditempuh (dalam kilometer atau meter).
    kecepatan_rata_rata (float): Kecepatan rata-rata perjalanan (dalam kilometer per jam atau meter per detik).
    
    Returns:
    float: Estimasi waktu yang dibutuhkan (dalam jam jika jarak dalam km, atau detik jika jarak dalam meter).
    """
    if kecepatan_rata_rata <= 0:
        raise ValueError("Kecepatan harus lebih besar dari 0")
    
    waktu = jarak / kecepatan_rata_rata
    return waktu
