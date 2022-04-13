import pandas as pd
import numpy as np

# Rows Selection
# adalah cara untuk mencari atau menseleksi baris dari dataframe dengan nilai tertentu

# dataframe
baris = 7
kolom = 6
nama_kolom = tuple("abcdef")

dataframe = pd.DataFrame(np.random.randint(1, 10, size = (baris, kolom)), columns = nama_kolom)
print(dataframe,"\n")



# Rows Selection
# contoh 1 : kita mencari baris (row) yang bernilai 5 pada kolom a

rows_select_1 = dataframe[dataframe['a'] == 5]
print("Baris dengan nilai 5 di kolom a\n")
print(rows_select_1)
print("\n")


# contoh 2 : mencari baris yang bernilai 7 atau 3 di kolom b
rows_select_2 = dataframe[(dataframe["b"] == 7) | (dataframe["b"] == 3)]
print("Baris dengan nilai 7 atau 3 di kolom b\n")
print(rows_select_2)
print("\n")


# contoh 3 : ada cara lebih mudah untuk contoh nomer 2 diatas
# menggunakan fungdi "isin()"
rows_select_3 = dataframe[dataframe["c"].isin([7,3])]
print("Baris dengan nilai 7 dan 3 di kolom c (dengan cara yang berbeda)\n")
print(rows_select_3)
print("\n")


# contoh 4 : mencari baris yang tidak bernilai 5 atau 2 di kolom d
# menggunakan "~"
rows_select_4 = dataframe[~dataframe["d"].isin([5,2])]
print("Baris dengan nilai bukan 5 atau 2 di kolom d\n")
print(rows_select_4)
print("\n")

#SELESAI