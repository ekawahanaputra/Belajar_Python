# ENCAPSULASI 
# Ada 2 aturan dalam encapsulasi yaitu:
# 1. buat semua variable private
# 2. untuk mengambil data private, kita menggunakan getter(mengambil) & setter (mensetting)
class game:

    def __init__(self,name,health,power):
        self.__name = name            # 1 buat semua variable private
        self.__health = health
        self.__power = power
    
    # getter  ==> hanya berfungsi untuk mengakses private variable
    def akses_nama(self):
        return self.__name
    
    def akses_health(self):
        return self.__health

    # setter  ==> berfungsi untuk mengubah nilai dari private variable
    def diserang(self, nilai_power):
        self.__health -= nilai_power


boy = game('Boy Chandra',50, 5)
lisna = game('Lisna Ayu',70,7)

# unuk mngakses private variable, tinggal ketikan berikut
print(lisna.akses_nama())
print(lisna.akses_health())
print(boy.akses_nama())
print(boy.akses_health())

# cara menampilkan setter
lisna.diserang(10)          # ubahn dulu nilai variable self.__health dengan syntax ini
print(lisna.akses_health()) # setelah itu barulah tampilkan fungsi getter (akses_health)