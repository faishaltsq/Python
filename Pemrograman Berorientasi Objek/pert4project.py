class Mahasiswa :
    login = False
    matkul = None
    def __init__(self,id,nama,alamat,email,telepon):
        self.npm = id
        self.nama = nama
        self.alamat = alamat
        self.email = email
        self.telepon = telepon

    def tampilkanIdentitas(self):
        if self.login != True :
            print("Anda harus login terlebih dahulu, baru bisa tampilkan identitas")
        else :
            print("NPM : ",self.npm)
            print("Nama : ",self.nama)
            print("Alamat : ",self.alamat)
            print("Email : ",self.email)
            print("Telepon : ",self.telepon)

    def login(self):
        self.login = True
        print("Anda berhasil login")

    def logout(self):
        if self.login != True :
            print("Ngapain logout klo gapernah login ")
        self.login = False
        print("Anda berhasil logout")

    def statusLogin(self):
        if self.login :
            print("Anda sedang login")
        else :
            print("Anda sedang logout")

    def krs(self,matkul):
        if self.login != True :
            print("Anda harus login terlebih dahulu, baru bisa krs")

        else:
            if self.matkul != None :
                print("Anda sudah mengambil mata kuliah")
            else :
                self.matkul = matkul
                print("Anda Berhasil KRS")

    def tampilkanMatkul(self):
        if self.login != True :
            print("Anda harus login terlebih dahulu, baru bisa tampilkan matkul")
        else :
            if self.matkul == None :
                print("Anda belum mengambil mata kuliah")
            else :
                print("Anda mengambil mata kuliah : ")
                for i in self.matkul :
                    print(i)

    def absensi(self):
        if self.login != True :
            print("Anda harus login terlebih dahulu, baru bisa absen")
        else :
            print("Anda berhasil absen")

faishal = Mahasiswa(180441100050,"Faishal","Jl. Kebon Jeruk","faishalganteng123@xzy.com","08123456789")
faishal.login()
faishal.tampilkanMatkul()