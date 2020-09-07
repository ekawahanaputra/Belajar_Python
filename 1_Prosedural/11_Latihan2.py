# LATIHAN KOMPARASI & LOGIKA
# Latihan ini adalah gabungan dari komparasi dan logika

#PR dari kelas terbuka
# 2. +++++0-----5+++++8-----11+++++
#    menentukan nilai kurang dari 0 atau diantara 5 dan 8 atau lebih dari 11

n_input = float(input('Input angka yang kurang dari 0\n atau angka diantara 5 dan 8\n atau angka yang lebih dari 11 ! :\n '))
n_correct_1 = n_input < 0
n_correct_2 = n_input > 11
n_hasil_1 = n_correct_1 or n_correct_2

n_correct_3 = n_input > 5
n_correct_4 = n_input < 8
n_hasil_2 = n_correct_3 and n_correct_4

HASIL = n_hasil_1 ^ n_hasil_2

print ('Angka yang anda masukan ', HASIL)
