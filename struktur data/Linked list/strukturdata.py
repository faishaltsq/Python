# my_list = [1, 2, 3, 4, 5, 6, 9, 8, 9, 10]

# my_list.pop(0)
# my_list.insert(0,9)
# my_list.insert(1,"Hello World")
# print(my_list)

# for i in my_list:
#     if i == 7:
#         print("Angka 7 ada di dalam list")
#     else:
#         print("Angka 7 tidak ada di dalam list")


# #class
# class cookie:
#     def __init__(self, color):
#         self.color = color


# cookie_one = cookie("brown")
# cookie_two = cookie("green")

# print(cookie_one.color)


#linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    def append(self, value):
        if self.next is None:
            self.next = LinkedList(value)
        else:
            self.next.append(value)
    def pop(self):
        if self.next is None:
            return None
        elif self.next.next is None:
            self.next = None
        else:
            self.next.pop()
    def get(self, index):
        if index == 0:
            return self.value
        elif self.next is None:
            return None
        else:
            return self.next.get(index - 1)
    def set(self, index, value):
        if index == 0:
            self.value = value
        elif self.next is None:
            return None
        else:
            self.next.set(index - 1, value)
    def insert(self, index, value):
        if index == 0:
            new_node = LinkedList(value)
            new_node.next = self
            return new_node
        elif self.next is None:
            return None
        else:
            self.next = self.next.insert(index - 1, value)
            return self
    def delete(self, index):
        if index == 0:
            return self.next
        elif self.next is None:
            return None
        else:
            self.next = self.next.delete(index - 1)
            return self
    def __str__(self):
        if self.next is None:
            return str(self.value)
        else:
            return str(self.value) + " " + str(self.next)
    def __len__(self):
        if self.next is None:
            return 1
        else:
            return 1 + len(self.next)
        
