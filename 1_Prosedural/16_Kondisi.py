# OPERATOR KONDISI (IF, IF - ELSE, ELIF)

'''
Operator Kondisi ada 3 jenis. Yaitu :
1. kondisi 'if'
    <    if (operator komparasi):  
            print( )                >
'''
# PROGRAM MENGGUNAKAN IF
print('=====IF CONDITION=====')
a = int(input('Masukan umur anda : '))

if (a > 40):
    print('Anda sudah tua') # dieksekusi bila a > 40 = True

#===========================================================================
'''
2. kondisi 'if - else'
    <    if (operator komparasi):  
            print( )
         else:                     
            print( )                >
'''
# PROGRAM MENGGUNAKAN IF - ELSE
print('\n=====IF - ELSE=====')
b = int(input('Masukan umur anak anda : '))

if (b <= 5):
    print('Anak anda masih balita') # dieksekusi jika b <= 5 = True

else :
    print('Anak anda sudah besar') # dieksekusi jika b <= 5 = False

#===========================================================================
'''
3. kondisi 'elif'
    <    if (operator komparasi):
            print( )
       elif (operator komparasi):
            print( )                >
'''
# PROGRAM MENGGUNAKAN ELIF
print('\n=====ELIF=====')
c = int(input('Masukan nilai ujian anda : '))

if (c <= 5):
    print('Anda Goblok')

elif (c >= 6 and c <= 9):
    print('Anda Pintar')

elif (c == 10):
    print('Anda Super Duper Genius')

#==============SELESAI=====================================================