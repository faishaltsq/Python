class Node :
    def __init__ (self,value):
        self.value = value 
        self.next = None
        

class Stack :
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
my_stack = Stack(4)
my_stack.push(20)
my_stack.push(21)
my_stack.push(22)