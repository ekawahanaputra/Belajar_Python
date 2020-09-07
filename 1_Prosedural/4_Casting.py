# CASTING
# adalah merubah / mengkonversikan tipe data
# Jenis tipe data : int, float, bool, str

#DATA INTEGER

print("\n=====INTEGER to ALL=====")
data_int = 10
print("Nilai int 10 = ", data_int, "(dalam int)")

data_float = float(data_int)
data_string = str(data_int)
data_boolean = bool(data_int)
print("Nilai int 10 = ", data_float, "(dalam float)")
print("Nilai int 10 = ", data_string, "(dalam string)")
print("Nilai int 10 = ", data_boolean, "(dalam boolean)")
#note : nilai dalam boolean akan false jika nilai int = 0

#DATA FLOAT
print("\n=====FLOAT to ALL=====")
data_float = 10.9
print("Nilai float 10.9 = ", data_float, "(dalam float)")

data_int = int(data_float)
data_string = str(data_float)
data_boolean = bool(data_float)
print("Nilai float 10.9 = ", data_int, "(dalam integer)")
print("Nilai float 10.9 = ", data_string, "(dalam string)")
print("Nilai float 10.9 = ", data_boolean, "(dalam boolean)")
#nilai float dalam integer akan dilipatkan ke angka dibawah

#DATA STRING
print("\n=====STRING to ALL=====")
data_string = "Eka"
data_boolean = bool(data_string)
print("Nilai string Eka = ", data_string, "(dalam string)")
print("Nilai string Eka = ", data_boolean, "(dalam boolean)")

#khusus untuk integer dan float, nilai string harus berupa angka
#kalau berupa karakter akan error / tak bisa di eksekusi
data_string = "100"
data_int = int(data_string)
data_float = float(data_string)
data_boolean = bool(data_string)
print("Nilai string 100 = ", data_int, "(dalam integer)")
print("Nilai string 100 = ", data_float, "(dalam float)")
print("Nilai string 100 = ", data_boolean, "(dalam boolean)")
#note : nilai string dalam boolean akan false jika string kosong ("")

#DATA BOOLEAN

print("\n=====BOOLEAN to ALL=====")
data_boolean = False
print("Nilai boolean False = ", data_boolean, "(dalam boolean)")

data_int = int(data_boolean)
data_float = float(data_boolean)
data_string = str(data_boolean)
print("Nilai boolean False = ", data_int, "(dalam integer)")
print("Nilai boolean False = ", data_float, "(dalam float)")
print("Nilai boolean False = ", data_string, "(dalam string)")
