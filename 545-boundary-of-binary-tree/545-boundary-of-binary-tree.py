# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # -- helpers --
        def findLeftBoundary(node):
            left = []
            while node and not isLeaf(node):
                left.append(node.val)
                if node.left:
                    node = node.left # - NOTE [1]
                else:
                    node = node.right # -- NOTE [2] -- 
            return left
            
            
        def findRightBoundary(node):
            right = []
            while node and not isLeaf(node):
                right.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left # -- see test case 2 : node 6
            return right
            
            
        def findLeaves(node, leaves=[]):
            if isLeaf(node):
                leaves.append(node.val)
            if node.left:
                findLeaves(node.left, leaves)
            if node.right:
                findLeaves(node.right, leaves)
            return leaves  
            
            
        def isLeaf(node):
            if not node.left and not node.right:
                return True
            return False
            
            
        # -- main --
        # edge cases
        if not root:
            return []
        if isLeaf(root):
            return [root.val]
        left = findLeftBoundary(root.left) # will be non-empty only if root has left child
        right = findRightBoundary(root.right) # will be non-empty only if root has right child
        leaves = findLeaves(root)
        res = [root.val]

        return res + left + leaves + right[::-1] 