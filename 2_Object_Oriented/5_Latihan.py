
# Class / Template
class game :

# Instance Variable / Variable dari Object
    def __init__ (self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

# Method dari Object
    def serang(self, musuh):            # musuh adalah argumen dari king
        print (self.name, 'Menyerang', musuh.name)
        musuh.diserang(self, self.power)       # agar 'king diserang' otomatis muncul, maka dipanggil disini

    def diserang(self, musuh, powerMusuh):   # powerMusuh adalah argumen baru yg di inisiasi oleh 'self.power' pada line 11
        print (self.name, 'diserang', musuh.name)
        powerAttack = powerMusuh / self.armor
        print ('Power yang diterima : ', powerAttack)
        sisaHealth = self.health - powerAttack
        print ('Sisa darah ', self.name, ' adalah : ', sisaHealth)

# Object
mario = game ('Mario', 100, 20, 20)
king = game ('King', 100, 50, 10)

# Excecute Method of Object / Program
mario.serang(king)
print ('\n')
king.serang(mario)