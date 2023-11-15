mhs = [
    {
        "nama": "Arsya",
        "npm ": "5220411114" ,
        "status" : True
    },
    {
        "nama": "Hery",
        "npm ": "5220411138" ,
        "status" : False
    },
    {
        "nama": "Faishal",
        "npm ": "5220411153" ,
        "status" : True
    },
    {
        "nama": "Gojo sutoro bin es kiko ",
        "npm ": "5220411153" ,
        "status" : False
    },
    {
        "nama": "Toji fushigoro bin apple",
        "npm ": "5220411193" ,
        "status" : False
    },
    {
        "nama": "Uzumaki Saburo",
        "npm ": "5220411993" ,
        "status" : False
    }
]

print("Status Pembayaran Modul Berdasarkan Database SIA")
for data in mhs:
    print("=============================================")
    print("Nama     :",data["nama"])
    print("NPM      :",data["npm "])
    if data["status"] == True:
        print("Status   : Sudah Membayar")
    else:
        print("Status   : Belum Membayar")