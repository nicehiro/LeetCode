from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        pass

    def method1(self, nums: List[int]):
        """Sort, then find max gap.
        """
        if not nums or len(nums) < 2:
            return 0
        # O(nlogn)
        nums.sort()
        maxGap = -1
        # O(n)
        for i in range(1, len(nums)):
            maxGap = max(maxGap, nums[i]-nums[i-1])
        return maxGap

    def method2(self, nums: List[int]):
        """Radix sort.
        """
        if not nums or len(nums) < 2:
            return 0
        i = 0
        # O(n)
        max_num = max(nums)
        j = len(str(max_num))
        # O(j)
        while i < j:
            bluck = [[] for _ in range(10)]
            # O(n)
            for n in nums:
                bluck[int(n / (10 ** i)) % 10].append(n)
            nums.clear()
            # O(n)
            for x in bluck:
                for y in x:
                    nums.append(y)
            i += 1
        max_gap = -1
        # O(n)
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i]-nums[i-1])
        return max_gap

    def method3(self, nums: List[int]):
        """Bucket sorting.
        """
        pass
