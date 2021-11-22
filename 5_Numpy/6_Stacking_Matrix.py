import numpy as np

# Stacking Matrix = adalah proses menumpuk matrik ataupun array

array_a = np.array([8,9,10])
array_b = np.array([1,2,3])

stack_AB_h = np.hstack((array_a, array_b))  # hstack ==>> stacking (menumpuk) secara horizontal
print('\nStacking Array Horizontal')
print(stack_AB_h)

stack_AB_v = np.vstack((array_a, array_b))  # vstack ==>> stacking (menumpuk) secara vertical
print('\nStacking Array Vertical')
print(stack_AB_v)


# Contoh operasa stacking pada matrik
matrik_a = np.zeros([3,4])
matrik_b = np.ones([3,4])

stack_Matrik_AB_h = np.hstack((matrik_a, matrik_b))
print('\nStacking Matrik Horizontal')
print(stack_Matrik_AB_h)

stack_Matrik_AB_v = np.vstack((matrik_a, matrik_b))
print('\nStacking Matrik Vertical')
print(stack_Matrik_AB_v)


# Note:
#       Hati hati ketika menentukan ukuran matrik (baris & kolom) sebelum melakukan stacking

# SELESAI