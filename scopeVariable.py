

#membuat variable global

nama = "Rizal"
alamat = "Jl. Raya Bogor"

def testing():
    #membuat variable local
    nama = "Rizal"
    alamat = "Jl. Raya Bogor"
    print("nama: %s "% nama)
    print(alamat)

#mengakses variable global
print("variable global")
print("nama: %s "% nama)
print(alamat)

testing()