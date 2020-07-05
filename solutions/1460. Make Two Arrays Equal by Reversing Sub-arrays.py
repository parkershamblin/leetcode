# redo Try solving with an occurence comparison. Will have to glance at notes/solutions
# but on 2nd retry try doing on my own
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)