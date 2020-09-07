# Looping dibagi menjadi 2, yaitu :

# 1. For Loop
# 2. While Loop
#=================

####  FOR LOOP

angka = (0,1,2,3,4,5,6,7,8,9,10)

for a in angka:               # a = variable loop, angka = variable list
    print('Looping ke ', a)

print('Finish')
#===============================================================================
print('\n')
# Kelebihan dari for loop ketimbang while adalah, for loop bisa bekerja untuk tipe data string
# Contoh dengan tipe data String

buah = ('Apel', 'Jeruk', 'Anggur', 'Nanas', 'Salak')

for b in buah:                # b = variable loop, buah = variable string list
    print('Buah ', b)

print('Finish')
#================================================================================
print('\n')

# 'For Loop juga bisa mengeja string
Nama = 'Wahana'

for eja in Nama:
    print(eja)                # saat di run, kata wahana akan di eja
#================================================================================
print('\n')
# For loop bersarang

nama = ('Andi', 'Agus', 'Ari', 'Aji', 'Angga')
buah = ('Apel', 'Jeruk', 'Anggur', 'Nanas', 'Salak')

for n in nama:
    for b in buah:            # for loop di dalam for loop
        print(n,' Suka makan buah ', b)

#================================ FINISH / SELESAI ===============================