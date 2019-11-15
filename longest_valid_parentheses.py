class Solution:
    def longestValidParentheses(self, s: str) -> int:
        i = 0
        longest = 0
        while i < len(s):
            if s[i] == ')':
                i += 1
                continue
            left, right = 1, 0
            j = i + 1
            while j < len(s):
                if s[j] == '(':
                    left += 1
                else:
                    right += 1
                if left < right:
                    longest = max(longest, 2 * min(left, right))
                    break
                j += 1
            if j == len(s):
                longest = max(longest, 2 * min(left, right))
            i += 1
        return longest


if __name__ == '__main__':
    s = Solution()
    st = '(()'
    print(s.longestValidParentheses(st))