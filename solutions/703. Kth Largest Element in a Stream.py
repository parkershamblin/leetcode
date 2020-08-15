class KthLargest:
​
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.queue = nums
        heapq.heapify(self.queue)
        while len(self.queue) > k:
            heapq.heappop(self.queue)
​
    def add(self, val: int) -> int:
        if len(self.queue) < self.k:
            heapq.heappush(self.queue, val)
        elif val > self.queue[0]:
            heapq.heapreplace(self.queue, val)
        return self.queue[0]
