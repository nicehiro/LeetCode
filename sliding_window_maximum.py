from typing import List
from heapq import heappop, heappush, heapify
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k > len(nums):
            return 0
        # return bruteforce(nums, k)
        # return self.max_heap(nums, k)
        return self.deque(nums, k)

    def bruteforce(self, nums, k):
        if not nums or k > len(nums):
            return 0
        maxs = []
        last_max = 0
        for i in range(len(nums)-k+1):
            last = -1 if i == 0 else nums[i-1]
            if i == 0 or last == last_max:
                max_ = max(nums[i:i+k])
            else:
                max_ = max(last_max, nums[i+k-1])
            last_max = max_
            maxs.append(max_)
        return maxs

    def max_heap(self, nums, k):
        """
        最大堆实现。

        当堆顶元素不在滑动窗口内时，删除堆顶元素。
        Python 的优先队列默认是最小堆。
        """
        n = len(nums)
        p = [(-nums[i], i) for i in range(k)]
        heapify(p)
        maxs = []
        for i in range(n-k+1):
            while p[0][1] < i:
                heappop(p)
            maxs.append(-p[0][0])
            if i + k < n:
                heappush(p, (-nums[i+k], i+k))
        return maxs

    def deque(self, nums, k):
        """
        单调队列。

        双向队列，并且队列内是单调元素。
        """
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        maxs = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            maxs.append(nums[q[0]])
        return maxs



if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solu = Solution()
    print(solu.maxSlidingWindow(nums, k))
