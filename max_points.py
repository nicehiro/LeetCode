from typing import List
import fractions


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        int_max = float('inf')
        points = [[fractions.Fraction(x) for x in p] for p in points]

        def linear(a, b, x, y):
            if a != int_max:
                return y == a * x + b
            return x == b

        def point_equal(p1, p2):
            return p1[0] == p2[0] and p1[1] == p2[1]

        n = len(points)
        max_ = 2
        for i in range(n-1):
            repeat = 0
            for j in range(i+1, n):
                if point_equal(points[i], points[j]):
                    repeat += 1
                    max_ = max(max_, 1 + repeat)
                    continue
                m = 2 + repeat
                repeat = 0
                if points[i][0] == points[j][0]:
                    a = int_max
                    b = points[i][0]
                else:
                    a = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    b = points[i][1] - a * points[i][0]
                for k in range(j+1, n):
                    if linear(a, b, points[k][0], points[k][1]):
                        m += 1
                max_ = max(max_, m)
        return max_


if __name__ == '__main__':
    solu = Solution()
    points = [[3,1],[12,3],[3,1],[-6,-1]]
    print(solu.maxPoints(points))
