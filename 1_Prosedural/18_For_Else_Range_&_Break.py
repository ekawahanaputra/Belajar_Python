# FOR - RANGE

for a in range(0,10):    # range (0,10) maksudnya adalah angka dari 0 sampai 10
    print(a)

print('\n')

for b in range(0,50,5):  # range (0,10,5) maksudnya adalah angka dari 0 sampai 50 dengan jarak kelipatan 5
    print(b)

# silahkan lihat perbedaan dari 2 syntax diatas dengan melakukan run
#=========================================================================
print('\n')
# FOR - BREAK

for c in range (0,11):
    print(c)
    if (c == 5):
        print('Angka Ditemukan')
        break            # fungsi break adalah menghentikan looping dalam sebuah kondisi
                         # jika tidak ada break, looping akan diteruskan sesuai range

#=========================================================================
print('\n')
# FOR - ELSE

find_number = float(input('Masukan number yang anda cari : '))

for d in range (0,20):
    print(d)
    if (d == find_number):
        print('Angka ', find_number,' ditemukan!')
        break
else:
    print('Angka ', find_number,' tidak masuk dalam range')

print('FINISH')

#=============== SELESAI ==================================================





