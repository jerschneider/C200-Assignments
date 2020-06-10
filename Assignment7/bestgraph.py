class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []
    
    def add_edge(self, pair):
        start, end = pair # breaking apart a tuple of 2 items
        self.edges[start].append(end)
    def del_edge(self, pair):

    def children(self):
        return self.edges[node]
    
    def nodes(self):
        # We just happen to have an instance variable
        #   the same name as a function 
        return str(self.nodes)
    def add_node(self):

    def del_node(self):

    def adjMatrix():
        #prdocues a list of lists that is an N x N matrix
    def __str__(self):
        return str(self.edges)