from collections import deque
 
 
class Graph:
    def __init__(self,edges,n):
        # A list of lists to represent an adjacency list
        self.adjList = [ [] for _ in range(n) ]
        
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def DFS(graph, v, visited):
    visited[v]=True
    print(v,end=' ')                # print the current node

    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not visited[u]:       # if `u` is not yet discovered
            DFS(graph, u, visited)

def BFS(graph, q, Visited):
 
    if not q:
        return
 
    # dequeue front node and print it
    v = q.popleft()
    print(v, end=' ')
 
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not Visited[u]:
            # mark it as discovered and enqueue it
            Visited[u] = True
            q.append(u)
 
    BFS(graph, q, Visited)


if __name__ == '__main__':

    n=int(input("Enter the no. of vertices: "))
    e=int(input("Enter the no. of edges:"))
    print("Enter the vertices of edges:")
    edges=list(tuple(map(int,input().split())) for r in range(e))
    # List of graph edges as per the above diagram
    '''edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # vertex 0, 13, and 14 are single nodes
    ]
 
    # total number of nodes in the graph (labelled from 0 to 14)
    n = 15'''
 
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    # to keep track of whether a vertex is discovered or not
    Visited = [False] * n
 
    # Perform BFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    loop=True
    while (loop!=False):
        print("\n1.DFS\n2.BFS\n3.End")
        ch=int(input("Enter your choice:"))
        if ch==1:
            for i in range(n):
                if not Visited[i]:
                # start BFS traversal from vertex i
                    DFS(graph, i, Visited)
    
        if ch==2:
            q = deque()
            Visited = [False] * n
            for i in range(n):
                if not Visited[i]:
            # mark the source vertex as discovered
                    Visited[i] = True
            # enqueue source vertex
                    q.append(i)
            # start BFS traversal from vertex i
                    BFS(graph, q, Visited)
        if ch==3:
            loop=False

 
'''
Example:
1.
0------1
|     /| \ 
|    / |  \ 
|   /  |   2
|  /   |  /
| /    | /
4------3
DFS:0 1 2 3 4 
BFS:0 1 4 2 3 

2.
                  1
               / \  \ 
              /   \  \ 
             2     3  4
            / \      / \ 
           /   \    /   \ 
          5     6  7     8
         / \      / \ 
        /   \    /   \ 
       9     10 11    12
DFS:0 1 2 5 9 10 6 3 4 7 11 12 8 13 14 
BFS:0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 

Actual Output:
Examaple 
1.
Enter the no. of vertices: 5
Enter the no. of edges:7
Enter the vertices of edges:
0 1
1 2
1 3
3 4
0 4
1 4
0 1

1.DFS
2.BFS
3.End
Enter your choice:1
0 1 2 3 4 
1.DFS
2.BFS
3.End
Enter your choice:2
0 1 4 2 3 
1.DFS
2.BFS
3.End
Enter your choice:3
PS C:\Users\Admin\Desktop\DFS_BFS> 

2.

Enter the no. of vertices: 15
Enter the no. of edges:11
Enter the vertices of edges:
1 2
1 3
1 4
2 5
2 6
5 9
5 10
4 7
4 8
7 11
7 12

1.DFS
2.BFS
3.End
Enter your choice:1
0 1 2 5 9 10 6 3 4 7 11 12 8 13 14 
1.DFS
2.BFS
3.End
Enter your choice:2
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 
1.DFS
2.BFS
3.End
Enter your choice:3
PS C:\Users\Admin\Desktop\DFS_BFS>'''
    
            
            
            
 
