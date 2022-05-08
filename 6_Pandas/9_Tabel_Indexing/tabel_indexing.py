import pandas as pd

dataKu = pd.read_excel("sumber.xlsx")
print(dataKu, "\n\n")
print(dataKu.describe(), "\n\n")


# CARA SEDERHANA
# Cara memilih kolom 1 kolom
dataBaru = dataKu["Plant"]     # ==>> "Plant" adalah nama kolom yg terdapat pada data
print(dataBaru)
print(type(dataBaru), "\n\n")

# NOTE : data dengan satu kolom disebut series (lihat type dataBaru diatas)
#        sedangkan data dengan lenih dari satu kolom disebut dataframe (lihat contoh dibawah)

# Cara memilih kolom lebih dari satu
dataBaru2 = dataKu[["Plant", "EquipmentNo", "Time Delivery Reschedule"]]
print(dataBaru2)
print(type(dataBaru2), "\n\n")



# ILOC mengindex data berdasarkan nomer index
# Cara memilih 1 baris
print(dataKu.iloc[1], "\n\n")   # ==>> '1' merupakan baris dengan index ke 1

# Cara memilih lebih dari satu baris
print(dataKu.iloc[2 : 5], "\n\n")  # ==>> < 2 : 5 > artinya memilih baris dari index 2 sampai index 5

# Cara memilih baris dan kolom
print(dataKu.iloc[: , 3], "\n\n")  # ==>> ' : '  artinya memilih semua baris / kolom
print(dataKu.iloc[3 , 3], "\n\n")  # ==>> 3 , 3 artinya mengambil nilai bada baris 3 dan kolom 3

# NOTE : jika nilai indexing bernilai negatif (-), maka indexing dihitung dari belakang data
