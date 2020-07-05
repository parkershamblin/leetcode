class Solution:
    def average(self, salary: List[int]) -> float:
        # question I would ask. Are all salaries unique? or are there duplicates?
        # if there are duplicates we could create a set of salaries and remove
        # the min and max.
        
        # NOTE. I use a O(4n) strategy here rather than sorted than array because
        # sorting it automatically makes it more complex because sorting is O(log n * n)
        # and even though poping the max would be O(1) I would still have to slice the list
        # to remove the min which is O(k)
        maxS = max(salary)
        minS = min(salary)
        salary.remove(maxS)
        salary.remove(minS)
        
        return (sum(salary) / len(salary))