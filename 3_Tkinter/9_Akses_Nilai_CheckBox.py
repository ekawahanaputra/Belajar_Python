# Cara Mengakses nilai Checkbox
from tkinter import*

def Click():
    if var1.get() == True:
        print('Badminton')
        jwb1 = Label(main, text = 'Badminton')
        jwb1.pack(side = BOTTOM)
    if var2.get() == True:
        print('Football')
        jwb2 = Label(main, text = 'Football')
        jwb2.pack(side = BOTTOM)
    if var3.get() == True:
        print('Cycling')
        jwb3 = Label(main, text = 'Cycling')
        jwb3.pack(side = BOTTOM)
    if var4.get() == True:
        print('Volley')
        jwb4 = Label(main, text = 'Volley')
        jwb4.pack(side = BOTTOM)

main = Tk()

soal = Label(main, text = 'Pilihlah hobi yang anda suka dibawah ini!')
soal.pack(side = TOP)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

choice1 = Checkbutton(main, text = 'Badminton', variable = var1)
choice1.pack(side = LEFT)

choice2 = Checkbutton(main, text = 'Football', variable = var2)
choice2.pack(side = LEFT)

choice3 = Checkbutton(main, text = 'Cycling', variable = var3)
choice3.pack(side = LEFT)

choice4 = Checkbutton(main, text = 'Volley', variable = var4)
choice4.pack(side = LEFT)

tombol = Button(main, text = 'Proses', command = Click)
tombol.pack(side = BOTTOM)

main.mainloop()

# Langkah - Langkah
# 1. Buatlah program GUI seperti biasanya, berisi, Label, CheckButton, Tombol, dll (sesuai kebutuhan ; optional)
# 2. Pada saat pembuatan widget CheckButton, definisikanlah sebuah variabel dengan nama bebas sesuai kehendak anda -->> lihat line 32, 35, 38, 41
# 3. Definisikanlah variabel CheckButton sebagai "IntVar()" -->> lihat line 27 - 30
# 4. Pada fungsi Click (command of Button) gunakanlah metode logika(if, elif, else, dll), jika CheckButton dicentang, maka nilai <Variabel>.get() bernilai
#    "True". lihat line 5, 9, 13, dan 17
# 5. Selanjutnya anda bisa menampilkan nilai/value yang anda inginkan, jika suatu Checkbutton dicentang sesuai keinginan dan kreatifitas anda. Bisa 
#    menampilkannya di console, atau juga dalam bentuk label seperti contoh diatas, --- >> line 6 - 8, 10 -12, 14 - 16, dan 18 - 20
# 6. Anda juga bisa mengatur sedemikian rupa agar CheckButton hanya bisa dipilih salah satu saja. silahkan dicoba coba saja

#=========== SELESAI ==========