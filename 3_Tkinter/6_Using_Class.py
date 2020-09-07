from tkinter import*

class Tombol:

    def __init__(self, objek):
        self.objek = objek

        tombol1 = Button(root, text ='Klik tombol ini',command = self.click_tombol1)
        tombol2 = Button(root, text = 'Exit', command = root.quit)
        tombol2.grid(row = 0, column = 1)
        tombol1.grid(row = 0, column = 0)



    def click_tombol1(self):
        label = Label(root, text = 'Selamat anda berhasil membuat program GUI')
        label.grid(row = 1, column = 0)


root = Tk()

execute = Tombol(root)    # menjalankan program -->> formatnya -->> Object = Class(argumen)

root.mainloop()

# Note :
#           root.quit   in line 9  ==>> berfungsi untuk menjalankan perintah keluar jika tombol2 di klik

# =========  SELESAI  ===================