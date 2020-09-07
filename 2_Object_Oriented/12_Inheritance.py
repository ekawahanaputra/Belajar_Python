# INHERITANCE 
# adalah sebuah teknik untuk menurunkan/mewariskan sebuah class yang disebut superclass kepada subclass
# Contoh:

class Tekken:            # Disebut SuperClass

    def __init__(self,name,health):
        self.name = name
        self.health = health

class Blood_War(Tekken): # Disebut SubClass       //===>> Cara penulisan Inheritance
    pass


# Lihat perbedaan pada penulisan syntax Objectnya

jin = Tekken('Jin',100)              # Ini object dari SuperClass Tekken
bakuryu = Blood_War('Bakuryu',50)    # Ini adalah object dari SubClass Bloody_War


# Cobalah syntax ini satu persatu untuk melihat sebuah object milik class yang mana
#print(help(jin))
#print(help(bakuryu))

print(jin.__dict__)
print(bakuryu.__dict__)