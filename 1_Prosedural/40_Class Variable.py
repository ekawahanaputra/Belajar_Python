# Memahami yang disebut class variable
class Mekanik:

    status = 'karyawan tetap'     # ini disebut class variable

    def __init__(self, nama, nomer):
        self.name = nama
        self.no = nomer

yoga = Mekanik('Yoga Deliz', '001')
ikshan = Mekanik('Made mahendra','002')


# perhatikan hasil ketiga syntax ini saat di print
print(Mekanik.status)
print(yoga.status)
print(ikshan.status)
# ketiga syntax diatas akan menampilkan 'karyawan tetap' saat di run
print('\n')

# jika variable status dirubah seperti ini:
Mekanik.status = 'karyawan kontrak'
print(Mekanik.status)
print(yoga.status)
print(ikshan.status)
# Ketiga syntax diatas akan menampilkan 'karyawan kontrak' saat di run
print('\n')

# jika variable status dirubah dengan memakai salah satu objek class seperti ini:
ikshan.status = 'resign'
print(Mekanik.status)
print(yoga.status)
print(ikshan.status)
# Hanya ikshan yang berubah jadi resign saat di run
# Kesimpulannya pikirkan sendiri

# PENGGUNAAN CLASS VARIABLE
# Biasanya variable class paling sering digunakan untuk menghitung object seperti dibawah ini

class mekanik:

    jumlah = 0     # class variable
    
    def __init__(self,nama,nomer):
        self.name = nama
        self.no = nomer

        mekanik.jumlah += 1        # ini artinya setiap object dibuat, nilai variable jumlah akan bertambah 1

rizal = mekanik('Ahmad Rizal',12)  # Ini object nya
yoga = mekanik('Yoga Deliz',15)
made = mekanik('Made Mahendra',20)

print(mekanik.jumlah)   # Lihatlah hasilnya saat di run!

# setiap object dibuat, jumlahnya akan bertambah 1
# Itulah salah satu penggunaan variable class

# ================== SELESAI =======================