# Cara membuat class (template)
class Countrys:           # disebut Deklarasi Class
    pass
                          # ada konvensi bahwa setelah deklarasi class, harus ada jarak 2 baris setelahnya
                          
Country1 = Countrys()     # ini disebut object / instance
Country2 = Countrys()
Country3 = Countrys()

Country1.name = 'Indonesia'
Country1.power = 300

Country2.name = 'Amerika'
Country2_power = 1000

Country3.name = 'Rusia'
Country3.power = 800

print (Country1)          # untuk membuktikan bahwa Country1 adalah object
print (Country1.__dict__) # untuk menampilkan atribut apa saja yg dimiliki Country1 dengan keyword __dict__
print (Country2_power)    # untuk menampilkan Country2.power

# Semua hasil bisa dilihat saat di run
