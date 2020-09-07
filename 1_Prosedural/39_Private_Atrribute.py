# Privat atrribute adalah sebuah variable ataupun atribute yang tidak bisa diakses
# dan dirubah sembarangan. Cara penulisannya adalah dengan menambahkan '__' pada nama variable
# Mari simak penggunaannya
class mekanik:

    tipe = 'avanza'   # ini adalah variable / atrribute public
    __OP = 0      # ini adalah variable / atrribute private

    # Untuk membuktikan, cobalah run program dibawah ini satu satu. Dan lihat perbedaannya

# print(mekanik.tipe)
# print(mekanik.__jumlah)


# PENGGUNAAN PRIVAT ATRRIBUTE

    def __init__(self, nama, nomer):
        self.name = nama
        self.no = nomer

    def performa(self,flate,jt):
        OP = (flate / jt) * 100                # Ini masih memakai atrribute public
        print('Productivitas',self.name,'adalah',OP)

    def point(self,produktivitas):
        self.__OP += produktivitas          # Cara memasukan variable private

    def PK(self):
        if self.__OP >= 110:
            print('PK',self.name,'B+')      # Cara mengolah variable private
        elif self.__OP <= 100:
            print('PK',self.name,'B')

yoga = mekanik('Yoga Deliz Pratama','001')
rizal = mekanik('Ahmad Rizal Mutaqin','002')


yoga.performa(150,154)     # cara menampilkan variable private dengan cara berantai
yoga.point(97)
yoga.PK()

rizal.performa(174,154)
rizal.point(112)
rizal.PK()