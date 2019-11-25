class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        length = len(s)
        dp = [0 for _ in range(length)]
        for i in range(1, length):
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                res = max(res, dp[i])
            elif s[i] == ')' and s[i-1] == ')' \
                and i - dp[i-1] > 0 \
                and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if (i - dp[i-1]) >= 2 else 0) + 2
                res = max(res, dp[i])
        return res


if __name__ == '__main__':
    s = Solution()
    st = '()(())'
    print(s.longestValidParentheses(st))