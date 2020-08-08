# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        intuitive brute force solution (two passes)
        """
    
        # first pass find length of list
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        # Edge case when entire linked list is to be deleted
        if length == n:
            return head.next
        
        # second pass update the to-be-deleted node's previous node's "next" field to .next.next
        cur = head
        for _ in range(length-n-1):
            cur = cur.next
        cur.next = cur.next.next
        return head
