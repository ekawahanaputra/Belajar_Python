import pandas as pd
import numpy as np


# COLUMNS SELECTION
# Menyeleksi kolom berdasarkan tipe data

baris = 5
kolom = 2
nama_kolom = ["bil_bulat", "bil_pecahan"]

dataframe = pd.DataFrame(np.random.randint(1, 20, size = (baris,kolom)), columns = nama_kolom)
dataframe["bil_pecahan"] = dataframe["bil_pecahan"].astype("float")
dataframe.index = pd.util.testing.makeDateIndex(baris, freq = "H") # baris ini untuk membuat index datetime dengan freqwensi "H" atau hours
dataframe = dataframe.reset_index()
dataframe["teks"] = list("abcde")

print("dataframe :")
print(dataframe)


# 1. Memilih kolom bertipe Number
print("\nkolom dengan tipe data number")
pilih_num = dataframe.select_dtypes("number")
print(pilih_num)

# 2. Memilih kolom bertipe float
print("\nkolom dengan tipe data float")
pilih_float = dataframe.select_dtypes(include = "float")
print(pilih_float)

# 3. Pilih kolom dengan tipe data datetime
print("\nkolom dengan tipe data datetime")
pilih_datetime = dataframe.select_dtypes(include ="datetime")
print(pilih_datetime)

# 4. Memilih kolom dengan kombinasi tipe data
print("\nkolom dengan tipe data kombinasi (object dan float)")
pilih_komb = dataframe.select_dtypes(["object", "float"])
print(pilih_komb)

#SELESAI