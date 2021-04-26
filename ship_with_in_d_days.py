from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        self.D = D
        self.weights = weights

        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            if self.check(mid):
                r = mid
            else:
                l = mid + 1

        return r

    def check(self, t):
        d = 1
        s = 0
        for i in range(len(self.weights)):
            if s + self.weights[i] <= t:
                s += self.weights[i]
            else:
                s = 0
                d += 1
        return d <= self.D
