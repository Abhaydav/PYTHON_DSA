class Graph:
    def __init__(self):
        self.adj_list={}
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex,':',self.adj_list[vertex])
    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        return False
obj=Graph()
obj.add_vertex('A')
obj.print_graph()