# Tipe data list
buah = ['Jeruk','Apel','Anggur','Semangka','Nanas']
print(buah)

# Diatas adalah tipe data list
#=============================================================
print('\n')
# Memanipulasi tipe data list dengan beberapa method

# DIbawah adalah method untuk menambah data kedalam list
# [1]
buah.append('Mangga')  # append = Method untuk menambahkan 'Mangga' ke dalam list
print(buah)

# [2]
buah.extend('Leci')    # extend = method untuk menambahkan 'Leci' ke dalam list
print(buah)            # Leci akan masuk list dengan cara di eja

# [3]
buah.insert(2,'Melon') # insert = method untuk menyisipkan 'Melon'
print(buah)            # (2,'Melon) artinya, 'Melon' disisipkan pada index kedua list

# Method untuk menghitung index sebuah list
a = len(buah)
print('Jumlah index list buah =',a)

# Method untuk menghitung anggota list dengan nama tertentu
a = buah.count('Semangka')
print('Jumlah Semangka adalah ',a)

# Method untuk meremove anggota list
buah.remove('Semangka') # remove = untuk menghapus 'Semangka' dari list
print(buah)

buah.reverse()          # reverse = Berfungsi untuk menampilkan list dengan
print(buah)             # urutan terbalik

# Dan lain lain
print('\n')

makanan = buah
makanan.append('Salak')
print(makanan)
print(buah)
# Jika syntax diatas di run, maka variable 'makanan' akan bertambah anggota listnya
# Begitu juga dengan variable buah.
# Jika anda ingin agar variable 'buah' anggota listnya tidak ikut bertambah, maka syntaxnya adalah sbb:
print('\n')

'''
makanan = buah.copy()   # Tambahkan .copy pada variable 'buah' ketika deklarasi variable
makanan.append('Salak')
print(makanan)
print(buah)
'''
#====================== SELESAI ===========================================