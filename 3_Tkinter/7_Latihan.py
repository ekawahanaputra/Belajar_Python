# MEMBUAT FORM REGRISTRASI SEDERHANA

from tkinter import*

class Tulisan:

    def __init__(self, master):
        self.master = master

        tulisan1 = Label(root, text = 'FORM REGRISTRASI', bg = 'Grey', fg = 'White')
        tulisan2 = Label(root, text = 'Nama')
        tulisan3 = Label(root, text = 'email')
        tulisan4 = Label(root, text = 'No. HP')
        

        tulisan1.grid(row = 0, column = 0)
        tulisan2.grid(row = 1, column = 0)
        tulisan3.grid(row = 2, column = 0)
        tulisan4.grid(row = 3, column = 0)

class Kolom_Entry:

    def __init__(self,master):

        entry1 = Entry(root)
        entry2 = Entry(root)
        entry3 = Entry(root)

        entry1.grid(row = 1, column = 1)
        entry2.grid(row = 2, column = 1)
        entry3.grid(row = 3, column = 1)

class Tombol:

    def __init__(self, master):

        tombol1 = Button(root, text = 'REGISTER', fg = 'Blue', bg = 'Orange', command = self.click)
        tombol1.grid(sticky = 'n')

    def click(self):
        tulisan5 = Label(root, text = 'SELAMAT ANDA SUDAH MELAKUKAN REGRISTRASI')
        tulisan5.grid(columnspan = 2)


root = Tk()

word = Tulisan(root)
entry = Kolom_Entry(root)
tombol = Tombol(root)

root.mainloop()