# #list sebagai iterable
gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']

for g in gorengan:
    print(g)
    
#string sebagai iterable
bakwan = 'bakwan'
for i in bakwan:
    print(i)
    
#for di dalam for
buah = ['semangka','jeruk','apel','anggur']
sayur = ['kangkung','wortel','tomat','kentang']

daftar_belanja = [gorengan,buah,sayur]
for daftar_belanja in daftar_belanja:
    print(daftar_belanja)
    for komponen in daftar_belanja:
        print(komponen)
        
#for loop
num = 2

for i in range(10):
    if i is num:
        print(i)    
        print('angka',num,'ditemukan')
        break
    else:
        continue
    
#while loop
angka = 0
status = True

while status:
    print("didalam while loop")
    for i in range(angka):
        if angka == 0:
            angka +=1
            print("angka saat ini adalah",angka)
    
    if angka == 50:
        status = False
        print("angka ditemukan",angka)
        break
    angka +=1