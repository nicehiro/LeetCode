from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.recursive(nums, [])
        return self.res

    def recursive(self, nums, tmp):
        if len(nums) == 0:
            self.res.append(tmp)
            return
        used = []
        for i in range(len(nums)):
            u = nums.copy()
            a = u.pop(i)
            if used.__contains__(a):
                continue
            used.append(a)
            t = tmp.copy()
            t.append(a)
            self.recursive(u, t)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 3]
    print(s.permuteUnique(nums))
