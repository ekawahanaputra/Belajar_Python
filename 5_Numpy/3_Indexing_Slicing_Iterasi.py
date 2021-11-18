import numpy as np

a = np.arange(5,20)

# IDNDEXING
# Adalah proses dari pengambilan nilai dari suatu array. Prosesnya sama seperti
# pengambilan nilai list pada python
print('==== INDEXING ====')
print('nilai ke 1 dari a adalah :', a[0])
print('nilai ke 3 dari a adalah :', a[2])
print('nilai akhir dari a adalah :', a[-1])
print('nilai akhir ke 2 dari a adalah :', a[-2])
# kalau mengambil dari akhir, dimulai dari -1, -2 , dst


# SLICING
# Adalah proses dari pengambilan rentang nilai dari array
print('\n==== SLICING ====')
print('nilai ke 2 sampai 5 dari a adalah :', a[1:5])
print('nilai ke 4 sampai akhir dari a adalah :', a[3:])
print('nilai awal sampai ke 7 dari a adalah :', a[:7])


# ITERASI
# Pengambilan nilai dengan pengulangan
print('==== ITERASI ====')
x = 0
for nilai in a:
    x += 1
    print('Nilai ke ',x, '= ', nilai)

# ==== SELESAI ====