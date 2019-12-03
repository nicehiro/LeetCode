from typing import List


class Solution:

    def __init__(self):
        super().__init__()
        self.res = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """递归算法
        """
        self.dp_iter(candidates, target, [])
        return self.res

    def dp_iter(self, candidates, target, temp):
        if target == 0:
            temp.sort()
            if temp not in self.res:
                self.res.append(temp)
        if target < 0 or len(candidates) <= 0:
            return
        self.dp_iter(candidates[1:], target, temp)
        x = temp.copy()
        x.append(candidates[0])
        self.dp_iter(candidates[1:], target - candidates[0], x)

    def combinationSum3(self, candidates, target):
        """迭代算法
        """
        candidates.sort()
        if target < candidates[0]:
            return []
        dp = [[[] for _ in range(len(candidates))] for _ in range(0, target + 1)]
        dp[candidates[0]][0].append([candidates[0]])
        for i in range(1, target + 1):
            for j in range(1, len(candidates)):
                temp = i - candidates[j]
                if temp == 0:
                    dp[i][j].append([candidates[j]])
                elif temp > 0:
                    for res in dp[temp][j - 1]:
                        x = res.copy()
                        x.append(candidates[j])
                        dp[i][j].append(x)
                for res in dp[i][j - 1]:
                    if res not in dp[i][j]:
                        dp[i][j].append(res)
        return dp[target][len(candidates) - 1]


if __name__ == '__main__':
    s = Solution()
    candidates = [2]
    target = 1
    # print(s.combinationSum2(candidates, target))
    print(s.combinationSum3(candidates, target))