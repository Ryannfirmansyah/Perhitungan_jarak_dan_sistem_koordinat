# (degree): Fungsi untuk mengubah derajat ke radian.
#JABBAR             
def derajat_ke_radian(derajat, desimal=2):
    pi = 3.141592653589793
    radian = derajat * (pi / 180)
    hasil = round(radian, desimal)
    return int(hasil) if desimal == 0 else hasil