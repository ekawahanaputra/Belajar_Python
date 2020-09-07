# Berikut ini akan membahas tentang getter dan setter milik python

class Mario_Bross:

    def __init__(self,name,health):
        self.__name = name
        self.__health = health

    @property                        # @property berfungsi untuk mengubah method menjadi variable
    def health(self):                # 1. ini syntax yang ditulis pertama
        pass

    @health.getter                   # 2. setelah itu barulah menuls syntax .getter
    def health(self):
        return self.__health

    @health.setter
    def health(self,input_baru):     # 3. ini syntax setter berfungsi untuk merubah variable
        self.__health = input_baru
    
    @health.deleter                  # 4. berfungsi untuk menghapus sebuah private variable
    def health(self):
        self.health = '0'

mario = Mario_Bross('Mario',100)
luigi = Mario_Bross('Luigi',90)

# Getter
print(mario.health)                  # Menampilkan getter, sama halnya dengan cara menampilkan variable. karena fungsi sudah dirubah ke dalam bentuk variable

# Setter                             
mario.health = 70                    # Ingat !!! menampilkannya harus sama dengan cara variable
print(mario.health)
print(mario.__dict__)

# Deleter
del mario.health
print(mario.health)
print(mario.__dict__)
