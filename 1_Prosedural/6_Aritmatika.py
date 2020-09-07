# OPERASI ARITMATIKA


# Operasi penjumlahan (+)
a = 2
b = 3
hasil1 = a + b

print (a, "+", b, "= ",hasil1)


# Operasi pengurangan (-)
a = 4
b = 3.5
hasil1 = a - b

print (a, "-", b, "= ",hasil1)


# Operasi perkalian (*)
a = 4
b = 3
hasil1 = a * b

print (a, "x", b, "= ",hasil1)


# Operasi pembagian (/)
a = 6
b = 2
hasil1 = a / b

print (a, "/", b, "= ",hasil1)


#Operasi Eksponen / pangkat (**)
a = 6
b = 3
hasil1 = a ** b

print (a, "**", b, "= ",hasil1)


#Operasi modulus (%)
a = 15
b = 4
hasil1 = a % b

print (a, "%", b, "= ",hasil1)
# Note : Modulus adalah operasi matematika dimana hasilnya adalah sisa dari pembagian


#Operasi floor division (//)
a = 15
b = 2
hasil1 = a // b

print (a, "//", b, "= ",hasil1)
# Note : pada operasi ini, hasil dari pembagian dibulatkan ke angka yang lebih kecil


#Operasi Prioritas
x = 3
y = 7
z = 4

hasil = x / y // z * y + (x - y) % 2 ** 3

print (x, "/" ,y, "//" ,z, "* ",y, "+ (",x, "-" ,y,") %" ,2, "**" ,3,"=", hasil)
# Note : untuk operasi prioritas seperti diatas, adapun urutan -->
# operasi yang diselesaikan terlebih dahulu adalah sebagai berikut :
# 1. operasi dalam kurung ' (---) '
# 2. operasi exponen ' ** '
# 3. operasi perkalian / pembagian / modulus /floor dev ' *, /, %, // '
# 4. operasi pertambahan / pengurangan ' +, - '