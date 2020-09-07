# Input dan Output File
# Ada beberapa mode dalam menggunakan input & output file yaitu:
'''
w = write mode / mode menulis dan menghapus file lama, jika tidak ada
    file, maka akan membuat file yang baru
r = read only mode -- Hanya bisa membaca saja
a = appending mode -- menambahkan data diakhir baris
r+ = write and read mode
'''

# 1. Cara membuat file.text

dokumen = open('belajar.txt','w')    # dahulukan dengan open(), kemudian berikan argumen 1 (nama file.txt), lalu argumen 2 (mode)
dokumen.write('Ini adalah keluarga saya')  # menuliskan isi file
dokumen.write('\nini baris kedua')
dokumen.close()       # setelah menulis (write) wajib untuk menutup (close) kembali

# Silahkan di run dan lihat hasilnya

# 2. Cara membaca file.text
baca_dok = open('belajar.txt','r')
#print(baca_dok.read())       # Ini akan menampilkan file.text diatas dalam console
#print(baca_dok.read(5))       # hanya akan membaca 5 karakter dalam file.txt
print(baca_dok.readline())     # Ini akan membaca file.txt baris per baris
print(baca_dok.readline())     # Untuk membaca baris berikutnya
baca_dok.close()

#3. Appending / menambahkan file.txt
dokumen2 = open('belajar.txt','a')
dokumen2.write('\nIni adalah baris terakhir')
dokumen2.close()