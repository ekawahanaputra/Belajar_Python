# Skenario :
# Sebuah game dimana setiap kali attack, object mendapat penambahan attPower dan Experience
import tkinter

class game:

    def __init__(self,name,power,health,armor):
        self.__name = name
        self.__power0 = power
        self.__health0 = health
        self.__armor0 = armor

        self.__experience = 0
        
    # Getter
    @property
    def getName(self):
        pass

    @property
    def getPower(self):
        pass

    @property
    def getHealth(self):
        pass

    @property
    def getArmor(self):
        pass

    @property
    def getExperience(self):
        pass
   
    @getName.getter
    def getName(self):
        return self.__name

    @getPower.getter
    def getPower(self):
        return self.__power0

    @getHealth.getter
    def getHealth(self):
        return self.__health0

    @getArmor.getter
    def getArmor(self):
        return self.__armor0
    
    @getExperience.getter
    def getExperience(self):
        return self.__experience

    # Setter
    @getPower.setter
    def setPower(self,new_input):
        self.__power0 = new_input
    
    @getHealth.setter
    def setHealth(self,new_input):
        self.__health0 = new_input

    @getArmor.setter
    def setArmor(self,new_input):
        self.__armor0 = new_input
    

    # Method
    def serang(self,enemy):
        # Informasi atribute sebelum serang & diserang
        print('===INFORMATION===')
        self.info0()
        print('\n')
        enemy.info0()
        print('\n')

        # Proses serang & diserang
        print('==' * 30)
        print(self.getName,'Menyerang',enemy.getName)
        enemy.diserang(self,self.getPower)

        # Informasi atribut setelah menyerang
        print('\n')
        self.setArmor += self.attPower
        print(self.getName)
        print('Health = ',self.setHealth)
        print('Armor =',self.setArmor)
        

    
    def diserang(self,enemy,enemyPower):
        # Proses diserang
        attPower = enemyPower / self.getArmor
        enemy.attPower = attPower
        print(self.getName,'diserang',enemy.getName,'dengan kekuatan',enemy.attPower)

        # Informasi atribut setelah diserang
        sisaHealth = self.getHealth - attPower
        sisaArmor = self.getArmor - (attPower / 2)
        self.setHealth = sisaHealth
        self.setArmor = sisaArmor
        print('==' * 30)
        print('\n')
        print('===AFTER ATTACK===')
        print(self.__name)
        print('Health =', self.setHealth)
        print('Armor =',  self.setArmor)

    def info0(self):
        print(self.__name)
        print('Health =',self.getHealth)
        print('Armor =', self.getArmor)


# Object        
mario = game('Mario', 5, 50, 10)
king = game('King of Crocodile', 6, 50, 15)


# Program with Graphical User Interface
jendela = tkinter.Tk()

def attack_mario():
    label1 = tkinter.Label(jendela,text = king.serang(mario))

def attack_king():
    label2 = tkinter.Label(jendela,text = mario.serang(king))

tombol1 = tkinter.Button(jendela, text = 'Serang Mario',command = attack_mario)
tombol2 = tkinter.Button(jendela,text = 'Serang King',command = attack_king)

tombol1.pack()
tombol2.pack()

jendela = tkinter.mainloop()


# Program with Command Line Interface
# mario.serang(king)