class SpanningTree:
    def __init__(self):
        self.numberOfVertices = 0
        self.parent = {}
        self.size = {}
        self.edges = []

    def find(self,root):
        parent = self.parent
        a = root
        while parent[a] != a:
            a = parent[a]

        # path comprehension
        while root != a:
            nextnode = parent[root]
            parent[root] = a
            root = nextnode
        return a

    def union(self,a, b):
        parent = self.parent
        size = self.size
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
            return True
        else:
            return False

    def createGraph(self):
        self.parent.clear()
        self.size.clear()
        self.edges = []
        self.numberOfVertices = int(input("Enter number of vertices=> "))
        numberOfEdges = int(input("Enter number of edges=> "))
        for edge in range(numberOfEdges):
            node1,node2,weight = map(int,input("Enter node1 - node2 - weight of edge").split())
            self.parent[node1] = node1
            self.parent[node2] = node2
            self.size[node1] = 1
            self.size[node2] = 1
            self.edges.append((weight,node1,node2))

    def Kruskals_algo(self):
        self.edges.sort()
        spanningTreeEdges = []
        totalEdges = 0
        for wieght,node1,node2 in self.edges:
            if self.union(node1,node2):
                totalEdges+=1
                spanningTreeEdges.append((wieght,node1,node2))
            if totalEdges == self.numberOfVertices-1:
                break
        for weight,node1,node2 in spanningTreeEdges:
            print(node1,node2,weight)


if __name__ == '__main__':
    s = SpanningTree()
    while True:
        print("""
        Enter
        1. To create new graph.
        2. To get spanning tree of graph
        3. To terminate the program.""")
        option = int(input())
        if option == 1:
            s.createGraph()
        elif option == 2:
            s.Kruskals_algo()
        else:
            break


""" 
Output:
PS E:\c++ practise\cpp> python -u "e:\LP2_LAB\assign3.py"

        Enter
        1. To create new graph.
        2. To get spanning tree of graph
        3. To terminate the program.    
1
Enter number of vertices=> 4 
Enter number of edges=> 6
Enter node1 - node2 - weight of edge1 2 2
Enter node1 - node2 - weight of edge2 3 2
Enter node1 - node2 - weight of edge3 4 1
Enter node1 - node2 - weight of edge1 3 4
Enter node1 - node2 - weight of edge1 4 4
Enter node1 - node2 - weight of edge2 4 3

        Enter
        1. To create new graph.
        2. To get spanning tree of graph
        3. To terminate the program.
2
3 4 1
1 2 2
2 3 2

        Enter
        1. To create new graph.
        2. To get spanning tree of graph
        3. To terminate the program.
1
Enter number of vertices=> 5
Enter number of edges=> 6
Enter node1 - node2 - weight of edge1 4 3
Enter node1 - node2 - weight of edge1 5 12
Enter node1 - node2 - weight of edge4 2 5
Enter node1 - node2 - weight of edge4 3 3
Enter node1 - node2 - weight of edge2 3 2
Enter node1 - node2 - weight of edge5 3 7

        Enter
        1. To create new graph.
        2. To get spanning tree of graph
        3. To terminate the program.
2
2 3 2
1 4 3
4 3 3
5 3 7

        Enter
        1. To create new graph.
        2. To get spanning tree of graph
        3. To terminate the program.
3
"""
