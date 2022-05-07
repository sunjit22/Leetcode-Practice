# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = [[root, 0]]
        width = 1
        while queue:
            width = max(width, queue[-1][1] - queue[0][1] + 1)
            for i in range(len(queue)):
                
                s = queue.pop(0)
                
                node = s[0]
                idx = s[1]
                
                if node.left is not None:
                    queue.append([node.left, (idx*2) + 1])
                    
                if node.right is not None:
                    queue.append([node.right, (idx*2) + 2]) 
        return width             
                    
                    
        