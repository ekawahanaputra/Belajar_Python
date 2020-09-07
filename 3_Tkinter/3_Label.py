# Label adalah tulisan
from tkinter import *

root = Tk()
 
tulisan1 = Label(root, text = 'Judul Program', bg = 'Yellow', fg = 'Black')
tulisan2 = Label(root, text = 'Ini adalah baris kedua dari program', bg = 'Green', fg = 'Blue')
tulisan3 = Label(root, text = 'Ini adalah kolom vertikal dari program', bg = 'Pink', fg = 'Purple')
tulisan4 = Label(root, text = 'Ini adalah FULL BOTH', bg = 'red', fg = 'Black')



tulisan1.pack()
tulisan2.pack(fill = X)
tulisan3.pack(side = LEFT, fill = Y)
tulisan4.pack(side = RIGHT, fill = BOTH)

root.mainloop()


# Note :
#        Label()      -->> untuk menampilkan tulisan pada GUI
#        bg           -->> bg (background) menampilkan warna dari background
#        fg           -->> fg (fontground) menampilkan warna dari tulisan
#        fill         -->> untuk menempatkan posisi label. pilihannya : X --> full horizontal, Y --> full Vertical, BOTH -- full horizontal & Vertical
#        side         -->> menempatkan posisi Label. pilihannya : LEFT, RIGHT, TOP, BOTTOM

# =========== SELESAI ===============