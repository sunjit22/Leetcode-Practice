# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(root,list_nodes):
            if root is not None:
                traverse(root.left,list_nodes)
                traverse(root.right,list_nodes)
                list_nodes.append(root.val)
            
        list_nodes = []
        traverse(root,list_nodes)
        return list_nodes

        
        
        
        