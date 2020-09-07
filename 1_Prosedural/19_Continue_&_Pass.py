# Break, Continue, & Pass

# Break 
for a in range (0,10):
    print(a)
    if (a == 5):
        print('Angka ', a, 'di STOP')
        break      # break berfungsi untuk menghentikan looping dalam suatu kondisi
else:
    print('Ini adalah else')

print('Ini diluar looping')
#==================================================
print('\n')

# COntinue
for b in range (0,20,2):
    if b is 14:
        continue    # continue berfungsi untuk melewatkan suatu looping dengan suatu kondisi dan melanjutkan ke looping berikutnya
    print(b)        # note : perhatikan perbedaan penulisan syntax continue dan break
else:
    print('Ini adalah else')

print('Ini diluar looping')
#==================================================
print('\n')

#Pass
for c in range (0,5):
    if c is 3:
        pass        # pass sebenarnya tidak berefek apapun, namun dalam kondisi tertentu dibutuhkan untuk mengecek dummy
    print(c)
else:
    print('Ini adalah else')

print('Ini diluar looping')

#=============== SELESAI ==========================