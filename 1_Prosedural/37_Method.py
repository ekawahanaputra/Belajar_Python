# Membuat method
# Method tidak berbeda jauh dengan function
# Method adalah function yang menempel pada class
# Sedangkan function berada diluar class
# Mari simak syntaxnya
class bendesa:            # ini adalah class
    pesengan = 'nama'     # ini adalah atribute
    yusa = 'umur'

    def kaluwarga(self):         # ini adalah method harus ada (self)
        print('Titiang warih bendesa manik mas ')
        print('Titiang subakti ring Hyang Kawitan ')

    def manira(self):            # menerangkan kegunaan self, dan bandingkan dengan method diatas
        print('wastan titiang',self.pesengan)

    def rupa(self,paras):        # method juga bisa ditambahkan argumen selain self
        print('Yusan titiang sampun',self.yusa, 'titiang nu', paras)


# Mendeklarasikan bahwa eka & sri adalah class bendesa
eka = bendesa()
sri = bendesa()

# Mendeklarasikan detail dari atribute
eka.pesengan = 'Eka Wahana Putra'
eka.yusa = 29
sri.pesengan = 'Sri Mariningsih'
sri.yusa = 28


# DISPLAY
eka.kaluwarga()    # untuk mengakses, ketikan eka.kaluwarga() [berbeda dengan fungsi]
sri.kaluwarga()

print('\n')

eka.manira()       # bandingkan hasil display dengan display diatas saat di run
sri.manira()

print('\n')

sri.rupa('jegeg') # cara display jika menambahkan argumen selain self
eka.rupa('bagus')