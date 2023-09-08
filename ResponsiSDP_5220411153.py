import random
from prettytable import PrettyTable

class Ayam:
    def __init__(self, label, umur):
        self.label = label
        self.umur = umur
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, label, umur):
        new_node = Ayam(label, umur)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node #type: ignore
    
    def bubble_sort(self):
        if self.head is None:
            return
        
        sorted_list = False
        while not sorted_list:
            sorted_list = True
            current = self.head
            while current.next:
                if current.umur > current.next.umur:
                    current.label, current.next.label = current.next.label, current.label
                    current.umur, current.next.umur = current.next.umur, current.umur
                    sorted_list = False
                current = current.next
    
    def check_umur(self):
        if self.head is None:
            return None
        
        dewasa = LinkedList()
        current = self.head
        while current:
            if 300 <= current.umur <= 600:
                dewasa.append(current.label, current.umur)
            current = current.next
        
        return dewasa
    
    def get_data(self):
        data = []
        current = self.head
        while current:
            data.append([current.label, current.umur])
            current = current.next
        
        return data
    
def main():
    daftar_ayam = LinkedList()
    for i in range(20):
        label = "Ayam " + str(i+1)
        umur = random.randint(0, 600)
        daftar_ayam.append(label, umur)
    
    daftar_ayam.bubble_sort()
    
    ayam_dewasa = daftar_ayam.check_umur()
    
    if ayam_dewasa is None:
        print("Tidak ada ayam yang sudah dewasa")
    else:
        print("Ayam yang sudah dewasa:")
        data = ayam_dewasa.get_data()
        table = PrettyTable()
        table.field_names = ["Label", "Umur(minggu)"]
        for row in data:
            table.add_row(row)
        print(table)

if __name__ == "__main__":
    main()
