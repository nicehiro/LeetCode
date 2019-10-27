from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        i, j = 0, length - 1
        max_area = -1
        while i < j:
            temp = (j - i) * min(height[i], height[j])
            if temp > max_area:
                max_area = temp
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))
