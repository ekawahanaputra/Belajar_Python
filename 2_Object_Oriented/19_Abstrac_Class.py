# ABSTRACK CLASS
# Perbedaan abstrack class dan class biasa adalah:
# Abstrack class adalah blueprint atau template dari class class
# sedangkan class biasa adalah blueprint / template dari object object
# Contoh pembuatan class abstrack

from abc import ABC, abstractmethod

# abc adalah singkatan dari abstrack base class - adalah sebuah module dari python

class Button (ABC):                         # 1. buat super class yang di inheritence dari module ABC

    @abstractmethod                         # 2. aplikasikan @abstrackmethod seperti syntax disebelah
    def click(self):
        pass

class push_Button(Button):                  # 3. buatlah sebuah subclass yang di inheritence dari superClass Button beserta fungsinya
    
    def click(self):
        print('Push Button')

class select_Radio(Button):

    def click(self):
        print('Putar Radio')


tombol1 = select_Radio()
tombol2 = push_Button()


# Display

tombol2.click()
tombol1.click()

# Penggunaan abstrack class akan memaksa agar sebuah fungsi dapat langsung diakses dari class nya sendiri meskipun class
# tersebut sudah di Inheritence dari Super Class yang lain