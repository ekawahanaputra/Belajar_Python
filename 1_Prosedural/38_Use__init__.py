# Cara menggunakan keyword __init__ pada class
class mekanik:

    def __init__(self,nama,NRP):    # bisa ditambahkan argumen selain self
        self.name = nama            # ini adalah inisialisasi dari argumen - argumen
        self.NRP = NRP
        print('Halo ini adalah __init__')
    
    def performa(self,Flate,JT):
        OP = Flate / JT
        print('Overall Produktifity',self.name, '=',OP)


eka = mekanik('Eka Wahana Putra','024611')    # mendeklarasikan object
yoga = mekanik('Yoga Deliz Pratama','024622') # deklarasikan nama & NRP sesuai urutan pada def __init__()

# Perbedaan __init__ dan fungsi biasa adalah, jika __init__, saat object di deklarasikan, __init__ langsung di eksekusi
# Sedangkan jika fungsi biasa, harus di akses dulu baru di eksekusi. Coba saja di run

# Cara mendisplay
print(eka.name)       # lihat hasilnya
a = yoga.NRP
print(a)
yoga.performa(150,130)
