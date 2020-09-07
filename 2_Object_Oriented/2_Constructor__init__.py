class Countrys:           
    
    def __init__(self, country_name, country_power):
        self.name = country_name
        self.power = country_power
        # def __init__ berfungsi sebagai inisialisasi


Country1 = Countrys('Indonesia', 500)
Country2 = Countrys('Amerika', 1000)
Country3 = Countrys('Rusia', 800)



print (Country1.name)
print (Country2.name)
print (Country3.name)
print (Country1.__dict__)
print (Country2.__dict__)
print (Country2.__dict__)
# __dict__ berfungsi untuk menampilkan seluruh atribute
# def __init__ & __dict__ adalah keyword dalam python

#===========SELESAI========================================