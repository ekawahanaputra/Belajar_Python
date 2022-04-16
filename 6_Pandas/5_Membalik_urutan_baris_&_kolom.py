import pandas as pd
import numpy as np

# Membalik urutan baris dan kolom
# Dataframe
baris = 5
kolom = 5
nama_kolom = tuple("abcde")

dataframe = pd.DataFrame(np.random.randint(1, 10, size = (baris, kolom)), columns = nama_kolom)
print("dataframe")
print(dataframe)


# Membalik urutan kolom
print("\nmembalik urutan kolom")
print(dataframe.loc[:, ::-1])
# .loc[:,::-1] maksudnya adalah:
# :    ===> baris nya tetap
# ::-1 ===> kolomnya dibalik dengan jarak satu(-1)


# Membalik urutan baris
print("\nmembalik urutan baris")
print(dataframe.loc[::-1, :])
# [::-1, 1]  bisa juga ditulis [::-1] saja. karena yg dibalik urutannya hanya barisnya saja


# Membalik urutan baris, tetapi index nya tetap
print("\nmembalik urutan baris dengan index tetap")
print(dataframe.loc[::-1].reset_index(drop =True))