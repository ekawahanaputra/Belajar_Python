# pada materi ini, hanya akan menunjukan teknik looping dengan menggunakan
# keyword keyword tertentu

# Contoh Looping dengan cara biasa
# Program Mencetak Urutan Mekanik
mekanik = ['Yoga','Rizal','Made','Ikshan','Harol','Hermawan']
no = 0

for x in mekanik:
    print('No', no, x)
    no += 1

print('\ndengan Enumerate')
# Looping diatas bisa dibuat lebih singkat dengan 'ENUMERATE'
for number, nama in enumerate(mekanik):        # number & nama adalah variable untuk menjalankan looping
    print(number, nama)                        # in enumerate adalah keyword

# Looping dengan keyword "in zip"
# 'in zip' dapat digunakan untuk menggabungkan looping 2 variable
print('\nLooping dengan in zip')
nama_cwe = ['Lisna','Ayu','Lia','Ninda','Gita']
hobi_cwe = ['menyanyi','Menari','Shopping','Senam','Berenang']

for nama, hobi in zip(nama_cwe, hobi_cwe):
    print(nama,'suka',hobi)

#==================================================================================================
# Looping dengan data set
print('\nLooping tipe data set')
type_mobil = {'Calya', 'Avanza','Agya','Fortuner','Camry'}

for toyota in type_mobil:
    print(toyota)

print('\n')
for toyota in sorted(type_mobil):   # Nama mobil akan diurut sesuai abjad
    print(toyota)

#==================================================================================================
# Looping dengan type data dictionary
print('\nLooping tipe data dictionary')
nameOF = {'Devi':'TK'
          ,'Ayu':'SD'
          ,'Lisna':'SMP'
          ,'Ninda':'SMA'
          ,'Tia':'Bekerja'}

for a in nameOF.keys():
    print(a)           # untuk melooping key nya saja

print('\n')

for b in nameOF.values():   # untuk melooping values nya saja
    print(b)

print('\n')

for c in nameOF.items():    # untuk melooping all items
    print(c)               

print('\n')

for nama, status in nameOF.items(): # jika menggunakan 2 variable, harus memakai '.items'
    print('ada',nama,'di masa',status,'ku')
#========================== SELESAI ===============================================================
