class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-stone for stone in stones]
        heapq.heapify(h)
        while h[0] != 0 and len(h) > 1:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]
