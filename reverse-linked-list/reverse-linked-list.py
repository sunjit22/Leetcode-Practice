# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        first = head
        arr = []
        while first is not None:
            arr.append(first.val)
            first = first.next
        
        result = head
        arr.reverse()
        for i in range(len(arr)):
            head.val = arr[i]
            head = head.next
            
        return result    
        