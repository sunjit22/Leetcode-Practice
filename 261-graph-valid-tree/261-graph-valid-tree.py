class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def dfs(visited, node, adj):
            if node in visited:
                return 
            
            visited.add(node)
            
            for a in adj[node]:
                dfs(visited, a,adj)
            
        
        if len(edges) != n-1:
            return False
        
        adj = []    
        for i in range(n):
            adj.append([])
            
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            
            
            
        visited = set()
        
        dfs(visited,0, adj)
        
        return len(visited) == n
        
        