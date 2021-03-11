from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # return self.method1(envelopes)
        return self.method2(envelopes)

    def method1(self, envelopes: List[List[int]]):
        """动态规划"""
        if not envelopes:
            return 0
        # 先对 w 进行升序排列，再对 h 进行降序排列
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)

        f = [1] * n
        for i in range(n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    f[i] = max(f[i], 1 + f[j])
        return max(f)

    def method2(self, envelopes: List[List[int]]):
        if not envelopes:
            return 0
        # 先对 w 进行升序排列，再对 h 进行降序排列
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)

        stack = []
        res = 0
        for i in range(n):
            if stack and envelopes[i][1] <= stack[-1][1]:
                res = max(res, len(stack))

            while stack and envelopes[i][1] <= stack[-1][1]:
                stack.pop()

            stack.append(envelopes[i])
        return max(res, len(stack))


if __name__ == "__main__":
    s = Solution()
    # envelopes = [
    #     [2, 100],
    #     [3, 200],
    #     [4, 300],
    #     [5, 500],
    #     [5, 400],
    #     [5, 250],
    #     [6, 370],
    #     [6, 360],
    #     [7, 380],
    # ]
    envelopes = [[30, 50], [12, 2], [3, 4], [12, 15]]
    print(s.maxEnvelopes(envelopes))
