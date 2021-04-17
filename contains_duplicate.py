from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        w = t + 1
        m = {}
        for i in range(len(nums)):
            id = self.get_id(nums[i], w)
            if id in m:
                return True
            m[id] = nums[i]
            if (id - 1) in m and abs(m[id - 1] - nums[i]) <= t:
                return True
            if (id + 1) in m and abs(m[id + 1] - nums[i]) <= t:
                return True
            if (i - k) >= 0:
                m.pop(self.get_id(nums[i - k], w))
        return False

    def get_id(self, x, w):
        if x >= 0:
            return x // w
        return (x + 1) // w - 1


if __name__ == "__main__":
    s = Solution()
    nums = [8, 7, 15, 1, 6, 1, 9, 15]
    print(s.containsNearbyAlmostDuplicate(nums, 1, 3))
