# DIAMOND PROBLEM
# diamond problem, penjelasannya masih berhubungan dengan Method Resolution Order pada episode sebelumnya
# hanya saja dengan kasus yang berbeda
# Contoh Kasusnya :

class A:

    def show(self):                         # 1. kita punya sebuah class A dan fungsinya yang bernama show
        print ('Ini adalah show class A')


class B (A):

    def show(self):                         # 2. kita punya class B dan fungsinya bernama show juga dan di inheritence dari class A
        print ('Ini adalah show class B')

class C (A):

    def show(self):                         # 3. kita juga punya class C dan fungsinya bernama show juga dan di inheritence dari class A juga
        print ('Ini adalah show class C')

class D (B,C):                              # 4. Terakhir kita punya class D yang di inheritence dari class B dan class C
    pass


# OBJECT
object = D ()


# DISPLAY

object.show()

# Yang mana kah yang akan ditampilkan oleh syntax object.show()   ????
# jawabannya bisa dilihat dengan syntax berikut:

# help(object)