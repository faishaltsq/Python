class barang:
    def __init__(self, sku, nama_barang, harga_satuan, jumlah_stok):
        self.sku = sku
        self.nama_barang = nama_barang
        self.harga_satuan = harga_satuan
        self.jumlah_stok = jumlah_stok
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, sku, nama_barang, harga_satuan, jumlah_stok):
        if not self.root:
            self.root = barang(sku, nama_barang, harga_satuan, jumlah_stok)
        else:
            self._insert(self.root, sku, nama_barang, harga_satuan, jumlah_stok)
        sku_tersimpan.append(sku)  # Add the SKU to the sku_tersimpan list

    def _insert(self, current_data, sku, nama_barang, harga_satuan, jumlah_stok):
        if sku < current_data.sku:
            if current_data.left:
                self._insert(current_data.left, sku, nama_barang, harga_satuan, jumlah_stok)
            else:
                current_data.left = barang(sku, nama_barang, harga_satuan, jumlah_stok)
        elif sku > current_data.sku:
            if current_data.right:
                self._insert(current_data.right, sku, nama_barang, harga_satuan, jumlah_stok)
            else:
                current_data.right = barang(sku, nama_barang, harga_satuan, jumlah_stok)
    def find(self, sku):
        if self.root:
            return self._find(self.root, sku)
        else:
            return None

    def _find(self, current_data, sku):
        if sku == current_data.sku:
            return current_data
        elif sku < current_data.sku and current_data.left:
            return self._find(current_data.left, sku)
        elif sku > current_data.sku and current_data.right:
            return self._find(current_data.right, sku)
        else:
            return None

def lihat_data_transaksi(transaksi):
    if len(transaksi) == 0:
        print("Belum ada data transaksi konsumen.")
    else:
        print("Data Transaksi Konsumen:")
        for transaction in transaksi:
            print("Nama Konsumen:", transaction["Nama Konsumen"])
            print("No. SKU:", transaction["No. SKU"])
            print("Jumlah Beli:", transaction["Jumlah Beli"])
            print("Subtotal:", transaction["Subtotal"])
            print()

def bubble_sort(transaksi):
    n = len(transaksi)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if transaksi[j]["Subtotal"] < transaksi[j + 1]["Subtotal"]:
                transaksi[j], transaksi[j + 1] = transaksi[j + 1], transaksi[j]

# Main Menu
bst = BST()
transaksi = []
sku_tersimpan = [] 

