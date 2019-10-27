from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        total_length = length1 + length2
        sorts = []
        i = j = k = 0
        while k <= total_length / 2:
            k += 1
            if i < length1 and j < length2:
                if nums1[i] <= nums2[j]:
                    sorts.append(nums1[i])
                    i += 1
                else:
                    sorts.append(nums2[j])
                    j += 1
            else:
                if i >= length1:
                    sorts.append(nums2[j])
                    j += 1
                else:
                    sorts.append(nums1[i])
                    i += 1
        if total_length % 2 != 0:
            return sorts[-1]
        return (sorts[-1] + sorts[-2]) / 2


if __name__ == '__main__':
    s = Solution()
    nums1 = []
    nums2 = [4, 5, 6]
    print(s.findMedianSortedArrays(nums1, nums2))
