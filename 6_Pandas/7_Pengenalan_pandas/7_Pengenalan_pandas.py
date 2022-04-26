import pandas as pd

# PENGENALAN PANDAS

# Membaca File (dengan cara sederhana)

bacaFileXL = pd.read_excel("SOURCE.xlsx") # Parameter juga bisa ditambahkan   "sheet_name = <<nama sheet>>"
print("Hasil dari membaca file excel")
print(bacaFileXL, "\n")


# Membaca 5 data teratas
print("5 data teratas")
print(bacaFileXL.head(), "\n")


# Membaca 5 data terbawah
print("5 data terbawah")
print(bacaFileXL.tail(), "\n")



# Mengekspor File
bacaFileXL.to_csv("fileekspor.csv", index=False)
# lihat hasilnya di direktory
'''
Note :
    "index = False"   >> bertujuan agar nomer index baris tidak 
                         dieksekusi menjadi bagian dari kolom
                         pada file tujuan. Jika nilai index tidak 
                         dimasukan, nilai defaultnya adalah "True" 
'''


# Selain itu, pandas juga bisa membaca dan mengekspore file xls, odt, xlsx, csv, html, sql dan lain2
# Pelajarilah sesuai kebutuhan