while True:
    print("""
====================================
Sistem informasi stok dan transaksi 
====================================
          Menu Utama:
    1. Kelola stok barang
    2. Kelola Transaksi Konsumen
    3. Keluar
====================================
    """)

    menu_utama = input("Pilih menu (1/2/3): ")

    if menu_utama == "1":
        print("""
====================================            
    Sub Menu Kelola Stok Barang:
====================================
    1. Input Data Stok Barang
    2. Restock Barang
    3. Lihat Stok Barang
    4. Kembali ke Menu Utama
====================================
""")    
        menu_utama = input("Pilih menu (1/2/3/4): ")
        
        if menu_utama == "1":
            # Input Data Stok Barang
            print("Input Data Stok Barang")
            while True:
                sku = input("No. SKU (4 digit angka): ")
                if len(sku) != 4 or not sku.isdigit():
                    print("No. SKU harus terdiri dari 4 digit angka.")
                    continue

                existing_item = bst.find(sku)
                if existing_item:
                    print("No. SKU sudah terdaftar.")
                    continue

                nama_barang = input("Nama Barang: ")
                harga_satuan = float(input("Harga Satuan: "))
                jumlah_stok = int(input("Jumlah Stok: "))

                bst.insert(sku, nama_barang, harga_satuan, jumlah_stok)
                # sku_tersimpan.append(sku)
                print("Data Stok Barang berhasil disimpan ke dalam program.")
                lanjut_input = input("Apakah ingin input data stok barang lagi? (Y/N): ")
                if lanjut_input.upper() == "N":
                    break

        elif menu_utama == "2":
            # Restock Barang
            print("Restock Barang")
            while True:
                # Menampilkan sku yang sudah tersimpan
                print("No. SKU yang sudah tersimpan di dalam program:")
                for sku in sku_tersimpan:
                    print(sku)
                sku = input("No. SKU (4 digit angka): ")
                if len(sku) != 4 or not sku.isdigit():
                    print("No. SKU harus terdiri dari 4 digit angka.")
                    continue

                existing_item = bst.find(sku)
                if existing_item:
                    jumlah_baru = int(input("Jumlah Stok Baru: "))
                    total_stok = existing_item.jumlah_stok + jumlah_baru
                    existing_item.jumlah_stok = total_stok
                    print("Stok barang dengan No. SKU", sku, "telah diperbarui.")
                else:
                    print("No. SKU belum tersimpan di dalam BST. Mohon input data stok barang terlebih dahulu.")
                
                lanjut_input = input("Apakah ingin restock barang lagi? (Y/N): ")
                if lanjut_input.upper() == "N":
                    break
                        
        elif menu_utama == "3":
            print("Lihat Stok Barang")
            while True:
                sku = input("No. SKU (4 digit angka): ")
                if len(sku) != 4 or not sku.isdigit():
                    print("No. SKU harus terdiri dari 4 digit angka.")
                    continue

                existing_item = bst.find(sku)
                if existing_item:
                    print("No. SKU:", existing_item.sku)
                    print("Nama Barang:", existing_item.nama_barang)
                    print("Harga Satuan:", existing_item.harga_satuan)
                    print("Jumlah Stok:", existing_item.jumlah_stok)
                else:
                    print("No. SKU belum tersimpan di dalam BST. Mohon input data stok barang terlebih dahulu.")
                
                lanjut_input = input("Apakah ingin melihat stok barang lagi? (Y/N): ")
                if lanjut_input.upper() == "N":
                    break
        elif menu_utama == "4":
            continue

    elif menu_utama == "2":
        # Sub Menu Kelola Transaksi Konsumen
        while True:
            print("""
====================================
Sub Menu Kelola Transaksi Konsumen:
====================================
1. Input Data Transaksi Baru
2. Lihat Data Seluruh Transaksi Konsumen
3. Lihat Data Transaksi Berdasarkan Subtotal
4. Kembali ke Menu Utama
====================================
""")

            menu_transaksi = input("Pilih menu (1/2/3/4): ")

            if menu_transaksi == "1":
                # Input Data Transaksi Baru
                nama_konsumen = input("Nama Konsumen: ")

                while True:
                    sku = input("No. SKU barang yang dibeli (4 digit angka): ")
                    if len(sku) != 4 or not sku.isdigit():
                        print("No. SKU harus terdiri dari 4 digit angka.")
                        continue

                    existing_item = bst.find(sku)
                    if existing_item:
                        jumlah_beli = int(input("Jumlah Beli: "))

                        if jumlah_beli <= existing_item.jumlah_stok:
                            subtotal = jumlah_beli * existing_item.harga_satuan

                            transaksi.append({
                                "Nama Konsumen": nama_konsumen,
                                "No. SKU": sku,
                                "Jumlah Beli": jumlah_beli,
                                "Subtotal": subtotal
                            })

                            existing_item.jumlah_stok -= jumlah_beli
                            print("Data transaksi berhasil disimpan.")
                        else:
                            print("Jumlah stok barang tidak mencukupi.")
                    else:
                        print("No. SKU belum tersimpan di dalam BST. Mohon input data stok barang terlebih dahulu.")
                    
                    lanjut_input = input("Apakah ingin input data transaksi lagi? (Y/N): ")
                    if lanjut_input.upper() == "N":
                        break

            elif menu_transaksi == "2":
                # Lihat Data Seluruh Transaksi Konsumen
                lihat_data_transaksi(transaksi)

            elif menu_transaksi == "3":
                # Lihat Data Transaksi Berdasarkan Subtotal
                if len(transaksi) == 0:
                    print("Belum ada data transaksi konsumen.")
                else:
                    bubble_sort(transaksi)
                    lihat_data_transaksi(transaksi)

            elif menu_transaksi == "4":
                break

    elif menu_utama == "3":
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan menu tidak valid. Silakan pilih menu yang sesuai.")
