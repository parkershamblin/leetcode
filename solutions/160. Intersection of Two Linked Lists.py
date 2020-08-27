# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        aptr, bptr = headA, headB
        
        while aptr is not bptr:
            aptr = aptr.next if aptr else headB
            bptr = bptr.next if bptr else headA
        return aptr
