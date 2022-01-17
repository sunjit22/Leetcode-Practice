# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        queue = []
        queue.append([root, 0])
        while queue:
            q_size = len(queue)
            index_1 = queue[0][1]
            
            for i in range(q_size):
                node, index_2 = queue.pop(0)
                    
                if node.left:
                    queue.append([node.left, 2 * index_2])
                if node.right:
                    queue.append([node.right, 2 * index_2 + 1])
            ans = max(ans, index_2 - index_1 + 1)
            
        return ans     
                    