


class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class doubly_linkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        self.tail = self.tail.prev
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
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1,index, -1):    
                temp = temp.prev
        return temp
    
    

my_doublyLinkedList = doubly_linkedList(10)
my_doublyLinkedList.append(5)
my_doublyLinkedList.append(16)
my_doublyLinkedList.pop_first()
my_doublyLinkedList.print_list()