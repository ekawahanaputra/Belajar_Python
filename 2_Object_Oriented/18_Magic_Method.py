# MAGIC METHOD adalah beberapa method khusus yang memiliki fungsi khusus. Magic Method pada python bisa dikenali
# melalui cara penulisannya yang diawali tanda underscore 2 kali dan diakhiri tanda underscore 2 kali juga
# Contoh Magic Method:
#      __init__
#      __repr__
#      __str__
#      __dict__
#      __add__
# dan masih banyak lagi yang lainnya. Jika ingin tau penggunaannya silahkan baca documtasi python di python.org

class Teh:

    def __init__(self,name,jumlah):
        self.name = name
        self.jumlah = jumlah

    #def __repr__(self):          
        #return "ini adalah {} dengan jumlah {}".format(self.name,self.jumlah)

    def __str__(self):
        return 'ini adalah method dari __str__, dan ada {} dengan jumlah {}'.format(self.name, self.jumlah)

        # Cara menampilkan print dari method __repr__ & __str__ adalah seperti diatas

    def __add__(self1,self2):
        return self1.jumlah + self2.jumlah


pucuk = Teh('Teh Pucuk', 5)
sosro = Teh('Teh Botol Sosro', 10)

# Print def __init__
print(pucuk.name)
print(pucuk.jumlah)

# Print def __repr__ atau __str__
print (sosro)

# Print def__add__
print(pucuk + sosro

# Masih banyak lagi magic method yang lain, lihatlah penggunaannya pada dokumentasi python.org
