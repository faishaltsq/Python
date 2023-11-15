class MieSedap:
    __stock = 100


    def __init__(self,rasa,ukuran,harga,jumlah):
        self.__rasa = rasa
        self.__ukuran = ukuran
        self.__harga = harga
        MieSedap.__stock -= jumlah

    @classmethod
    def getStock(cls):
        return cls.__stock

    @property
    def rasa(self):
        pass

    @property
    def ukuran(self):
        pass

    @property
    def harga(self):
        pass

    @rasa.getter
    def rasa(self):
        return self.__rasa

    @rasa.setter
    def rasa(self,rasa):
        self.__rasa = rasa

    @ukuran.getter
    def ukuran(self):
        return self.__ukuran

    @ukuran.setter
    def ukuran(self,ukuran):
        self.__ukuran = ukuran

    @harga.getter
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self,harga):
        self.__harga = harga


rendang = MieSedap("Rendang", "Besar", 2500, 10)
print(f"Stock Mie : {rendang.getStock()}")
print(f"Harga Mie {rendang.rasa} {rendang.harga}")
rendang.harga = 3000
print(f"Harga Mie {rendang.rasa} {rendang.harga}")
rendangBesar = MieSedap("Rendang Besar", "Besar", 2500, 10)
print(f"Harga Mie {rendangBesar.rasa} {rendangBesar.harga}")