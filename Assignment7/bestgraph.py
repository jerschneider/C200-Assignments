class Graph:

    def __init__(self, nodes):
        self.nodes = nodes #this is the list
        self.edges = {} #this is the dictionary for the lists of edges
        for node in nodes:
            self.edges[node] = [] #creates a list inside of the dictionary, a key where the value is an empty list
    
    def add_edge(self, pair):
        (start, end) = pair # breaking apart a tuple of 2 item
        if start not in self.nodes or end not in self.nodes:
            return -1 # a false
        if end not in self.edges[start]: #edges is the dictionary for each path
            self.edges[start].append(end) #adds a new or an additional end value to an existing key >>> start:[existingpaths]+newpath
            return 1
        else:
            return -1    
    
    def del_edge(self, pair): #a method dedicated to just deleting
        (one, two) = pair #maybe change this to (start, end) for consistency
        if one in self.nodes and two in self.nodes and two in self.edges[one]:
            self.edges[one].remove(two)
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
            self.edges[node] = [] #then creats a dict entry
            return 1
    def del_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            del self.edges[node] #deletes the key
            for key in self.edges.keys():
                if node in self.edges[key]:
                    self.edges[key].remove(node)
            return 1
        else:
            return -1

    
    def adjMatrix(self):
        #prdocues a list of lists that is an N x N matrix
        #pass
        result = []
        for start in self.edges.keys():
            row = []
            for end in self.edges.keys():
                if end in self.edges[start]:
                    row += [1]
                else:
                    row += [0]
            result.append(row)
        #print(result)
        return result
    
    #Mr german had this included in his example and Iam not sure what it does
    def __repr__(self):
        return str(self.nodes) + " " + str(self.edges)


    def __str__(self):
        return str(self.edges)
        