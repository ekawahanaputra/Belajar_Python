import numpy as np

# Contoh aritmatika pada list python
a = [1,2,3,4,5]
b = [2,4,6,8,10]
hasil_ab = a + b

print('\n== Hasil jumlah list python ==\n', hasil_ab)

# list python apabila diberi operasi tambah, akan menambahkan elemen list
# ==================================================================================


# ==== Aritmatika pada array numpy ====
c = np.array([1,2,3,4,5])
d = np.array([2,4,6,8,10])

# PENJUMLAHAN +
hasil_CplusD = c + d
print('\n\n== Hasil jumlah array numpy ==\n', hasil_CplusD)

# PENGURANGAN -
hasil_CminD = c - d
print('\n== Hasil kurang array numpy ==\n', hasil_CminD)

# PERKALIAN *
hasil_CkaliD = c * d
print('\n== Hasil kali array numpy ==\n', hasil_CkaliD)

# PEMBAGIAN /
hasil_CbagiD = c / d
print('\n== Hasil bagi array numpy ==\n', hasil_CbagiD)

# KUADRAT **
hasil_CkuadratD = c ** d
print('\n== Hasil kuadrat array numpy ==\n', hasil_CkuadratD)

# MODULUS %
hasil_CmodD = c % d
print('\n== Hasil Modulus array numpy ==\n', hasil_CmodD)

#===================================================================


# Aritmatika pada matrix
# PENJUMLAHAN
e = np.array([(1,2,3), (4,5,6), (7,8,9)])
f = np.array([(2,4,6), (8,10,12), (14,16,18)])
hasil_jml_ef = e + f

print('\n\n== Hasil jumlah matrix array ==\n', hasil_jml_ef)

# PERKALIAN
g = np.zeros([3,3])
h = np.ones([3,3])
hasil_kali_gh = g * h

print('\n\n== Hasil kali matrix array ==\n', hasil_kali_gh)

# SELESAI