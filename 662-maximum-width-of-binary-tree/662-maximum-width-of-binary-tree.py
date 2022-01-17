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
            _, level_head_index = queue[0]
            
            for i in range(q_size):
                node, col_index = queue.pop(0)
                    
                if node.left:
                    queue.append([node.left, 2 * col_index])
                if node.right:
                    queue.append([node.right, 2 * col_index + 1])
            ans = max(ans, col_index - level_head_index + 1)
            
        return ans     
                    