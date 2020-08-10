# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        
        if not head or not head.next:
            return False
        
        fast = fast.next.next
        
​
        
        while slow: # <- is this correct?
            if slow and fast:
                if slow.val == fast.val:
                    return True
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
