# STATIC METHOD & CLASS METHOD
# Materi ini juga termasuk pada mater encapsulasi. Hanya saja, pada materi ini
# akan membahas tentang cara mengakses private variable yang menempel pada class

class game:

    __jumlah = 0       # private class variable

    def __init__(self,name):
        self.name = name
        game.__jumlah += 1

    # Ini adalah praktek
    # Kita coba mengakses private class variable dengan getter
    def get_jumlah1(self):
        return game.__jumlah     # ini tidak akan bisa mengakses nilai __jumlah karena method ini hanya untuk object, bukan class
                                 # hanya object yang bisa mengakses
    
    # Kita coba method tanpa (self)
    def get_jumlah2():           # ini bisa mengakses class, tapi tidak bisa mengakses object
        return game.__jumlah
    
    # Agar bisa mengakses class maupun method, ada 2 cara
    # dengan STATIC METHOD
    @staticmethod
    def get_jumlah3():
        return game.__jumlah

    # dengan CLASS METHOD
    @classmethod
    def get_jumlah4(hore):
        return game.__jumlah

lisna = (game('Lisna Ayu'))
surya = (game('Adi Surya'))
oka = (game('Oka Chandra'))

# LIHAT HASIL AKSES/ cobalah dengan berbagai macam syntax
print(oka.get_jumlah3())
print(lisna.get_jumlah4())