# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        if head.val == val:
            while head and head.val == val:
                head = head.next
​
        cur = head
        while cur:
            if cur.next and cur.next.val == val:
                while cur.next and cur.next.val == val:
                    if cur.next.next:
                        cur.next = cur.next.next
                    else:
                        cur.next = None
            cur = cur.next
        return head
