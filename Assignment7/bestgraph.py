class Graph:

    def __init__(self, nodes):
        self.nodes = nodes #this is the list
        self.paths = {} #this is the dictionary for the lists of edges
        for node in nodes:
            self.paths[node] = [] #creates a list inside of the dictionary, a key where the value is an empty list
    
    def add_edge(self, pair):
        (node1, node2) = pair # breaking apart a tuple of 2 item
        if node1 not in self.nodes or node2 not in self.nodes:
            return -1 # a false
        if node2 not in self.paths[node1]: #edges is the dictionary for each path
            self.paths[node1].append(node2) #adds a new or an additional end value to an existing key >>> start:[existingpaths]+newpath
            return 1
        else:
            return -1    
    
    def del_edge(self, pair): #a method dedicated to just deleting
        (node1, node2) = pair #maybe change this to (start, end) for consistency
        if node1 in self.nodes and node2 in self.nodes and node2 in self.paths[node1]:
            self.paths[node1].remove(node2)
            return 1
        else:
            return -1
        #del self.edges[start].append(end)

    #def children(self):
        #return self.edges[node]
    
    #def nodes(self):
        # We just happen to have an instance variable
        #   the same name as a function 
        #return str(self.nodes)
    
    def add_node(self, node):
        if node in self.nodes:
            return -1 #returns -1(false) if the node already exists
        else:
            self.nodes += [node]
            self.paths[node] = [] #then creats a dict entry
            return 1
    def del_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            del self.paths[node] #deletes the key
            for key in self.paths.keys():
                if node in self.paths[key]:
                    self.paths[key].remove(node)
            return 1
        else:
            return -1

    def adjMatrix(self):
        #prdocues a list of lists that is an N x N matrix
        #pass
        result = []
        for node1 in self.paths.keys():
            row = []
            for node2 in self.paths.keys():
                if node2 in self.paths[node1]:
                    row += [1]
                else:
                    row += [0]
            result.append(row)
        #print(result)
        return result
        