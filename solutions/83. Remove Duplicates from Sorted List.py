# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            # Uses next_distinct to find the next distinct value.
            next_distinct = cur.next
            while next_distinct and next_distinct.val == cur.val:
                next_distinct = next_distinct.next
            cur.next = next_distinct
            cur = next_distinct
        return head
