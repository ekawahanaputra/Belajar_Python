# Cara membuat GUI dengan Built in Package Tkinter
# Karena Tkinter merupakah salah satu package dari python, maka untuk menggunakannya harus import dulu

import tkinter

jendela_utama = tkinter.Tk()      #ini untuk membuat window / jendela GUI

# Ini adalah sebuah method yang muncul jika tombol ditekan
def jika_tombol_ditekan():
    tulisan2 = tkinter.Label(jendela_utama, text = 'Kamu Monyet ^_^"')
    tulisan2.pack()

# Membuat tulisan didalam jendela
tulisan = tkinter.Label(jendela_utama, text = 'Om Swastiastu')

# Membuat tombolnya
tombol = tkinter.Button(jendela_utama, text = 'Tekan Aku', command = jika_tombol_ditekan)


# Pastikan menulis syntax .pack()
tulisan.pack()
tombol.pack()

jendela_utama.mainloop()          #ini agar GUI looping terus menerus selama yg diinginkan

# Silahkan di run. Window GUI akan muncul

