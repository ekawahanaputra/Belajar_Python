# RETURN VALUE

def angka(x):
    total = x ** 3
    print('Nilai dari ', x,'kuadrat 3 adalah = ', total)
    return total

a = angka(2)          # return_value digunakan ketika anda ingin menggunakan 
print(a)              # nilai dari angka(2)

#=============================================================================

def variable(x,y):
    total = x + y
    print(x,' + ',y,' = ',total)
    return total      # penulisan return

b = variable(2,3)
print(b)

#======================== SELESAI ============================================