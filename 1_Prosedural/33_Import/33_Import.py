# Import adalah teknik untuk mengakses suatu data maupun program yang berasal dari 
# file luar (eksternal file)
# Pada praktek import kali ini, saya menggunakan file < Main.py > sebagai file external

import Main    # Mengakses seluruh isi program file Main.py

a = Main.Volume # Cara mengakses variable dari Main.py
print(a)

print(Main.panjang)

Main.Luas(10,2) # Cara mengakses function dari Main.py
Main.Luas(5,3)


'''
NOTE :
Ada banyak cara dalam menuliskan syntax import

1.  import Main          (seperti cara diatas - mengimport semua isi program)
2.  import Main as blablabla     
3.  from Main import Luas (Jika ingin mengimport fungsi Luas)
4.  from Main import Luas, Volume (Jika ingin mengimport lebih dari sebuah fungsi)
5.  from Main import Luas as blablabla
'''