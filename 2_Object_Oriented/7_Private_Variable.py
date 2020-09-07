# Private Variable
class mekanik:

    jumlah = 0       # disebut public class variable
    __NRP = 2567      # disebut private class variable

    def __init__(self,name,nomer):
        self.name = name      # Ini public inheritence variable
        self.no = nomer
        self.__umur = 'Rahasia'    # ini private unheritance variable
        
    

made = mekanik('Made Mahendra',6)
yoga = mekanik('Yoga Deliz Pratama',3)

# Cobalah berexperimen merubah variable diatas

print(made.__dict__)
made.__umur = 30
print(made.__dict__)


mekanik.__NRP = 20200
print(mekanik.__dict__)