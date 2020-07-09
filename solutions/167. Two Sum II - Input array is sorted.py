class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # holy shit this soltion is bad
        right = bisect.bisect(numbers, target)
        for i, n in enumerate(numbers[:right+1]):
            dif = target - n
            if dif in numbers[:right+1]:
                uno = numbers.pop(i)
                dos = numbers.index(dif)
                return [i+1, dos+2]