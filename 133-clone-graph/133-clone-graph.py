"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        visited = {}
        visited[node] = Node(node.val, [])
        
        queue = [node]
        
        while queue:
            s = queue.pop(0)
            
            for nbr in s.neighbors:
                if nbr not in visited:
                    visited[nbr] = Node(nbr.val, [])
                    queue.append(nbr)
                    
                visited[s].neighbors.append(visited[nbr])
                
        return visited[node]        
        