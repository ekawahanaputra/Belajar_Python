import pandas as pd
import numpy as np


# Pada tutorial ini akan membahas tentang cara membuat dataframe

baris = 5#
kolom = 6
nama_kolom = tuple('ABCDE')

data = pd.DataFrame(np.random.randint(1,6, size=(kolom,baris)), columns = nama_kolom)

# np.random.randitn untuk mengacak nomer secara random

print("1. Wujud dataframe : \n")
print(data)


# PREFIX
# imbuhan yang bisa ditambahkan di depan nama parameter kolom

kolom_prefix = data.add_prefix("kolom_")

print("\n2. Wujud dataframe dengan prefix :\n")
print(kolom_prefix)


# SUFFIX
# imbuhan yang ditambahkan di belakang nama parameter kolom

kolom_suffix = data.add_suffix("_adsen")

print("\n3. Wujud dataframe dengan suffix :\n")
print(kolom_suffix)

# SELESAI

# tes