# (degree): Fungsi untuk mengubah derajat ke radian.
#JABBAR
def drjt_rdn(derajat, desimal=2):
    pi = 3.141592653589793
    radian = derajat * (pi / 180)
    return round(radian, desimal)