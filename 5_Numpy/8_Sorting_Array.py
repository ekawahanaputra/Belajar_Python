import numpy as np

a = np.floor(np.random.rand(1,5)*10)  
# .random.rand >> berfungsi untuk memunculkan array secara acak (random)
# floor        >> berfungsi untuk membuat array menjadi integer
# *10          >> berfungsi untuk mengkalikan array yang random dengan jumlah

print(a)

print("\n Nilai maximum dan minimum")
print("Nilai Maksimum dari a = ", a.max())
print("Posisi Maksimum dari a = ", a.argmax())
print("Nilai Minimum dari a = ", a.min())
print("Posisi Minimum dari a = ", a.argmin())

print("\nMengurutkan nilai dari a")
print(np.sort(a))     # secara default mengurutkan dari nilai yang kecil ke besar
print(np.argsort(a))  # mengurutkan index dari nilai a berdasarkan index awal
