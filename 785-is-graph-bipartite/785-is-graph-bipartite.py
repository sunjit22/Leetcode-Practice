class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        for i in range(len(graph)):
            if i not in color:
                queue = [i]
                color[i] = 0
                while queue:
                    s = queue.pop(0)
                    for neighbor in graph[s]:
                        if neighbor not in color:
                            queue.append(neighbor)
                            color[neighbor] = color[s]^1
                        elif color[neighbor] == color[s]:
                            return False
        return True                
    
        