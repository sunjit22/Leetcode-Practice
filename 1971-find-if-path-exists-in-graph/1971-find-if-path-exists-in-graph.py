class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        vertices = []
        for i in range(n):
            vertices.append(i)
            
        g = Graph(vertices)
        
        for A,B in edges:
            g.adj[A].append(B)
            g.adj[B].append(A)
            
        return g.bfs(start, end)    
        
    
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.adj = []
        
        for i in range(len(vertices)):
            self.adj.append([])

    def add_edge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        
    def bfs(self,source, dest):
        visited = {}
        visited[source] = True
        queue = []
        queue.append(source)
        
        while queue:
            s = queue.pop(0)
            
            if s == dest:
                return True
            
            for neighbor in self.adj[s]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    
        return False
        
         
    