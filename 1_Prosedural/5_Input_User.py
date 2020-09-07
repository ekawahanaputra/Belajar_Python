# CARA MENGINPUT DATA USER

#Contoh 1
Data_Nama = input("Input nama anda = ")
Data_Umur = input("Input umur anda = ")
#note : jika di run, tipe data input pasti menjadi string

#Contoh 2
#Agar tipe data input berubah menjadi tipe integer & float, -->
#input harus dirubah ke tipe data yang diinginkan
#penulisan sintax seperti dibawah :
Data_Anak = int(input("Input jumlah anak = "))
Data_Umur_Anak = float(input("Input umur anak anda = "))

#Contoh 3
#Agar tipe data input menjadi tipe boolean
Data_Biner1 = bool(input("Input jumlah total keluarga anda = "))
#Jika syntax input boolean seperti diatas,-->
#Berapa pun nilai inputnya, hasilnya akan tetap 'True'
#Maka khusus untuk input data boolean, type data boolean -->
#harus dikonversi dulu ke tipe integer. Seperti penulisan dibawah ini :
Data_Biner2 = bool(int(input("Input jumlah total keluarga anda = ")))



#HASIL PRINT
print("\nNama = ",Data_Nama ,type(Data_Nama))
print("Umur = ",Data_Umur ,type(Data_Umur))
print("Jumlah anak = ", Data_Anak, type(Data_Anak))
print("Umur anak = ", Data_Umur_Anak, type(Data_Umur_Anak))
print("Benarkah anda punya keluarga? = ", Data_Biner1, type(Data_Biner1))
print("Benarkah anda punya keluarga? = ", Data_Biner2, type(Data_Biner2))