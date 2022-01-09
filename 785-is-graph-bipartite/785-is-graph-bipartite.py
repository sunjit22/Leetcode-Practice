class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Create a hashmap to keep track of visited node's colors
        color = {}
        
        # Loop through all nodes
        for i in range(len(graph)):
            # Check if has already been visited or not
            # BFS
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
    
        