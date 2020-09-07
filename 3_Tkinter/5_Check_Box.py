from tkinter import*

root = Tk()

label1 = Label(root, text = 'Pilih jenis kelamin anda !')
check1 = Checkbutton(root, text = 'Laki - laki')
check2 = Checkbutton(root, text = 'Perempuan')

label1.grid(row = 0, column = 0)
check1.grid(columnspan = 1, sticky = 'w')
check2.grid(columnspan = 1, sticky = 'w')

root.mainloop()

# Note :
#           Checkbutton()     ==>>  berfungsi untuk membuat checkbutton
#           columnspan        ==>>  berfungsi untuk meletakan check1, untuk aturannya caranya masih dipelajari !!!!!
#           sticky            ==>> berfungsi untuk meletakan check1, dengan parameter string : n, s, w, e  -->> n -> north, s -> south, w -> west, e -> east

# ========= SELESAI ==================