"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        if root is None:
            return
        else:
            arr.append(root.val)
            self.read_tree(root, arr)
            return arr
            
    def read_tree(self, root,arr):
        if root:
            for i in range(len(root.children)):
                arr.append(root.children[i].val)
                self.read_tree(root.children[i],arr)
            
        
        