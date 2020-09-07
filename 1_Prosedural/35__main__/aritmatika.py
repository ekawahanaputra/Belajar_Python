# Variable __main__ dan variable __name__

def tambah(a,b):
    c = a + b
    print(a,'+',b,'=',c)

def kurang(a,b):
    c = a - b
    print(a,'-',b,'=',c)

def kali(a,b):
    c = a * b
    print(a,'x',b,'=',c)

def bagi(a,b):
    c = a / b
    print(a,':',b,'=',c)

def modulus(a,b):
    c = a % b
    print(a,'mod',b,'=',c)

def floor_dev(a,b):
    c = a // b
    print(a,'//',b,'=',c)

# didalam bahasa pemrograman python, terdapat sebuah variable unik yaitu '__name__'
# Variable ini berfungsi ketika kita bekerja dengan modul modul
# mari kita coba melakukan print(__name__):
print(__name__)

# Jika di run di dalam file program ini (utama), __name__ akan menjadi __main__ (class str)
# Namun cobalah untuk melakukan run pada program file main.py dengan cara import.
# hasilnya akan muncul nama file utama, dimana file itu diimport. Silahkan dicoba!!

# Fungsi dari variable __main__ dan __name__ adalah jika kita ingin agar satu atau beberapa
# fungsi tidak ditampilkan pada program file main.py ketika melakukan import
# Caranya adalah seperti dibawah:

bagi(5,2)
if __name__ == '__main__':
    modulus(20,3)

# Dengan syntax diatas, jika di run pada file ini (aritmatika.py) bagi(5,2) & modulus(20,3)
# akan diakses
# namun jika syntax diatas di run di file main.py dengan cara import, hanya bagi(5,2) yang ditampilkan
# modulus(20,3) tidak akan diakses
# SILAHKAN DICOBA

#=========================== SELESAI ===============================================





