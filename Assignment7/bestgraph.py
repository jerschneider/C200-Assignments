class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []
    
    def add_edge(self, pair):
        (start, end) = pair # breaking apart a tuple of 2 item
        if start not in self.nodes or end not in self.nodes:
            return -1
        if end not in self.edges[start]:
            self.edges[start].append(end)
            return 1
        else:
            return -1    
    def del_edge(self, pair):
        (one, two) = pair
        if one in self.nodes and two in self.nodes:
            self.edges[one].remove(two)

        else:
            return -1




        #del self.edges[start].append(end)

    def children(self):
        return self.edges[node]
    
    def nodes(self):
        # We just happen to have an instance variable
        #   the same name as a function 
        return str(self.nodes)
    def add_node(self, node):
        if node in self.nodes:
            return -1
        else:
            self.nodes += [node]
            self.edges[node] = []
            return 1
    def del_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            self.edges.pop(node)
            for key in self.edges.keys():
                if node in self.edges[key]:
                    self.edges[key].remove(node)
            return 1
        else:
            return -1

    
    def adjMatrix(self):
        #prdocues a list of lists that is an N x N matrix
    
    
    #def __str__(self):
        #return str(self.edges)
        