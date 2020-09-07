import tkinter

jendela = tkinter.Tk()

def Type_Identitas():
    tulisan = tkinter.Label(jendela, text = 'Nama : Eka Wahana Putra')
    tulisan.pack()

tombol = tkinter.Button(jendela, text = 'Start', command = Type_Identitas)

tombol.pack()
jendela = tkinter.mainloop()