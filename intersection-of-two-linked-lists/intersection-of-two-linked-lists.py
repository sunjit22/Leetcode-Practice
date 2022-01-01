# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        count_1 = count_2 = 0
        
        curr_1 = headA
        curr_2 = headB
        while curr_1 or curr_2:
            if curr_1:
                count_1 += 1
                curr_1 = curr_1.next
                
            if curr_2:
                count_2 += 1
                curr_2 = curr_2.next  
               
        if count_1 > count_2:
            for i in range(count_1 - count_2):
                headA = headA.next
                
        elif count_2 > count_1:
            for i in range(count_2 - count_1):
                headB = headB.next
        
        # Find common point
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None        
            