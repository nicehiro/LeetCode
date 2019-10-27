from typing import List


class Solution:
    """三数之和

    二数之和的时候考虑使用 HashTable 解决，因此在解决这个问题的时候会去想可不可以使用
    类似的方法，但结果是不可以。

    新的解法是：先排序，一次遍历，找满足条件的其他点

    1. l, r 只在 i 的后面找，否则会找到重复的点
    2. 如果遇到重复的点，需要跳过
    3. 找到一次的点集之后还要继续找
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        last_i = None
        for i in range(len(nums) - 2):
            if sorted_nums[i] > 0:
                break
            if last_i == sorted_nums[i]:
                continue
            last_i = sorted_nums[i]
            l, r = i + 1, len(nums) - 1
            last_l = last_r = -1
            while l < r:
                if last_l != -1 and l != last_l and sorted_nums[l] == sorted_nums[last_l]:
                    l += 1
                    continue
                last_l = l
                if last_r != -1 and r != last_r and sorted_nums[r] == sorted_nums[last_r]:
                    r -= 1
                    continue
                last_r = r
                temp = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if temp == 0:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                elif temp < 0:
                    l += 1
                else:
                    r -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
