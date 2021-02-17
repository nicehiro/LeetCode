from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums or not nums[0]:
            return nums
        ori_r = len(nums)
        ori_c = len(nums[0])
        if ori_r * ori_c != r * c:
            return nums
        res = []
        for i in range(r):
            res.append([])
            for j in range(c):
                l = i * c + j
                ori_i = l // ori_c
                ori_j = l % ori_c
                res[i].append(nums[ori_i][ori_j])
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(s.matrixReshape(nums, 1, 4))
