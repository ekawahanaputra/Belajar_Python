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

print(dataframe)
