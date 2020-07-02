class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._items = []
        

    def push(self, x: int) -> None:
        self._items.append(x)
        

    def pop(self) -> None:
        self._items.pop()

    def top(self) -> int:
        return self._items[-1]

    def getMin(self) -> int:
        return min(self._items)