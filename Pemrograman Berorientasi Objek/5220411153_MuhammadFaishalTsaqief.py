# responsi Pemrograman Berorientasi Obejek 10/11/2023

class Atm:
    def __init__(self, lokasi,saldo ):
        self.lokasi = lokasi
        self.saldo = saldo

#mengetahui lokasi atm
    @property
    def lokasi_atm(self):
        return self.lokasi

    @lokasi_atm.setter
    def lokasi_atm(self, lokasi):
        self.lokasi = lokasi
        print(f"lokasi atm berada di {self.lokasi}")
#mengecek jumlah uang yang ada di atm


    def cek_jumlah_atm(self):
       print( f"Saldo pada ATM ini adalah {self.saldo}")


#menambahkan uang kedalam atm
    @property
    def jumlah_atm(self):
        return self.saldo

    @jumlah_atm.setter
    def jumlah_atm(self, saldo):
        self.saldo = saldo

        print(f"Atm ini telah menambahkan {self.saldo} ke dalam atm")





class User(Atm):
    def __init__(self, nama, saldo,lokasi):
        super().__init__(lokasi, saldo)
        self.nama = nama
        self.saldo = saldo
#mengecek saldo user
    def cek_saldo(self):
        print(f"Halo {self.nama}, saldo anda adalah {self.saldo}")

#setor uang kedalam atm
    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Halo {self.nama}, saldo anda adalah {self.saldo}")

#tarik uang dari atm
    def tarik(self, jumlah):
        self.saldo -= jumlah
        print(f"Halo {self.nama},anda telah menarik uang sebesar {self.saldo}")


atm1 = Atm("Jl. Sudirman", 1000000)

budi = User("Budi", 1000000, "Jl. Sudirman")


print(f"Lokasi atm ini berada di {atm1.lokasi_atm}")


atm1.cek_jumlah_atm()
atm1.jumlah_atm = 50000000

budi.cek_saldo()

budi.setor(5000)

budi.tarik(10000)













