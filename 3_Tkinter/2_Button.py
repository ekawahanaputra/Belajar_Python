from tkinter import *

root = Tk()

# 1. Membuat Frame
topframe = Frame(root)    # frame adalah nama variable untuk Frame()
                          # Frame(root) artinya kita membuat sebuah frame / kerangka dan kita tempatkan di dalam root

buttonFrame = Frame(root) # Membuat frame tombol

# 2. Membuat Button
tombol1 = Button(buttonFrame, text = 'LEFT', fg = 'Purple')      # tombol1 adalah nama variable, Button() adalah class untuk membuat tombolnya
                                                                 # Button(frame, text = 'LEFT') artinya membuat Button didalam frame dengan tulisan LEFT

tombol2 = Button(buttonFrame, text = 'RIGHT', fg = 'Yellow')     # fg = 'Yellow' = membuat agar warna tulisan pada tombol menjadi kuning

tombol3 = Button(buttonFrame, text = 'BOTTOM', fg = 'Blue')
tombol4 = Button(buttonFrame, text = '    TOP    ', fg = 'Red')

topframe.pack()                           # menampilkan topFrame
buttonFrame.pack(side = BOTTOM)           # side = LEFT --->> Menampilkan buttonFrame di posisi BOTTOM
tombol1.pack(side = LEFT)
tombol2.pack(side = RIGHT)
tombol3.pack(side = BOTTOM)
tombol4.pack(side = TOP)

root.mainloop()

# SILAHKAN DI RUN dan LIHAT HASILNYA
# =============== SELESAI =================================