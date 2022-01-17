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
            curMin = queue[0][1]
            leftMost = 0
            rightMost = 0
            
            for i in range(q_size):
                cur_id = queue[0][1] - curMin
                s = queue.pop(0)[0]
                
                if i == 0 :
                    leftMost = cur_id
                if i == q_size-1:
                    rightMost = cur_id
                    
                if s.left:
                    queue.append([s.left, cur_id*2+1])
                if s.right:
                    queue.append([s.right,cur_id*2+2])
            ans = max(ans, rightMost -leftMost + 1)
            
        return ans     
                    