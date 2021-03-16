class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        return self.method2(preorder)

    def method1(self, preorder: str):
        nums = preorder.split(",")
        i = 0

        def dfs():
            nonlocal i
            if i >= len(nums):
                return False
            c = nums[i]
            i += 1
            if c == "#":
                return True
            left = dfs()
            right = dfs()
            if not left or not right:
                return False
            return True

        return dfs() and i >= len(nums)

    def method2(self, preorder: str):
        nums = preorder.split(",")
        stack = []
        for c in nums:
            stack.append(c)
            while (
                len(stack) >= 3 and stack[-1] == stack[-2] == "#" and stack[-3] != "#"
            ):
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        return len(stack) == 1 and stack.pop() == "#"

    def method3(self, preorder: str):
        """diff = out - in"""
        nums = preorder.split(",")
        diff = 1
        for c in nums:
            diff -= 1
            if diff < 0:
                return False
            if c != "#":
                diff += 2
        return diff == 0


if __name__ == "__main__":
    s = Solution()
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    s.isValidSerialization(preorder)
