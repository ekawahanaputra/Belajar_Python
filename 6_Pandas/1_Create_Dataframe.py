import pandas as pd
import numpy as np


# Pada tutorial ini akan membahas tentang cara membuat dataframe

baris = 5
kolom = 6
nama_kolom = tuple('ABCDE')

data = pd.DataFrame(np.random.randint(1,6, size=(kolom,baris)), columns = nama_kolom)

# np.random.randitn untuk mengacak nomer secara random

print(data)