class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return len(points)
        arrows = 0        
        points.sort(key=lambda x: (x[1]))
        i = 0
        while i < len(points) - 1:
            j = i + 1
            while j < len(points) and points[i][1] >= points[j][0]:
                j += 1
            i = j
            arrows += 1
        if ((len(points) > 2 and points[-1][0] > points[-2][1]) or j<len(points)):
            arrows += 1
        return arrows
