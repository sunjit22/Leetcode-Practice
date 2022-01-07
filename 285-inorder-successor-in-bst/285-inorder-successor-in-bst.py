# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        # First check if right exists
        if p.right:
            curr = p.right
            while curr.left:
                curr = curr.left
            return curr
        else:
            successor, curr = None, root
            while curr != p:
                if curr.val < p.val:
                    curr = curr.right
                else:
                    successor, curr = curr, curr.left
            return successor