# LATIHAN KOMPARASI & LOGIKA
# Latihan ini adalah gabungan dari komparasi dan logika

#PR dari kelas terbuka
# 1. -----0+++++5-----8+++++11-----
#    menentukan nilai antara 0 sampai 5 atau 8 sampai 11

N_input = float(input('input nilai diantara 0 dan 5 atau diantara 8 dan 11 : '))
N_correct1_1 = N_input > 0
N_correct1_2 = N_input < 5
hasil_correct1 = N_correct1_1 and N_correct1_2

N_correct1_3 = N_input > 8
N_correct1_4 = N_input < 11
hasil_correct2 = N_correct1_3 and N_correct1_4

hasil_akhir = hasil_correct1 ^ hasil_correct2

print ('Angka yang anda masukan adalah', hasil_akhir)
