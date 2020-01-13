from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_opt = [0] * length
        right_opt = [0] * length
        for i in range(length - 1):
            left_opt[i + 1] = max(height[i], left_opt[i])
            right_opt[length - 2 - i] = \
                max(height[length - 1 - i], right_opt[length - 1 - i])
        ans = 0
        for i in range(length):
            ans += max(0, min(left_opt[i], right_opt[i]) - height[i])
        return ans


if __name__ == "__main__":
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(height))