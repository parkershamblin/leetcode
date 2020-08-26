# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
​
        headA_ptr = headA
        headB_ptr = headB
        
        if headA_ptr is headB_ptr:
            return headA_ptr
        
        while headA_ptr.next or headB_ptr.next:
            if headA_ptr is headB_ptr:
                return headA_ptr
            headA_ptr = headA_ptr.next if headA_ptr.next else headB
            headB_ptr = headB_ptr.next if headB_ptr.next else headA
            if headA_ptr is headB_ptr:
                return headA_ptr
