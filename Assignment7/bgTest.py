from bestgraph import Graph

def main():
    print("Testing code below")
    print("="*30)

    givenNodes = [1, 2, 3, 4]

    givenEdges = [(1, 2), (1, 3), (3, 4)]

    g = Graph(givenNodes)

    print("Testing adding original edges")
    print("=" * 10)
    for e in givenEdges:
        result = g.add_edge(e)
        if result == -1:
            print("Adding edges " + str(e) + " should have returned 1. Returned -1")

    print("=" * 10 + "\n")

    print("Testing Add Node")

    addNodes = [1, 5, 6, 7]
    results = [-1, 1, 1, 1]

    print("=" * 10)
    for i in range(len(addNodes)):
        toAdd = addNodes[i]
        correct = results[i]
        result = g.add_node(toAdd)
        if result != correct:
            print("Adding nodes " + str(toAdd) + " should have returned " + str(-1 * result) + ". Returned " + str(result))
    print("=" * 10 + "\n")


    print("Testing Add Edge")

    addEdges = [(1, 2), (2, 5), (3, 2), (2, 7), (7, 2)]
    addResults = [-1, 1, 1, 1, 1]

    print("=" * 10)
    for i in range(len(addEdges)):
        toAdd = addEdges[i]
        correct = addResults[i]
        result = g.add_edge(toAdd)
        if result != correct:
            print("Adding edges " + str(toAdd) + " should have returned " + str(-1 * result) + ". Returned " + str(result))
    print("=" * 10 + "\n")

    # You are allowed to make new graphs to help with testing

    print("Testing Adjacency Matrix")
    # FIXME: This does not test if you adjacency Matrix is created correctly. 
    #   If you want to ensure it works, you need to write your own tests (required)

    # NOTE: If you are unsure if something is correct, suggest a graph on 
    #       Piazza (publicly) and you can see if you are able to solve it
    #       or if give a chance for some to get take a stab at it (without
    #       using the program)


    print("\n"*3)
    print("=" * 10 + "New Graph" + "=" * 10)
    newNodes = [1, 2, 3, 4, 5, 6]

    newEdges = [(1, 2), (1, 3), (3, 4), (1, 5), (6, 4), (4, 1), (6, 2), (1, 2)]
    newGraph = Graph(newNodes)
    for e in newEdges:
        newGraph.add_edge(e)
    
    print("Testing Delete Nodes")

    toDelete = [7, 4]
    toDeleteResults = [-1, 1]
    toDeleteEdgeResult =[
        {1: [2, 3, 5], 2: [], 3: [4], 4: [1], 5: [], 6: [4, 2]},
        {1: [2, 3, 5], 2: [], 3: [], 5: [], 6: [2]},
    ]

    print("=" * 10)
    for i in range(len(toDelete)):
        d = toDelete[i]
        result = newGraph.del_node(d)
        if result != toDeleteResults[i]:
            print("Deleting node  " + str(d) + " should have returned " + str(-1 * result) + ". Returned " + str(result))
        
        if newGraph.edges != toDeleteEdgeResult[i]:
            print("Removing Node ({}) Expected results: {} \t Given Results: {}".format(d, toDeleteEdgeResult[i], newGraph.edges))
    print("=" * 10 + "\n")

    print()
    print("Testing Delete Edges")
    # FIXME: This does not test if you delete nodes and edges correctly. 
    #   If you want to ensure it works, you need to write your own tests (required)


if __name__ == "__main__":
        main()
        