from typing import List
from operator import itemgetter


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # return self.dp(intervals)
        return self.greedy(intervals)

    def dp(self, intervals) -> int:
        """
        动态规划。

        排序会简化问题。
        dp[i] = 1 + max[dp[j]] | j in range(i)
        """
        if not intervals:
            return 0
        intervals.sort()
        dp = [1]
        for i in range(1, len(intervals)):
            dp.append(1 + max((dp[j] for j in range(0, i) if intervals[j][1] <= intervals[i][0]), default=0))
        return len(intervals) - max(dp)

    def greedy(self, intervals) -> int:
        """
        贪婪算法。

        按结束时间排序。
        """
        def cmp(a, b):
            return a[1] < b[1]
        if not intervals:
            return 0
        intervals.sort(key=itemgetter(1))
        count = 1
        right = intervals[0][1]
        for interval in intervals:
            if interval[0] < right:
                continue
            count += 1
            right = interval[1]
        return len(intervals) - count


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    solu = Solution()
    print(solu.eraseOverlapIntervals(intervals))
