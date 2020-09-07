# TIPE DATA SET
# Tipe data set bisa juga disebut himpunan.
# Ada 2 cara membuat tipe data set. Yaitu:

# Cara Pertama
pewayangan = {'Rama','Shinta','Rahwana','Anoman','Sugriwa'}
print(pewayangan)

# Ditulis dengan kurung kurawal { data_set }
# Menambahkan data ke data set
pewayangan.add('Arjuna')
print(pewayangan)   # Lihatlah arjuna diletakan tak berurutan, karena tipe data ini tidak mementingkan urutan

# Jika menambahkan data yang sama
pewayangan.add('Rama')
print(pewayangan)   # Rama tetap ada satu, karena tipe data ini tidak mementingkan jumlah data
                    # meskipun jumlah data ada 2, namun tetap akan dianggap satu

print(sorted(pewayangan))  # Cara print agar berurutan
#=============================================================================================================
# Cara Kedua
superhero = set()       # buat variablenya dengan nilai = set()

superhero.add('ironman')   # tambahkan himpunannya satu persatu seperti disamping
print(superhero)
superhero.add('C.America')
print(superhero)
superhero.add('Thor')
print(superhero)
superhero.add(212)         # himpunan juga dapat dicampurkan dengan angka/number
print(superhero)
#=============================================================================================================
# Operasi pada himpunan
himp_bil_ganjil = {1,3,5,7,9,11}
himp_bil_genap = {2,4,6,8,10}
himp_bil_prima = {1,2,3,7,11,13}

print(himp_bil_ganjil.union(himp_bil_genap))   # menggabungkan himp_bil_ganjil & genap

a = himp_bil_genap.intersection(himp_bil_prima) # irisan dari himp_bil_genap & prima
print(a)

#===================================== SELESAI ================================================================