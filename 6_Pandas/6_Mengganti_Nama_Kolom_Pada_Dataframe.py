import pandas as pd
import numpy as np

# Mengganti nama kolom (label) pada dataframe
baris = 3
kolom = 3
label = tuple("ABC")

# dataframe
print("dataframe")
dataframe = pd.DataFrame(np.random.randint(1, 9, size = (baris, kolom)), columns = label)
print(dataframe)

# mengganti nama kolom (label)
# mengganti nama kolom "A" menjadi "Angka"
print("\n")
print(dataframe.rename(columns = {"A" : "Angka"}))


# mengganti lebih dari satu nama kolom (multiple)
print("\n")
print(dataframe.rename(columns = {"B" : "Bil", "C" : "Cuk"}))