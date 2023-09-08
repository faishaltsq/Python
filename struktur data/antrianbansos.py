class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new_node = node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None        
        self.length -= 1
        return True


    

    def add_priority(self, data, priority):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        if priority == 1:
            new_node.next = self.head
            self.head = new_node
            return
        count = 1
        temp = self.head
        while temp.next and count < priority - 1:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node
        if new_node.next is None:
            self.tail = new_node

amal_bansos = LinkedList("")

while True:
    print("""
--------------------------------------------
        Program Amal Bantuan Sosial        
--------------------------------------------
1. Menambahkan data penerima bantuan       
2. Melihat data penerima bantuan
3. Menambah data prioritas
4. Menghapus data penerima bantuan
5. Keluar
--------------------------------------------
          """)
    pilihan = input("Masukkan pilihan: ")
    if pilihan == "1":
        data = input("Masukkan nama penerima bantuan: ")
        amal_bansos.append(data)
        print("Data berhasil ditambahkan")
    elif pilihan == "2":
        amal_bansos.print_list()
        print("Data berhasil ditampilkan")
    elif pilihan == "3":
        data = input("Masukkan nama data prioritas: ")
        priority = int(input("Masukkan prioritas: "))
        amal_bansos.add_priority(data, priority)
        print("Data menjadi antrian prioritas")
    elif pilihan == "4":
        antrian = int(input("Masukkan antrian yang ingin dihapus : "))
        result = amal_bansos.remove(antrian)
        if result:
            print("Data berhasil dihapus")
        else:
            print("Antrian tidak valid. Gagal menghapus data.")
    elif pilihan == "5":
        print("Terimakasih telah menggunakan program ini")
        exit()
    else:
        print("Pilihan tidak ada")

      