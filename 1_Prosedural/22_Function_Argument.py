# Fungsi Argument
# 1. Argumen Sederhana

def mekanik(nama, NRP, masa_kerja):       # nama, NRP, masa_kerja disebut argumen
    print('Nama mekanik : ', nama)
    print('NRP : ', NRP)
    print('masa kerja : ', masa_kerja)

mekanik('Yoga', 24655, '5 Tahun')         # Cara menampilkan adalah dengan menampilkan
print('\n')                               # nilai dari semua argumen
mekanik('Ikshan', 23567, '3 Tahun')
#=========================================================================
print('\n')
# 2. Argumen dengan Keyword
# nilai dari argumen ditetapkan saat display

def Foreman(nama,training):
    print('Nama mekanik : ', nama)
    print('Training Terakhir : ', training)

Foreman(nama = 'Eka', training = '3 DT')        # Cara Menampilkan seperti disamping
Foreman(training = 'Master', nama = 'Budi')     # Meski penulisan argumen dibalik, hasil print tetap sesuai urutan pada def

Foreman('Arpi','2 DT')                          # Perbedaannya jika penulisannya seperti disamping
Foreman('2 DT', 'Arpi')                         # Jika di balik akan ngaco! Di coba aja di RUN
#=========================================================================
print('\n')
# 3. Argument dengan default argument
# Argument yang nilainya sudah ditetapkan saat pendeklarasian fungsi
def keluarga(Nama = 'Eka', Umur = 29, Pekerjaan = 'Swasta'):
    print('Nama : ', Nama)
    print('Umur : ', Umur)
    print('Pekerjaan : ', Pekerjaan)

keluarga('Eka')
keluarga('Yofi', Umur = 30)       # Nilai bisa dirubah saat display
#keluarga(Umur = 30, Pekerjaan = 'Swasta') ==>> akan error karena nilai dari nama belum ditentukan
keluarga()
keluarga(Umur = 25, Nama ='Arga') # Posisi juga dapat ditukar
#================================= Selesai ================================