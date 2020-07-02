class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        seconds = 0
        for i in range(len(points)-1):
            curr_points = points[i]
            next_points = points[i+1]
            
            while curr_points != next_points:
                # if current point is farther to the right than the next point
                if curr_points[0] > next_points[0]:
                    # go left one
                    curr_points[0] -= 1
                # elif current point is father to the left than the next point
                elif curr_points[0] < next_points[0]:
                    # go right one
                    curr_points[0] += 1
                # if current point is higher than the next point
                if curr_points[1] > next_points[1]:
                    # move down one
                    curr_points[1] -= 1
                elif curr_points[1] < next_points[1]:
                    # move up one
                    curr_points[1] += 1
                seconds += 1
        return seconds