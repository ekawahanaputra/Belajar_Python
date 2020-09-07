# SUPER CONSEPT
# Adalah teknik dalam pemrograman python, yang berfungsi untuk memudahkan programer untuk menuliskan syntax
# yang sifatnya berulang ulang antar SuperClass dan SubClass

class Game:

    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor

    def Info(self):
        print("nilai Armor dari {} adalah {}".format(self.name, self.armor))

class Tekken(Game):

    # Agar kita tidak perlu lagi menulis fungsi yang sama seperti yang ada pada SuperClass Game, maka dapat
    # ditulis seperti dibawah ini :
    def __init__(self,name):
        Game.__init__(self,name,100,50)   #//----> Memakai nama superClass Game
        
        # print fungsi Info()
        super().Info()

class Bloody_War(Game):

    # Selain cara diatas, dapat juga ditulis dengan syntax berikut
    def __init__(self,name):
        super().__init__(name,300,30)    #//-----> Memkai Super().__init__()

        # cara lain print fungsi info()
        Game.Info(self)

jin = Game('Jin', 200, 40)
bakuryu = Tekken('Bakuryu')
shima = Bloody_War('Shima')

# Lihat hasilnya

# def __init__
print('\n')
print('nilai Health dari',jin.name,'adalah',jin.health)              # print Object SuperClass Game
print('nilai Health dari',bakuryu.name,'adalah',bakuryu.health)      # print Object SubClass Tekken
print('nilai Health dari',shima.name,'adalah',shima.health)          # print Object SubClass Bloody_War
