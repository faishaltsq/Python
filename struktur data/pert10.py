class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinerySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None: 
            self.root = new_node 
            return True
        
        # logic jika root sudah didefinisikan
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def delete(self, value):
        temp = self.root
        if temp == None:
            return False
        if value < temp.value:
            if temp.left:
                temp.left = temp.left.delete(value)
            return True
        if value > temp.value:
            if temp.right:
                temp.right = temp.right.delete(value)
            return self
        if temp.right == None:
            return temp.left
        if temp.left == None:
            return temp.right
        min_larger_node = temp.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        temp.value = min_larger_node.value
        temp.right = self.right.delete(min_larger_node.value)
        return self
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value: temp = temp.left
            elif value > temp.value: temp = temp.right
            else: return True
        return False
    
    def min_value_node(self, current_node):
        while current_node.left: current_node = current_node.left
        return current_node
    
    def max_value_node(self, current_node):
        while current_node.right: current_node = current_node.right
        return current_node

if __name__ == "__main__":
    my_tree = BinerySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)   
    print('Maximum Value in Tree:')
    print(my_tree.max_value_node(my_tree.root).value) 
    # print(my_tree.contains(21))
    print('Binary search tree coontains 21')
    print(my_tree.contains(21))