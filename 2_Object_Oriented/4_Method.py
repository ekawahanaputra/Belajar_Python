class game:

    def __init__(self, inputName, inputNyawa):
        self.name = inputName
        self.nyawa = inputNyawa

    # Method ada 3, yaitu :
    # 1. Void Method atau Method tanpa Return
    def siapa(self):
        print ('\nNama ku adalah ', self.name)
    
    def berapa(self):
        print ('Sisa nyawa adalah ', self.nyawa)
    
    # 2. Method dengan argumen
    def tambah_nyawa(self,up):
        self.nyawa += up
        print ('Dapat 1 nyawa menjadi', self.nyawa)
    
    # 3. Method dengan return
    def kurangi_nyawa(self):
        return self.nyawa



Karakter1 = game ('Mario', 3)
Karakter2 = game ('Luigi', 4)

print (Karakter1.__dict__)

# Memanggil dengan method tanpa return
Karakter1.siapa()
Karakter1.berapa()

# Memanggil method dengan argumen
Karakter1.tambah_nyawa(1)

# Memanggil argumen method dengan return
print (Karakter1.kurangi_nyawa())


