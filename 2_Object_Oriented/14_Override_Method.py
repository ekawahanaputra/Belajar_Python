# OVERRIDE METHOD
# Sebuah metode untuk meng override atau menimpa sebuah fungsi pada superClass

class Game:

    def __init__(self,name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor

    def showInfo(self):
        print('ini adalah fungsi dari SuperClass Game')
        print('{} health = {}'.format(self.name, self.health))

    # Marilah kita coba untuk mengOverride / menimpa fungsi 'showInfo()' dari superClass Game

class Tekken(Game):

    def __init__(self,name):
        super().__init__(name, 90, 30)
    

    # Syntax dibawah ini, adalah syntax untuk menimpa fungsi 'showInfo' pada superClass
    def showInfo(self):
        print('ini adalah fungsi dari SubClass Tekken')
        print('{} health = {}'.format(self.name, self.health))

class Bloody_war(Game):

    def __init__(self,name):
        super().__init__(name, 150, 20)

jin = Game('Jin Kazama', 100, 50)
ryu = Tekken('Bakuryu Ha')
inu = Bloody_war('Inuyasa')


# Lihat lah hasil dari kedua syntax dibawah saat di run! meski syntaxnya sama, namun hasilnya akan berbeda
inu.showInfo()
print('/n')
ryu.showInfo()        # Hasil override dari fungsi superClass