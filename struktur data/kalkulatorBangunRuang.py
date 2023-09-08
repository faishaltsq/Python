'''membuat class kubus, balok, prisma segitiga'''
#5220411153 Muhammad Faishal Tsaqief 
import math

class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi
    def set_sisi(self, sisi):
        self.sisi = sisi
    def get_sisi(self):
        return self.sisi
    def Luas(self):
        return 6 * self.sisi * self.sisi
    def Volume(self):
        return self.sisi * self.sisi * self.sisi
    
    
class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    def set_panjang(self, panjang):
        self.panjang = panjang
    def set_lebar(self, lebar):
        self.lebar = lebar
    def set_tinggi(self, tinggi):
        self.tinggi = tinggi
    def get_panjang(self):
        return self.panjang
    def get_lebar(self):
        return self.lebar
    def get_tinggi(self):
        return self.tinggi
    def luas(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)
    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class PrismaSegitiga:
    def __init__(self, rusuk, tinggi):
        self.rusuk = rusuk
        self.tinggi = tinggi
    def set_rusuk(self, rusuk):
        self.rusuk = rusuk
    def set_tinggi(self, tinggi):
        self.tinggi = tinggi
    def get_rusuk(self):
        return self.rusuk
    def get_tinggi(self):
        return self.tinggi
    def luas(self):
        return 2 * self.rusuk * self.tinggi
    def volume(self):
        return self.rusuk * self.tinggi
        
'''membuat menu'''

def menu():
    print('''
========= Kalkulator Bangun Ruang =========
1. Kubus
2. Balok
3. Prisma Segitiga
===========================================
          ''')
    
while True:
    menu()
    pilihan = input('Masukkan pilihan anda : ')
    
    if pilihan == '1':
        sisi = int(input('Masukkan sisi kubus: '))
        kubus = Kubus(sisi)
        print('Luas permukaan kubus : ', kubus.Luas())
        print('Volume kubus : ', kubus.Volume())
    elif pilihan == '2':
        panjang = int(input('Masukkan panjang balok: '))
        lebar = int(input('Masukkan lebar balok: '))
        tinggi = int(input('Masukkan tinggi balok: '))
        balok = Balok(panjang, lebar, tinggi)
        print("Luas permukaan balok : ", balok.luas())
        print("Volume balok : ", balok.volume())
    elif pilihan == '3':
        rusuk = int(input('Masukkan rusuk prisma segitiga: '))
        tinggi = int(input('Masukkan tinggi prisma segitiga: '))
        prisma = PrismaSegitiga(rusuk, tinggi)
        print("Luas permukaan prisma segitiga : ", prisma.luas())
        print
        
    else:
        print("pilihan tidak ada")
        break       