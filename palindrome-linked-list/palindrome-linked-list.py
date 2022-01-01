# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
          
        # Check if arr is equal to it's reverse
        return arr == arr[::-1]    
            