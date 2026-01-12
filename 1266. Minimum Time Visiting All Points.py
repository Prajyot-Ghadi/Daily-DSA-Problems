class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_step = 0
   

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            total_step += max(dx, dy)

        return total_step
