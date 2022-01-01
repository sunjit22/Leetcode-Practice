"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Check is node exists
        if node is None:
            return None
        
        # Data structures used : 
        # 1. Queue
        # 2. Hashmap (Key: newNode, Value: newNode)
        queue = []
        visited = {}
        
        queue.append(node)
        visited[node] = Node(node.val, [])
        
        while queue:
            s = queue.pop(0)
            for neighbor in s.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                    
                # Append neighbors to new node    
                visited[s].neighbors.append(visited[neighbor])
                
        return visited[node]               