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
        
        queue = []
        visited = {}
        queue.append(node)
        visited[node] = Node(node.val, [])
        while(len(queue) != 0):
            s = queue.pop(-1)
            
            for neighbour in s.neighbors:
                if neighbour not in visited:
                    visited[neighbour] = Node(neighbour.val, [])
                    queue.append(neighbour)
                    
                visited[s].neighbors.append(visited[neighbour]) 
        return visited[node]         
                    
                