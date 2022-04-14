import pandas as pd

# Kali ini adalah cara untuk mengkonversikan dataframe dari string ke numerik

data = {"A" : ["1","2","3","text"],
        "B" : ["4","5","6","7"]}

# dataframe
print("dataframe :")
dataframe = pd.DataFrame(data)
print(dataframe)

print("\ntipe dataframe :")
print(dataframe.dtypes)
# lihat hasilnya


# KONVERSI
# 1. Konversi data dalam satu kolom saja 
data_konversi_1= dataframe.astype({"B" : "int"}) # mengginakan astype, selain int, bisa juga memakai float, bol, dll
print("\ndataframe yang kolom B dikonversi ke integer")
print(data_konversi_1)
print("\ntipe data konversi 1")
print(data_konversi_1.dtypes)

# untuk data pada kolo A3 "text", tidak dapat dikonversikan ke numerik karena bersifat string
# jika dipaksakan, maka output program akan error

# 2. Konversi data untuk semua dataframe
data_konversi_2 = dataframe.apply(pd.to_numeric, errors = "coerce")
print("\nsemua dataframe dikonversikan")
print(data_konversi_2)
print("\ntipe data konversi")
print(data_konversi_2.dtypes)

# note = "errors = "coerce" maksudnya, apabila ada data string yang tidak bisa dikonversikan ke 
#        numeric, maka akan ditampilkan keterangan "Nan"

# SELESAI