from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.back_find(nums1, m, nums2, n)

    def front_find(self, nums1, m, nums2, n):
        i = j = 0
        while i < m and j < n:
            if nums2[j] < nums1[i]:
                k = m - 1
                while k >= i:
                    nums1[k+1] = nums1[k]
                    k -= 1
                nums1[i] = nums2[j]
                j += 1
                i += 1
                m += 1
            else:
                i += 1
        if j < n:
            t = j
            while j < n:
                nums1[m+j-t] = nums2[j]
                j += 1

    def back_find(self, nums1, m, nums2, n):
        i, j, k = m-1, n-1, m+n-1
        while i >= 0 and j >= 0 and k >= 0:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        if j >= 0:
            while j >= 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1



if __name__ == '__main__':
    solu = Solution()
    nums1 = [4,5,6,0,0,0]
    nums2 = [1,2,3]
    solu.merge(nums1, 3, nums2, 3)
    print(nums1)
