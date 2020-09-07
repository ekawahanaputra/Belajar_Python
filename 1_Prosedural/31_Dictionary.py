# DICTIONARY
# Cara Penulisan Tipe Data Dictionary
'''
data = {key:value,key:value,....} 
'''

data = {'NRP':24611,
        'Nama':'Eka Wahana Putra',
        'Training':'3 DT'}

print(data)

# Jika ingin mengakses nilai dari key
print(data['NRP'])
print(data['Nama'])

# Jika kita hanya ingin mengambil keys nya saja
print(data.keys())

# Jika kita hanya ingin mengambil value nya saja
print(data.values())
print('\n')
#============================================================
print('===== MEMBERLIST ======')

member1 = {'ID':100,
           'Nama':'Eka',
           'Job':'Swasta'}

member2 = {'ID':202,
           'Nama':'Sri',
           'Job':'Perawat'}

# dengan data dictionary, kita bisa mengakses sebuah database dalam bentuk memberlist
memberlist = {100:member1, 202:member2}

print(memberlist[100])
print(memberlist[202])
#====================== SELESAI ===========================