# 2. While loop

nilai = 0     # Dengan variable number

while (nilai < 10):
    nilai += 1
    print('No ',nilai)
print('finish')

'''
Jika syntax diatas diterjemahkan dalam kalimat, akan menjadi seperti berikut
nilai = 0 ==> loopinglah nilai ketika nilai kurang dari 10 < while (nilai < 10): >
dengan argumen, setiap looping, nilai ditambah 1 (nilai += 1)
'''
#=====================================================================================
print('\n')

start = True   # Dengan variable boolean
angka = 1

while start:
    print('Huruf')
    angka += 1
    if angka == 10:
        start = False
        print('Stop di angka ', angka)
#=====================================================================================
print('\n')
# CONTOH KASUS LOOPING
# Membuat looping, dimana kita menentukan angka awal dan angka akhir melalui input

angka_awal = int(input('Masukan angka awal : '))
angka_akhir = int(input('Masukan angka akhir : '))
start = True

while start:
    print(angka_awal)
    angka_awal += 1
    if angka_awal == angka_akhir:
        start = False
        print('Looping Berakhir')
#=====================================================================================
print('\n')
    
