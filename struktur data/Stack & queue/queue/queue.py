class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
my_queue = Queue()

my_queue.enqueue('item1')
my_queue.enqueue('item2')
my_queue.enqueue('item3')

print(my_queue.size()) # akan menampilkan 3

print(my_queue.dequeue()) # akan menampilkan 'item1'

print(my_queue.size()) # akan menampilkan 2
