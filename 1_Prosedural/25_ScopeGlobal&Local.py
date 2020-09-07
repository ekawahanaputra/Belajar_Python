# Scope LOKAL
namaAnjing = 'Blacky'

def ubah_nama_anjing(namaBaru):
    namaAnjing = namaBaru
    print('Nama anjing saya setelah dirubah adalah ',namaAnjing)

ubah_nama_anjing('Jinggo') # print variable pada fungsi (lokal)
print('Nama anjing saya setelah dirubah adalah ',namaAnjing)  # print variable global
# hasil print yang kedua tidak akan merubah nilai variable global
#====================================================================================
# Scope GLOBAL
print('\n')
# Untuk merubah variable lokal menjadi global

buah = 'Apel'

def GantiBuah(BuahBaru):
    global buah            # tambahkan 'global' untuk menjadikan variable lokal
    buah = BuahBaru        # menjadi global. Sehingga variable bisa dirubah
    print('Nama buah setelah dirubah ',buah)

GantiBuah('Jeruk')
print('Nama buah setelah dirubah ',buah)
# hasilnya bisa dilihat saat di run

'''
NOTE :
global bisa ditulis seperti ini juga :
"global variable_baru1, variable_baru2"
jika variable yang akan dirubah lebih dari satu
'''
#===================================================================================

