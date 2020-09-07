# METHOD RESOLUTION ORDER
# Teknik melakukan multiple inheritence jika nama method adalah sama

class A:

    def Info(self):
        print('Ini adalah method class A')

class B:

    def Info(self):
        print('Ini adalah method class B')

# Multiple Inheritence
class C (A,B):
    pass

object = C()

# Display Print

object.Info()

# Jika nama method class A dan Class B sama, maka ketika di print dan di run akan memunculkan method pada class A
# mengapa demikian? jawabannya bisa dilihat dengan menjalankan syntax berikut:

# help(object)

# jika syntax diatas di run , maka akan menampilkan urutan eksekusi dari multiple inheritence.
# Jadi KESIMPULANNYA adalah peletakan nama class pada multiple inheritence mempengaruhi urutan eksekusinya
# Contoh syntax :      class C (A,B):
#                      class C (B,A):

# Perbedaan penulisan syntax diatas akan menghasilkan urutan yang berbeda pula. Itulah kuncinya