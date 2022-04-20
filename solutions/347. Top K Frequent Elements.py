class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} # num: frequency
        for n in nums:
            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 1
        sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
        return [i[0] for i in sorted_d[:k]]
​
