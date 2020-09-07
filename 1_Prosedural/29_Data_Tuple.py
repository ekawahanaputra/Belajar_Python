# DATA TUPLE
# Berbicara tentang data tuple, kita tidak bisa lepas dari tipe data list
# Adapun data tuple dan data list memiliki persamaan dan perbedaan yaitu:

# Contoh perbedaan data list & tuple
list = [1,2,3,4,5]     # ini adalah list. penulisan menggunakan [list]
tuple = (1,2,3,4,5)    # ini adalah tuple. penulisan menggunakan (tuple)

print('ini adalah data list', list)
print('ini adalah data tuple', tuple,'\n')

# Data List dapat melakukan banyak manipulasi seperti append, insert, index,dll
# sedangkan data tuple sifatnya tetap, dan permanen dan tidak bisa dirubah ubah

list.append(6)
print(list)        # data list ditambahkan
list.insert(3,99)
print(list)        # list akan menyisipkan '99' pada index '3'

'''
tuple.append(6)
print(tuple)       # tak akan dieksekusi/error jika dirun
'''

# Kesimpulannya, meski hampir terlihat sama, namun data list dan tuple adalah berbeda
# gunakan data list hanya jika kedepannya data tersebut akan anda rubah / manipulasi
# prioritaskan menggunakan data tuple hanya jika anda yakin tidak akan menggunakannya untuk manipulasi

# Note :
       # data tuple lebih sedikit memakan memory daripada data list
       # selain itu, proses eksekusi data tuple juga 10 kali lebih cepat dari list
       # pertimbangkan selalu data apa yang akan anda gunakan ketika membuat syntax
#============================= SELESAI ========================================================================