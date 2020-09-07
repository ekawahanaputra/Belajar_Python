# Class Inheritance
class Mobil:

    def __init__(self, nama, transmisi):
        self.name = nama
        self.trans = transmisi
    
    def Jenis_Mobil(self):
        print('Mobil',self.name,'adalah jenis mobil city car')
    
    def Penggerak(self):
        print('Mobil',self.name,'menggunakan transmisi',self.trans)


# Class Inheritance berfungsi jika kita ingin membuat class yang berbeda
# namun masih tetap memiliki fungsi yang sama. Sehingga kita tak perlu
# menulis ulang syntax fungsi. Cara penulisannya adalah sebagai berikut:

class Toyota(Mobil):        # Lihatlah class Toyota adalah class yang berbeda dengan class Mobil
    pass                    # pass ditulis jika tidak ada penambahan function

calya = Mobil('Calya','Otomatis')
agya = Mobil('Agya','Manual')
avanza = Toyota('Avanza','Manual')

calya.Jenis_Mobil()
agya.Penggerak()

avanza.Jenis_Mobil()