# STACKS
# Stacks jika diibaratkan seperti ketika kita menumpuk buku,
# maka ketika buku buku tersebut kita ambil, maka kita akan
# mengambilnya dari atas, atau dari urutan terakhir kali
# ketika kita menambahkannya.
# COntoh ;

Books = [1,2,3,4,5]
print('Tumpukan buka awal ',Books,'\n')

Books.append(6)
print('Taruh lagi buku menjadi ',Books,'\n')

Books.append(7)
print('Taruh lagi buku menjadi ',Books,'\n')

a = Books.pop()    # variable.pop() = untuk mengurangi tumpukan secara stacks
print('Buku yang diambil adalah nomer ',a)
print('Maka buku menjadi ', Books,'\n')

# Itulah yang disebut Stacks
#==========================================================================


