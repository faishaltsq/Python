class mobil:
    def __init__(self, merk , warna, CC):
        self.__merk = merk
        self.warna = warna
        self.CC = CC
        
    def tampilkan_merk(self):
        print(f"Merk mobil ini adalah {self.__merk}")
        
    
        

jip = mobil("Jeep", "Merah", 2000)


print(mobil.__dict__)
print(mobil.tampilkan_merk(jip))
    