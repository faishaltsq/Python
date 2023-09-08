"""
OOP
"""

class RuasBangun:
    def __init__(self,panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        
    """
    SETTTER DAN GETTER
    SETTER : method atau function yang kita gunakan untuk mengubah nilai variabel pada class
    GETTER : method atau function untuk mengambil nilai
    """
    def set_panjang(self,panjang):
        self.panjang = panjang
        
    def set_lebar(self,lebar):
        self.lebar = lebar
        
    def get_panjang(self):
        return self.panjang
    def get_lebar(self):
        return self.lebar
    
class Persegi_panjang(RuasBangun): #Mewakili karakteristik class induknya
    def __init__(self, panjang, lebar):
        RuasBangun.__init__(self,panjang,lebar)
    
    def luas(self):
        # return RuasBangun.get_panjang(self) * RuasBangun.get_lebar(self)
        return self.panjang * self.lebar

class Persegi(RuasBangun): #Tidak mewakili karakteristik class induknya
    def __init__(self, sisi):
        self.sisi = sisi
    
    def set_sisi(self, sisi):
        self.sisi = sisi
    def get_sisi(self, sisi):
        return self.sisi
    
    def luas(self):
        return self.sisi * self.sisi
        
    
        
        
pp = Persegi_panjang(5, 10)
print(pp.luas())

p = Persegi(5)
print(p.luas())
# print(rb.panjang)
# rb.set_panjang(6)
# print(rb.panjang)