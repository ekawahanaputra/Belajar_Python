import numpy as np

# Membuat matrik dengan tipe data tertentu (integer, float, boolean, dll)
a = np.array(([1,2,3], [4,5,6,]), dtype=float)  #== dtype = diisi dengan tipe data

print('\nMatrik dengan tipe data tertentu')
print(a)
#===============================================================================



# Membuat array menggunakan function
# Contoh 1
def kuadrat(baris,kolom):
    return kolom**2

# Perbandingan pake cara biasa dan cara khusus
print('\nPake cara biasa') #=====================
print(kuadrat(1,5))

print('\nPake cara khusus') #===================
b = np.fromfunction(kuadrat,(1,5), dtype=int)
print(b)

#Contoh 2
def jumlah(baris,kolom):
    return baris + kolom

c = np.fromfunction(jumlah, (3,4), dtype=float)
print('\ncontoh lain')
print(c)

# NOTE : Format penulisan ==>> np.fromfuction(<nama_fungsi>, (<ukuran_matrik>), <dtype>)
