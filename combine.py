from typing import List
import copy


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.iteration(n, k)

    def recursive(self, n: int, k: int) -> List[List[int]]:
        """Recursive version.
        """
        if k == 1:
            return [[x] for x in range(1, n+1)]
        if n == k:
            return [[x for x in range(1, n+1)]]
        if k >= n:
            return 0
        t = self.iteration(n-1, k-1)
        [x.append(n) for x in t]
        z = self.iteration(n-1, k)
        return t + z

    def iteration(self, n: int, k: int) -> List[List[int]]:
        opt = [[[] for _ in range(k+1)] for _ in range(n+1)]
        for i in range(min(n, k)+1):
            opt[i][i] = [[x for x in range(1, i+1)]]
        for i in range(n+1):
            opt[i][1] = [[x] for x in range(1, i+1)]
        for i in range(2, n+1):
            for j in range(2, min(i, k+1)):
                t = opt[i-1][j-1]
                temp = copy.deepcopy(t)
                [x.append(i) for x in temp]
                opt[i][j] = temp + opt[i-1][j]
        return opt[n][k]


if __name__ == '__main__':
    s = Solution()
    n = 5
    k = 3
    print(s.combine(n, k))
