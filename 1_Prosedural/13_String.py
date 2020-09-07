# PENGENALAN STRING
# String adalah kumpulan dari karakter

# Contoh
data = 'Tulisan ini adalah String'
print (data)
print (type(data))

# Materi ini akan menerangkan cara membuat string dengan cara yang berbeda beda
# 1. Cara Membuat String ada 3 yaitu ;
'''
   1. Membuat string dengan single quote ('.....')
   2. Membuat string dengan double quote (".....")
   3. Membuat string dengan backslash ( \ ) tanda diatas ENTER
'''

# Dengan Single Quote ('...')
data = 'Menggunakan single quote'
print (data)

# Dengan Double Quote ("...")
data = "Menggunakan double quote"
print (data)

# Dengan Backslash (\)
# digunakan disaat tertentu ketika ingin menjadikan tanda (') menjadi string
# Contoh
'''
<< print ('Waktunya shalat jum'at') >>
syntax diatas akan rancu dan error
sebagai solusinya, syntax akan di buat seperti dibawah :
'''
print ('waktunya shalat jum\'at')


# 2. Tanda tanda yang digunakan pada string

# Tanda tab ('\t')
# digunakan untuk menjauhkan jarak spasi
print ('Eka\tWahana')

# Tanda backspace ('\b')
# digunakan untuk mendekatkan jarak spasi
print ('Eka\bWahana')

# Tanda newline ('\n'), ('\r'), ('\n\r')
# digunakan untuk menampilkan line baru
print ('Eka\nWahana')       # LF - Line Feed - di unix
print ('Eka\rWahana')       # CR - Carriage Return
print ('Eka\n\rWahana')     # CRLF - Line Feed Carriage Return - di Windows


# 3. Sring Literal atau raw
# contoh :
print ('C:\new user') # jika dieksekusi akan membuat line baru

# maka solusinya adalah menggunakan raw (r) di depan
# contoh :
print (r'C:\new user') # semua karakter setelah 'r' akan dianggap string


# 4. Multiline literal string 
print ("""
Nama : Eka Wahana Putra
Umur : 29 Tahun
Istri: Sri Mariningsih
""")
# digunakan untuk menulis string yang banyak

# 5. Gabungan multiline literal dan raw
print (r"""
Nama : Eka Wahana Putra
Umur : 29 Tahun
Istri: Sri Mariningsih
Website : www.tfirst\login\toyota
""")
# untuk memudahkan saja