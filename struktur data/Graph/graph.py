class Graph :
    def __init__(self):
        self.adj_list = {}
    def print_graph(self):
        if(self.adj_list == {}): return False
        for vertex in self.adj_list:
            print(vertex , ":" , self.adj_list[vertex])
        print(''); return True
            
    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True 
        return False
    
    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys() :
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True 
        return False
    
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys() :
            try :
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    def avoidDuplicateAppend(self, listTarget, value):
        if(value not in listTarget):
            listTarget.append(value)
            return True
        return False
    def isInGraph(self, vertex):
        if(vertex in self.adj_list.keys()): 
            return True
        else:
            return False
    
    def printALLConnected(self, vertex):
        if(self.adj_list == {}): return False
        print(f"Data in {vertex} vertex -->, end=''")
        for data in self.adj_list[vertex]:
            print(data, end=',' if data != self.adj_list[vertex][-1] else '')
        print(''); return True
    
    
# my_graph = Graph()
# my_graph.add_vertex("A")
# my_graph.add_vertex("B")
# my_graph.add_vertex("C")
# my_graph.add_vertex("D")

# my_graph.add_edge("A","B")
# my_graph.add_edge("A","C")
# my_graph.add_edge("A","D")
# my_graph.add_edge("B","D")
# my_graph.add_edge("C","D")
# my_graph.print_graph()

if __name__ == '__main__':
    print('\n ================= FINAL RESULT =================')
    my_graph = Graph()
    listVertex = [21,76,44,12,32,54,87]
    listVertex = [str(data) for data in listVertex]
    for vertex in listVertex: my_graph.add_vertex(vertex)
    
    # 21 vertex
    my_graph.add_edge(listVertex[0], listVertex[1])
    my_graph.add_edge(listVertex[0], listVertex[2])
    my_graph.add_edge(listVertex[0], listVertex[3])

    # 76 vertex
    my_graph.add_edge(listVertex[1], listVertex[3])
    my_graph.add_edge(listVertex[1], listVertex[0])
    my_graph.add_edge(listVertex[1], listVertex[2])

    # 44 vertex
    my_graph.add_edge(listVertex[2], listVertex[1])
    my_graph.add_edge(listVertex[2], listVertex[0])
    my_graph.add_edge(listVertex[2], listVertex[3])

    # 18 vertex
    my_graph.add_edge(listVertex[3], listVertex[0])
    my_graph.add_edge(listVertex[3], listVertex[2])
    my_graph.add_edge(listVertex[3], listVertex[4])

    # 52 vertex
    my_graph.add_edge(listVertex[4], listVertex[3])
    my_graph.add_edge(listVertex[4], listVertex[5])

    #27 vertex
    my_graph.add_edge(listVertex[5], listVertex[4])
    my_graph.add_edge(listVertex[5], listVertex[6])

    #82 vertex
    my_graph.add_edge(listVertex[6], listVertex[5])

    my_graph.print_graph()
    #show all connected vertex
    my_graph.printALLConnected(listVertex[0])

    #check is it contains or not
    print(f'{listVertex[1]} is Contains' if my_graph.isInGraph(listVertex[1]) else f'{listVertex[1]} is not Contains')
    print('===============================================')