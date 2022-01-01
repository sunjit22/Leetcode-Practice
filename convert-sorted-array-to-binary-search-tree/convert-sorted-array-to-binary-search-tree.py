# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def sortHelper(left, right):  
            if left > right:
                return None
            middle = (left+right) //2
            node = TreeNode(nums[middle])
            node.left = sortHelper(left, middle-1)
            node.right = sortHelper(middle+1, right)

            return node
         
        
        return sortHelper(0,len(nums)-1)
        
    