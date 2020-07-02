class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        possible_destinations = [i[-1] for i in paths]
        for destination in possible_destinations:
            if destination not in [i[0] for i in paths]:
                return destination