from tkinter import *

root = Tk()

# Label
label1 = Label(root, text = 'Nama')
label2 = Label(root, text = 'Alamat')
label3 = Label(root, text = 'No. HP')

# Entry
entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)

label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0)
label3.grid(row = 2, column = 0)

entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)
entry3.grid(row = 2, column = 1)

root.mainloop()

# Note :
#           grid()    ==>> berfungsi untuk meletakan label dengan format row dan column -->> grid(row = 0, column = 0)
#           Entry()   ==>> berfungsi untuk membuat kolom input (input box)

# =========== SELESAI =================