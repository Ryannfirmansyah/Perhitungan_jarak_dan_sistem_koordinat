#(points, speed): Fungsi untuk estimasi waktu mengunjungi beberapa titik.
#VELIN
# time_estimation_package.py

def hitung_waktu_tempuh(jarak, kecepatan):
    """Hitung waktu tempuh berdasarkan jarak dan kecepatan.

    Args:
        jarak (float): Jarak dalam kilometer.
        kecepatan (float): Kecepatan dalam kilometer per jam.

    Returns:
        float: Waktu tempuh dalam jam.
    """

    waktu = jarak / kecepatan
    return waktu

