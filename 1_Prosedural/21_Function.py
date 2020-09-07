# FUNCTION / FUNGSI
'''Function berfungsi untuk mempermudah / mempersingkat penulisan 
syntax program yang panjang'''

# CONTOH 1
# Mendeklarasikan function
def nama():
    print('nama saya adalah Eka')

# Menampilkan display dari function
nama()
#===================================================================
print('\n')

# Contoh 2
def jam_tersedia():
    print('jam tersedia')

def flaterate():
    jam_tersedia()           # Display jam tersedia juga bisa ditaruh pada function yang lain
    print('flaterate')

flaterate()

# Silahkan lihat perbedaan contoh 1 dan contoh 2
#===================================================================
print('\n')

# Contoh 3 - FUNCTION dengan input argumen
def harga_telur(kg):       # (kg) adalah input argumennya
    harga = 20000
    harga_total = harga * kg
    print('Harga total = ', harga_total)

harga_telur(2)

#===================================================================
print('\n')

# Contoh 4
def konversi(satuan_meter):
    print('1km sama dengan 1000 meter')
    Kilometer = 1000 * satuan_meter
    print(satuan_meter, ' kilometer = ', Kilometer, ' meter')

konversi(2)
konversi(3)
konversi(2.5)
konversi(1000)
konversi(250)
konversi(25)
# Dengan menggunakan function, kita dapat menampilkan display tanpa harus
# menulis banyak syntax

#========================== SELESAI ===============================