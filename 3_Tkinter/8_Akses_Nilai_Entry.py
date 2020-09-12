# Cara mengakses nilai Entry
from tkinter import*

def Click():
    ouput_entry = inputen.get()
    tulisan2 = Label(root, text = ouput_entry)
    tulisan2.pack()
    print(ouput_entry)

root = Tk()

tulisan1 = Label(root, text = 'Masukan inputan anda !')
tulisan1.pack()

inputen = StringVar()
inputan1 = Entry(root, width = 30, textvariable = inputen)              
inputan1.pack()


tombol1 = Button(root, text = 'Click Here', command = Click)
tombol1.pack()

root.mainloop()

# Langkah langkah
# 1. buatlah program GUI seperti biasa berisi Label, Entry, dan Tombol beserta fungsi untuk mengeksekusinya  --> isi gui hanya optional saja
# 2. pada pembuatan Entry, buatlah sebuah variabel dalam bentuk textvariabel --> lihat line 17 (nama variabel bebas)
# 3. definisikan textvariabel pada Entry sebagai sebuah StringVar(). mengindikasikan bahwa textvariabel Entry adalah berupa Teks/String --> lihat line 16
# 4. kemudian pada fungsi command Click, definisikan sebuah variabel baru (nama bebas) dengan nilai "<textvariable>.get()" --> lihat line 5
# 5. tampilkanlah output atau nilai/value dari Entry bisa dengan Label -->> line 6, atau bisa juga menampilkannya di console run -->> line 8, atau
#    bisa juga dengan cara lainnya(terserah anda)

#========= SELESAI ===============
