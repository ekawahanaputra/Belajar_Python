# OPERASI KOMPARASI
# Operasi komparasi adalah membandingkan 2 buah / lebih nilai dari sebuah objek
# Misalkan :  a = 10
#             b = 9
# a & b disebut object sedangkan nilai 9 & 10 disebut nilai literal
# Hasil dari operasi komparasi adalah Type data Boolean
# Jenis - jenis operasi komparasi adalah :

# 1. Operasi Lebih Dari (>)
a = 10
b = 9
hasil1 = a > 3
hasil2 = b > 9

print (a, '> 3 = ',hasil1 )
print (b, '> 9 = ',hasil2 )

# 2. Operasi Kurang Dari (<)
a = 10
b = 9
hasil1 = a < 3
hasil2 = b < 11

print (a, '< 3 = ',hasil1 )
print (b, '< 11 = ',hasil2 )

# 3. Operasi Lebih Dari Sama Dengan (>=)
a = 10
b = 9
hasil1 = a >= 3
hasil2 = b >= 11
hasil3 = b >= 9

print (a, '>= 3 = ',hasil1 )
print (b, '>= 11 = ',hasil2 )
print (b, '>= 9 = ',hasil3 )

# 4. Operasi Kurang Dari Sama Dengan (<=)
a = 10
b = 9
hasil1 = a <= 10
hasil2 = b <= 11
hasil3 = b <= 3

print (a, '<= 10 = ',hasil1 )
print (b, '<= 11 = ',hasil2 )
print (b, '<= 3 = ',hasil3 )

# 5. Operasi Sama Dengan (==)
a = 10
b = 9
hasil1 = a == 10
hasil2 = b == 10

print (a, '== 10 = ',hasil1 )
print (b, '== 10 = ',hasil2 )

# 6. Operasi Tidak Sama Dengan (!=)
a = 10
b = 9
hasil1 = a != 10
hasil2 = b != 10

print (a, '!= 10 = ',hasil1 )
print (b, '!= 10 = ',hasil2 )

# 7. Operasi is (is)
a = 10
b = 9
c = 10
hasil1 = a is b
hasil2 = a is c

print ('a is b = ',hasil1 )
print ('a is c = ',hasil2 )

# 7. Operasi is not (is not)
a = 10
b = 9
c = 10
hasil1 = a is not b
hasil2 = a is not c

print ('a is not b = ',hasil1 )
print ('a is not c = ',hasil2 )

# Note : Khusus untuk operasi 'is' dan operasi 'is not' , -->
# hanya boleh digunakan untuk mengcompare sesama object.
# 'is' & 'is not' tidak diperkenankan digunakan untuk mengkomparasikan -->
# objek dan nilai literal maupun sesama nilai literal