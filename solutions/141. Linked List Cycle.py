# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        """While fast and fast.next hasn't reached the end of the linked list.
        If fast or fast.next is None that means we have reached the end of the linked list
        and the fast and slow pointers never intersected, therefor, the list doesn't
        have a cycle.
        """
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
