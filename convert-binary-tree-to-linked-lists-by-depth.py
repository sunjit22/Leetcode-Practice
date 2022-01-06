# LINTCODE : 242 · Convert Binary Tree to Linked Lists by Depth

# Description
# Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if root is None:
            return []
        result = []
        queue = [root] 
        dummy = ListNode(0) 
        lastNode = None
        while queue:
            lastNode = dummy 
            for i in range(len(queue)):
                node = queue.pop(0)
                lastNode.next = ListNode(node.val)
                lastNode = lastNode.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)     
            result.append(dummy.next)
        return result
