from typing import List
import collections


class Solution:
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        r = l = res = 0
        min_q = collections.deque()
        max_q = collections.deque()
        for num in nums:
            while len(min_q) and num < min_q[-1]:
                min_q.pop()
            while len(max_q) and num > max_q[-1]:
                max_q.pop()
            min_q.append(num)
            max_q.append(num)
            r += 1
            while max_q[0] - min_q[0] > limit:
                if min_q[0] == nums[l]:
                    min_q.popleft()
                if max_q[0] == nums[l]:
                    max_q.popleft()
                l += 1
            res = max(res, r - l)
        return res

    def overtime(self, nums, limit):
        """超时版本。"""
        if not nums or limit < 0:
            return 0
        l = 0
        r = 1
        res = []
        while r < len(nums) + 1:
            if r == len(nums):
                res.append(r - l)
                break
            p = True
            for j in range(l, r):
                if abs(nums[j] - nums[r]) > limit:
                    res.append(r - l)
                    l = j + 1
                    p = False
                    break
            r += 1 if p else 0
        return max(res)


if __name__ == "__main__":
    s = Solution()
    nums = [8, 2, 4, 7]
    limit = 5
    print(s.longestSubarray(nums, limit))
