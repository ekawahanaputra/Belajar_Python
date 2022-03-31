# INFO :  materi ini (no.9) masih sama dengan materi no.8 Sorting Array
import numpy as np

a = np.floor(np.random.rand(2,3)*10)  

print(a)

print("\nNilai maximum dan minimum")
print("Nilai Maksimum dari a = ", a.max())
print("Posisi Maksimum dari a = ", a.argmax())
print("Nilai Minimum dari a = ", a.min())
print("Posisi Minimum dari a = ", a.argmin())

print("\nMengurutkan nilai dari a")
print(np.sort(a))     # untuk matrix, diurutkan dari baris per baris. baris satu dulu, baru baris dua
print(np.argsort(a))