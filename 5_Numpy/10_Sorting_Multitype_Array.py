# INFO : Lanjutan dari materi no 8 dan no 9, tentang sorting array
import numpy as np

# Cara membuat multitype array
dtipe = [("nama siswa", "S10"),("nilai", int)] # format >> [(variable, jumlah string(S10),(nilai variabel, tipe data))]

data = [
    ("Agus", 80),
    ("Rio", 40),
    ("Jojo", 10),
    ("Surya", 50)
]

a = np.array(data, dtype = dtipe)
print(a)

print("\nMengurutkan a berdasarkan nilai yang diperoleh siswa")
print(np.sort(a, order="nilai"))

print("\nMengurutkan a berdasarkan nama siswa")
print(np.sort(a, order="nama siswa"))

# mengambil nilai salah satu multiple array
print("\n", a[1])
