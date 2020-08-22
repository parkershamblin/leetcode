class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode(val={self.val}, next={self.next})"
​
​
class MyLinkedList:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(val=0, next=None) # watch out val=0, not val=None
        self.size = 0
        
​
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur = self.head
        if 0 <= index < self.size:
            for _ in range(index):
                cur = cur.next
            return cur.val
        else:
            return - 1
​
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion,
        the new node will be the first node of the linked list.
        """
        self.addAtIndex(index=0, val=val)
​
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(index=self.size, val=val)
​
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the
        length of linked list, the node will be appended to the end of linked list. If index is
        greater than the length, the node will not be inserted.
        """
        if index < 0 and index > self.size:
            return None # do nothing
​
        elif index == 0:
            new_node = ListNode(val=val)
            new_node.next = self.head
            self.head = new_node
​
        elif index == self.size:
            cur = self.head
            for _ in range(self.size - 1):
                cur = cur.next
            new_node = ListNode(val=val, next=None)
            cur.next = new_node
    
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            new_node = ListNode(val, cur.next)
            cur.next = new_node
