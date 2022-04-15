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