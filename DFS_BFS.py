from collections import deque

class Graph:
    def _init_(self,edge,n):
        self.adjList=[[] for _ in range(n)]
        for(src,dest) in edge:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
            
    def DFS(self,v,visited):
        visited[v]=True
        print(v,end=' ')
        for u in graph.adjList[v]:
            if not visited[u]:
                graph.DFS(u,visited)
    def BFS(self,q,visited):
        if not q:
            return
        v=q.popleft()
        print(v,end=' ')
        for u in graph.adjList[v]:
            if not visited[u]:
                visited[u]=True
                q.append(u)
        graph.BFS(q,visited)
        
if __name__=='__main__':
    n=int(input("Enter No. of vertices: "))
    e=int(input("Enter No. of edges: "))
    print("Enter Vertices for edges: ")
    edge=list(tuple(map(int,input().split())) for r in range(e))
    graph=Graph(edge,n)
    
    loop=True
    while (loop!=False):
        print("\n1.DFS\n2.BFS\n3.End\n")
        c=int(input("Enter your choice: "))
        if c==1:
            visited=[False]*n
            for i in range(n):
                if not visited[i]:
                    graph.DFS(i,visited)
        elif c==2:
            q=deque()
            visited=[False]*n
            for i in range(n):
                if not visited[i]:
                    visited[i]=True
                    q.append(i)
                    graph.BFS(q,visited)
        elif c==3:
            loop=False
            print("End")