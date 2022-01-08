# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = [root]
        arr = []
        
        while queue:
            queue2 = queue
            queue = []
            while queue2:
                s = queue2.pop(0)
                
                if s.left:
                    queue.append(s.left)
                    
                if s.right:
                    queue.append(s.right)
            
                                
            arr.append(s.val)    
        return arr        
                
                
                
        