# OPERASI PADA STRING

# 1. Cara menggabungkan string
nama_depan = 'Eka'
nama_tengah = 'Wahana'
nama_akhir = 'Putra'

# cara menggabungkan memakai (+)
nama_lengkap = nama_depan + nama_tengah + nama_akhir
print (nama_lengkap)

# agar gabungan string berspasi, memakai ('   ')
nama_lengkap = nama_depan +' '+ nama_tengah +' '+ nama_akhir
print (nama_lengkap)

#=============================================================

# 2. Cara mengukur panjang string menggunakan lenght (len)
panjang_nama = len (nama_lengkap)
print ('Panjang nama Eka adalah = ', panjang_nama)

#=============================================================

# 3. Operator pada string

# cara mengecek eksistensi sebuah char atau string pada sring
# menggunakan (in)
huruf = 'W'
eksistensi = huruf in nama_lengkap  # maksudnya huruf W di nama lengkap
print ('Apakah ada huruf W di nama ku ? ', eksistensi)

kata = 'Putra'
eksistensi = kata in nama_lengkap
print ('Apakah ada kata"Putra" di namaku ? ', eksistensi)

kata = 'Eka'
eksistensi = kata not in nama_lengkap # maksudnya kata tidak ada di nama lengkap
print ('Benarkah kata "Eka" tidak ada di namaku ? ', eksistensi)

#=============================================================

# 4. Cara mengulang string
print ('wk'*10) # hasilnya akan mejadi 'wkwkwkwkwkwkwkwkwk'. atau bisa juga ditulis
print (10*'wk')

#=============================================================

# 5. Indexing (Menampilkan huruf ke -n dari sebuah string)
Nama = 'Eka Wahana Putra'
print ('index ke 2 : ', Nama[2]) # syntax indexing adalah '[index ke- n]'
print ('index ke 3 : ', Nama[3]) # index dihitung mulai dari 0 1 2 3 4 ...dst
print ('index ke -1 : ', Nama[-1]) # index ke -1 dihitung dari belakang
print ('index dari 0 sampai 4 : ', Nama[0:4]) # syntax index dari n ke n '[dari n : ke n]'
print ('index 2 4 6 8 : ', Nama[0:10:2]) # syntax untuk jenis ini '[dari n : ke n : selisih]'

# nilai char yang paling kecil
print ('nilai Char paling kecil dari Eka Wahana Putra : ', min(Nama)) # syntax pake 'min(data)'
# yang dimaksud nilai char paling kecil adalah berdasarkan kode ASCII
# mari kita lihat nilai ASCII untuk spasi ('  ')
ascii_code = ord (' ')
print ('Nilai ascii dari spasi adalah ', ascii_code)

# nilai char yang paling besar
print ('nilai Char paling besar dari Eka Wahana Putra : ', max(Nama))

#=============================================================

# 6. Operator String dalam bentuk method
nama = 'I Putu Surya Adi Wahana Saputra'
jumlah = nama.count('a')  # menghitung jumlah huruf a dari string
print ('Jumlah huruf a pada ',nama,' adalah ', jumlah)


#=============== SELESAI ======================================

