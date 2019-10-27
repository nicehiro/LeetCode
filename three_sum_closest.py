from typing import List


class Solution:
    """寻找最接近 target 的三数之和

    暴力破解法

    排序 + 双指针

    优化方法其实就是用双指针更快的找符合条件的数
    方法类似之前的三数求和问题
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l = len(nums)
        close_res = nums[0] + nums[1] + nums[2]
        gap = abs(close_res - target)
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    temp = nums[i] + nums[j] + nums[k]
                    if abs(temp - target) < gap:
                        close_res = temp
                        gap = abs(temp - target)
        return close_res

    def threeSumClosest2(self, nums: List[int], target: int) -> int:
        length = len(nums)
        sorted_nums = sorted(nums)
        close_res = sorted_nums[0] + sorted_nums[1] + sorted_nums[2]
        gap = abs(close_res - target)
        last_i = None
        for i in range(length - 2):
            if last_i != None and sorted_nums[last_i] == sorted_nums[i]:
                continue
            l = i + 1
            r = length - 1
            last_l = last_r = None
            last_i = i
            while l < r:
                if last_l != None and last_l != l and sorted_nums[last_l] == sorted_nums[l]:
                    l += 1
                    continue
                if last_r != None and last_r != r and sorted_nums[last_r] == sorted_nums[r]:
                    r -= 1
                    continue
                temp = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if abs(temp - target) < gap:
                    gap = abs(temp - target)
                    close_res = temp
                if temp > target:
                    r -= 1
                elif temp < target:
                    l += 1
                else:
                    break
        return close_res


if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,1,1,55]
    print(s.threeSumClosest2(nums, 3))
