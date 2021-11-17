import numpy as np

# 1 MEMBUAT VEKTOR
a = np.array ( [1, 2, 3, 4, 5] )
b = np.array ( [1.3, 2.7, 3.1, 4, 5] )



# 2 MEMBUAT VEKTOR DENGAN RANGE
c = np.arange (1, 10, 2)
d = np.arange (1, 5, 0.5)

    # Note :    1. Perhatikan perbedaan penulisan dalam membuat vektor dan vektor dengan range
    #           2. Format pembuatan vektor dengan range adalah : np.arange (angka_awal,  angka_akhir,  kelipatan)



# 3 MEMBUAT LINSPACE
e = np.linspace (1, 20, 3)

    # Note :    1. linespace ini bertujuan untuk menampilkan sebuah range angka / vektor menjadi beberapa bagian dengan jarak yang sama
    #           2. Format penulisan linspace adalah : np.linespace (angka_awal,  angka_akhir,  jumlah_angka_yang_ditampilkan)
    #           3. Misal contoh: np.linspace (1, 20, 3) ===>> ini akan menampilkan angka denga range 1 sampai 20 menjadi 3 bagian dengan jarak yang sama



# 4 MEMBUAT ARRAY MULTIDIMENSI ( MATRIK )

f = np.array ( [ (1 ,2 ,3), (4, 5, 6), (7, 8, 9) ] )

    # Note :    1. Format Penulisan array multidimensi adalah : np.array ( [ (angka-angka baris 1), (angka-angka baris 2), (dan seterusnya) ] )



# 5. MEMBUAT MATRIK DENGAN NILAI 0

g = np.zeros ( [6, 3] )

    # Note :    1. Format penulisan matrik dengan nilai semuanya 0 adalah : ( [ jumlah_baris, jumlah_kolom] )



# 6. MEMBUAT MATRIK DENGAN NILAI 1

h = np.ones ( [3, 6] )

    # Note :    1. Format penulisan sama dengan matrik nilai 0 semuanya

# 7. MEMBUAT MATRIK IDENTITAS
    # Ada 2 cara yaitu :

i = np.identity ( 3 )
j = np.eye ( 6 )

    # Note :    1. Matrik identity adalah matrik yang menampilkan nilai 0, namun juga menampilkan nilai 1 secara diagonal
    #           2. Format penulisannya ada 2, bisa pake np.identity, maupun np.eye dengan format ( jumlah baris dan kolom )



# DISPLAY
print('======== Ini Adalah Vektor ==========')
print(a)
print(b, '\n')

print('======== Ini Adalah Vektor dengan Range')
print(c)
print(d,'\n')

print('======== Ini Adalah Linspace ========')
print(e, '\n')

print('======== Ini Adalah Array Multidimensi / Matrik ============')
print(f,'\n')

print('======== Ini Adalah Matrik dengan Nilai 0 ==========')
print(g, '\n')

print('======== Ini adalah matrik dengan nilai 1 semua ==========')
print(h, '\n')

print('======== Ini adalah matrik identitas =========')
print(i,'\n')
print(j)