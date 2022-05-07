# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = [root]
        while queue:
            result.append([])
            for i in range(len(queue)):
                s = queue.pop(0)
                result[-1].append(s.val)
                
                if s.left is not None:
                    queue.append(s.left)
                    
                if s.right is not None:
                    queue.append(s.right) 
        return result 