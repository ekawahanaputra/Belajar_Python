# LAMBDA FUNCTION
# Sebuah Fungsi

def opa (x,y):
    z = x + y
    return z

hasil = opa(5,10)
print(hasil)

# Contoh fungsi diatas bisa dibuat dengan lambda function, seperti berikut:
# Contoh penulisan :
#                    variable = lambda(argumen):print(argumen)

ore = lambda argumen: print(argumen)
ore('joss')
#====================================================

ozi = lambda x,y: x + y
print(ozi(10,5))

hasil = ozi(1,5)      # tak perlu memakai return
print(hasil)
#======================= SELESAI ====================