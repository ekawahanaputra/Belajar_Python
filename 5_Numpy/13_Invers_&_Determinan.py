import numpy as np

a = np.array([(1,-1), (1,1)])
print("Matrik a = \n", a)
print("\n")


# INVERS MATRIX
a_invers = np.linalg.inv(a)
print("Invers dari matrik a adalah = \n", a_invers)

# Untuk membuktikan, a dikali a invers, hasilnya adalah matrik satuan

a_x_ainvers = np.dot(a, a_invers)
print("Hasil kali a dan a invers adalah =\n", a_x_ainvers)


# DETERMINAN MATRIX
det_a = np.linalg.det(a)
print("\nDeterminan dari a adalah =\n", det_a)

det_a_invers =np.linalg.det(a_invers)
print("Determinan dari a invers adalah =\n", det_a_invers)


#SELESAI*