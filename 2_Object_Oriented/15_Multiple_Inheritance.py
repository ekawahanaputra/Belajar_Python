# MULTIPLE INHERITENCE
# adalah sebuah metode yang berguna untuk memungkinkan programer mengherit / menurunkan sebuah SubClass
# dari 2 atau lebih SuperClass sekaligus
# Contoh Syntax:

class A:

    def method_A(self):
        print('Ini adalah method A pada superClass A')

class B:

    def method_B(self):
        print('Ini adalah method B pada superClass B')

class C (A,B):   #//------>> Cara multiple inheritence

    pass

object = C()


# Lihat lah hasil display
object.method_A()
object.method_B()

# Meskipun object adalah milik class C, tapi biasa menampilkan method_A pada class A dan method_B pada class B