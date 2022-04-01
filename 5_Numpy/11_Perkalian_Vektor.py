import numpy as np

# Perkalian vektor ada 2 jenis :
#   1. Perkalian dot
#   2. Perkalian cross

# PERKALIAN dot
print("1. Perkalian dot 2 dimensi (x, y)")
a = np.array([1,3])
b = np.array([2,1])

c = np.dot(a,b)
print(c)

print("\nPerkalian vektor 3 dimensi (x, y, z)")
d = np.array([1,2,3])
e = np.array([3,2,1])

f = np.dot(d,e)
print(f)


# PERKALIAN cross
print("\nPerkalian vektor dengan cross")
# Perkalian cross bersifat 3 dimensi (x,y,z)

x = np.array([1,2,4])
y = np.array([3,2,5])

z = np.cross(x,y)
s = np.cross(y,x)

print(z)
print(s)
# Lihat perbedaan z & s