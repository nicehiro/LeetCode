from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        times = {}
        for i, n in enumerate(nums):
            if n not in times:
                times[n] = [i, i, 0]
            times[n][1] = i
            times[n][2] += 1
        res_max = 0
        res = 0
        for n, t in times.items():
            temp = t[1] - t[0] + 1
            if t[2] > res_max:
                res_max = t[2]
                res = temp
            elif t[2] == res_max:
                if temp < res:
                    res = temp
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 2, 3, 1, 4, 2]
    print(s.findShortestSubArray(nums))
