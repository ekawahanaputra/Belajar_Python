# QUEUES
# Queues tidak jauh berbeda dengan stacks. Hanya saja pada queues
# bisa diibaratkan seperti nomer antrian. Siapa yang pertama
# itulah yang keluar duluan.
# untuk Queues pada python harus mengimport library
# CONTOH
from collections import deque        # Ini adalah import library

antrian = deque([1,2,3,4,5])           # memakai deque( [ list ] )
print('Antrian saat ini ', antrian,'\n')

# Ketika antrian dimasukan
antrian.append(6)
print('Antrian saat ini ', antrian,'\n')

antrian.append(7)
print('Antrian saat ini ', antrian,'\n')

# Ketika antrian dipanggil dan berkurang
a = antrian.popleft()
print('Antrian No ',a,' dipanggil')
print('Antrian saat ini ', antrian,'\n')

a = antrian.popleft()                # Menggunakan variable.popleft() untuk mengurangi antrian
print('Antrian No ',a,' dipanggil')
print('Antrian saat ini ', antrian,'\n')

# Saat antrian dimasukan lagi
antrian.append(8)
print('Antrian saat ini ', antrian,'\n')

# Begitulah program berjalan seterusnya sesuai antrian
# =============== SELESAI =========================================