# Package adalah sebuah folder yang berisi kumpulan dari module module
# Struktur Package :
# Main.py     =   File utama
# name.py     =   sebagai module
# name.py     =   sebagai module
# __init__.py = file untuk mengakses module - module

# Tata cara buat packages
#1. buatlah file Main.py
#2. buatlah folder untuk module dan beri nama sesukamu. Contoh : Folder EKa
#3. di dalam folder Eka, buatlah file file module sebanyak yang kamu perlukan, lalu beri nama sesuai selera
#4. buatlah sebuah file lagi dalam folder Eka, dan beri nama __init__.py
#5. pada __init__.py, tulislah syntax untuk mengimport module module pada folder Eka
#6. import lah module module pada folder Eka dengan mengimport folder Eka
#   tidak perlu lagi mngimport file file module satu persatu
#   perhatikan saja syntax dibawah ini:

import Eka
# penulisan import juga bisa dibuat bermacam - macam, lihat materi pada import.py


Eka.Luas_Segi_Empat(2,4)
Eka.Volume_Balok(3,5,2)
