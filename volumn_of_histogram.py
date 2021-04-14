from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                p = stack.pop()
                if stack:
                    res += (min(height[i], height[stack[-1]]) - height[p]) * (
                        i - stack[-1] - 1
                    )
            stack.append(i)
        return res


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    print(s.trap(height))
