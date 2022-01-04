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
        
        visited= {}
        visited[node] = Node(node.val, [])
        
        queue = []
        queue.append(node)
        
        while queue:
            s = queue.pop(0)
            for neighbor in s.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)    
                visited[s].neighbors.append(visited[neighbor])
                
        return visited[node]      
                
                
                    
        