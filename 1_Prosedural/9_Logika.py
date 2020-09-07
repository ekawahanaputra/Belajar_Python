# OPERATOR LOGIKA / BOOLEAN
# Pada operator logika, type data yang dipakai adalah boolean
# Operator logika ada 4 yaitu :
# 'not', 'or', 'and', 'xor.

# Operator 'NOT'
print ('=====NOT=====')
a = True
b = not a

print ('Nilai a = ',a)
print ('Nilai not a = ',b)


# Operator 'OR'
print ('\n=====OR=====')
a = False
b = False
c = a or b
print (a, 'or', b, '=', c)

a = False
b = True
c = a or b
print (a, 'or', b, '=', c)

a = True
b = False
c = a or b
print (a, 'or', b, '=', c)

a = True
b = True
c = a or b
print (a, 'or', b, '=', c)


# Operator 'AND'
print ('\n=====AND=====')
a = False
b = False
c = a and b
print (a, 'and', b, '=', c)

a = False
b = True
c = a and b
print (a, 'and', b, '=', c)

a = True
b = False
c = a and b
print (a, 'and', b, '=', c)

a = True
b = True
c = a and b
print (a, 'and', b, '=', c)


# Operator XOR (^)
print ('\n=====XOR=====')
a = False
b = False
c = a ^ b
print (a, 'xor', b, '=', c)

a = False
b = True
c = a ^ b
print (a, 'xor', b, '=', c)

a = True
b = False
c = a ^ b
print (a, 'xor', b, '=', c)

a = True
b = True
c = a ^ b
print (a, 'xor', b, '=', c)