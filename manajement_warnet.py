#manajemen sistem warnet

#import library
import mysql.connector

#koneksi database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="")
#membuat cursor
cursor = db.cursor()

#membuat database
cursor.execute("CREATE DATABASE IF NOT EXISTS db_warnet")
cursor.execute("USE db_warnet")

#membuat tabel
cursor.execute("CREATE TABLE IF NOT EXISTS tb_customer (username VARCHAR(30) PRIMARY KEY,"
               " nama_pelanggan VARCHAR(40),"
               " no_hp VARCHAR(13),"
               " billing VARCHAR(3))")

#fungsi untuk menampilkan menu
def menu():
    print("""
=========== APLIKASI CRUD WARNET ===========
                     MENU
============================================
    1. Tambah Pelanggan Baru
    2. Lihat Data Pelanggan
    3. Ubah  Data Pelanggan
    4. Hapus Akun Pelanggan
    5. Keluar
============================================
    """)
    pilih = input("Pilih Menu> ")
    if pilih == "1":
        tambah()
    elif pilih == "2":
        lihat()
    elif pilih == "3":
        ubah()
    elif pilih == "4":
        hapus()
    elif pilih == "5":
        print("Terimakasih telah menggunakan aplikasi ini")
        exit()
    else:
        print("Menu Tidak Ada")
        back()
        
#fungsi untuk kembali ke menu

def back():
    back = input("Kembali ke menu (y/t)? ")
    if back == "y":
        menu()
    elif back == "t":
        print("Terimakasih telah menggunakan aplikasi ini")
        exit()
    else:
        print("Pilih y/t")

        back()

#fungsi untuk tambah pelanggan
def tambah():
    print("""
=========== APLIKASI CRUD WARNET ===========
                TAMBAH DATA
============================================
    """)
    username = input("Username: ")
    nama_pelanggan = input("Nama Pelanggan: ")
    no_hp = input("No HP: ")
    billing = input("Billing(menit): ")
    sql = "INSERT INTO tb_customer (username, nama_pelanggan, no_hp, billing) VALUES (%s, %s, %s, %s)"
    val = (username, nama_pelanggan, no_hp, billing)
    cursor.execute(sql, val)
    db.commit()
    print("{} data pelanggan ditambahkan".format(cursor.rowcount))
    print("""
============================================
    """)
    back()

#fungsi untuk lihat pelanggan

def lihat():
    print("""
=========== APLIKASI CRUD WARNET ===========
                  LIHAT DATA
============================================
    """)
    cursor.execute("SELECT * FROM tb_customer")
    result = cursor.fetchall()
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in result:
            print(data)
    print("""
============================================
        """)
    back()


def hapus():
    print("""
=========== APLIKASI CRUD WARNET ===========
                  HAPUS DATA
============================================
        """)

    username = input("Username: ")
    cursor.execute("DELETE FROM tb_customer WHERE username = %s", (username,))
    db.commit()
    print("{} data pelanggan dihapus".format(cursor.rowcount))
    print("""
============================================
        """)
    back()


def ubah():
    print("""
=========== APLIKASI CRUD WARNET ===========
                   UBAH DATA
============================================
    """)
    username = input("Username: ")
    nama_pelanggan = input("Nama Pelanggan: ")
    no_hp = input("No HP: ")
    billing = input("Billing: ")
    cursor.execute("UPDATE tb_customer SET nama_pelanggan = %s, no_hp = %s, billing = %s WHERE username = %s", (nama_pelanggan, no_hp, billing, username))
    db.commit()
    print("{} data pelanggan diubah".format(cursor.rowcount))
    print("""
============================================
    """)
    back()





if __name__ == "__main__":
    menu()

