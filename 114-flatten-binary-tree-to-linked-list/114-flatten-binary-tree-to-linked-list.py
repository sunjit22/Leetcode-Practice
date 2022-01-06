# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#   Approach 1   
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        stack = []
        stack.append(root)

        prev = None

        while stack:
            s = stack.pop()
            if s:
                stack.append(s.right)
                stack.append(s.left)

                if prev:
                    prev.right = s
                    prev.left = None
                    s.left = None

                prev = s
            
#     Approach 2 - Recursion O(n)          
#     def dfs(self, root):
#         if not root:
#             return None

#         if not root.left and not root.right:
#             return root
        
#         leftTail = self.dfs(root.left)
#         rightTail = self.dfs(root.right)

#         if leftTail:
#             leftTail.right = root.right
#             root.right = root.left
#             root.left = None

#         return rightTail if rightTail else leftTail
        
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """        
#         self.dfs(root)       
                
                    
            
            
    
