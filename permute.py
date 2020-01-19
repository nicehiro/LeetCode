from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.recursive(nums, [])
        return self.res

    def recursive(self, nums, tmp):
        if len(nums) == 0:
            self.res.append(tmp)
            return
        for i in range(len(nums)):
            u = nums.copy()
            a = u.pop(i)
            t = tmp.copy()
            t.append(a)
            self.recursive(u, t)


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.permute(nums))
