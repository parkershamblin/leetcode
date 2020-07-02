class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._items = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._items.insert(0, x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self._items.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._items[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._items