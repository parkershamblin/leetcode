# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        cur = dummy
​
        while cur:
            next_distinct = cur.next
            while next_distinct and next_distinct.val == val:
                next_distinct = next_distinct.next
            cur.next = next_distinct
            cur = next_distinct
​
        return dummy.next
