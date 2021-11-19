import numpy as np

a = np.array(([2,3,4], [4,3,2]))
b = np.ones([3,2])

print('Matrik a :\n', a)
print('\nMatrik b :\n', b)

# Cara perkalian matrix
hasil = np.dot(a,b)   #====>>>> Caranya

print('\nHasil kali matrik a dan matrik b adalah :\n', hasil)

# SELESAI