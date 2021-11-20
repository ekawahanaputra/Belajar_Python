import numpy as np
from numpy.core.fromnumeric import ravel, shape

a = np.array(([4,3,2], [9,8,7]))
print('\nMatrik a :')
print(a)
print('ukuran :', np.shape(a)) # ===>> bisa juga ditulis begini "a.shape"


# Transpose Matrik (Merubah baris jadi kolom, & sebaliknya)
print('\ntranspose matrik a :')
print(np.transpose(a))
    # bisa juga dibuat seperti ini:
print('\n', a.transpose())
    # atau seperti ini
print('\n', a.T)

# Note : transpose tidak merubah nilai a perhatikan hasil script dibawah:
print('\n', a)
print('ukuran :', a.shape)
#================================================================================



# Flatten Array (Merubah matrik menjadi array)
print('\nflatten array matrik a :')
print(np.ravel(a))
    # bisa juga ditulis begini
print(a.ravel())

# Note : nilai a tidak dirubah
#================================================================================



# Reshape Matrik (Merubah bentuk matrik)
print('\nReshape matrik a :')
print(a.reshape(3,2))  #===>> nilai argumen = harus sama dengan jumlah element matrik
                            # kalau jml elemen = 6, nilai argumen dibuat (1,6),(6,1),(2,3),atau(3,2)
    # kita coba dengan argumen yang beda sbb:
print('\n', a.reshape(6,1))

# Note : reshape tidak merubah nilai a, dan perhatikanlah perbedaan hasilnya dengan tranpose
#======================================================================================================



# Resize (Merubah ukuran matrik)
print('\nResize matrik a :')
a.resize(3,2)
print(a)
print('ukuran stelah diresize ;', np.shape(a))

# Argumen resize bisa dibuat berapapun. jika argumen melebihi elemen matrik yang dirubah,
# elemen matrik akan ditambah kan elemen 0. Lihat contoh dibawah :
a.resize(10,5)
print('\n', a)
print('ukuran a setelah resize :', np.shape(a))
#=====================================================================================================


# SELESAI