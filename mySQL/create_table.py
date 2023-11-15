import mysql.connector

nama_db = {
    'host': 'root',
    'password': '',
    'host': 'localhost',
    'database' : 'aset'
}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()
kursor.execute("""
    CREATE TABLE IF NOT EXISTS `aset`
    kode char(5) NOT NULL,
    nama varchar(50) NOT NULL,
    jumlah int(10) NOT NULL,
    harga int(10) NOT NULL,
    nilai int(10) NOT NULL,
    """)
