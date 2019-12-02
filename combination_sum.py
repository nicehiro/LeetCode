from typing import List


class Solution:
    """动态规划 DP
    """
    def __init__(self):
        super().__init__()
        self.all = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.dp_iter(candidates, target, [])
        return self.all

    def dp_iter(self, candidates, target, res):
        """递归算法
        """
        if target == 0:
            self.all.append(res)
            return
        if target < 0 or len(candidates) == 0:
            return
        temp = res.copy()
        temp.append(candidates[0])
        self.dp_iter(candidates, target - candidates[0], temp)
        self.dp_iter(candidates[1:], target, res)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """迭代算法
        """
        dp = [[] for _ in range(target + 1)]
        for i in range(target + 1):
            for j in candidates:
                if j == i:
                    dp[i].append([j])
                elif j < i:
                    for k in dp[i - j]:
                        x = k.copy()
                        x.append(j)
                        x.sort()
                        if x not in dp[i]:
                            dp[i].append(x)
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    candidates = [2, 3, 5]
    target = 8
    # print(s.combinationSum(candidates, target))
    print(s.combinationSum2(candidates, target))