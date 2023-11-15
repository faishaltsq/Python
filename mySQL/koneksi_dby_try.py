

import mysql.connector
from mysql.connector import errorcode

try:
    koneksi = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                        database='my_database')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Ada yang salah dengan username atau password anda")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database tidak ada")
    else:
        print(err)

else:
    print("Koneksi berhasil")
    koneksi.close()


