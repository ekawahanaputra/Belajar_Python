import pandas as pd

dataKu = pd.read_excel("SOURCE.xlsx")
print(dataKu)

print("-"*70)
print("\n")


# Untuk mengetahui ringkasan dari semua data
infoData = dataKu.info()
print(infoData)

print("-"*70)
print("\n")


# Untuk mendapatkan statistik diskriptif dari data
# 1. untuk tipe data yg bersifat numerik
print(dataKu.describe())
print("\n")


# 2. untuk tipe data yang bersifat string/object, gunakan ini
print(dataKu.describe(include = "O"))


# SELESAI
