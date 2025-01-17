class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i - 1] == "1" or s[i - 1] == "2":
                    dp[i] = dp[i - 2] if i >= 2 else 1
                else:
                    return 0
            elif s[i - 1] == "1" or (s[i - 1] == "2" and int(s[i]) <= 6):
                dp[i] = dp[i - 1] + (dp[i - 2] if i >= 2 else 1)
            else:
                dp[i] = dp[i - 1]
        return dp[-1]

    def method2(self, s: str):
        n = len(s)
        dp = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            if s[i] == "0" and (i - 1 < 0 or int(s[i - 1]) > 2):
                return 0
            if s[i] == "0":
                dp[i] = dp[i + 1]
                dp[i - 1] = dp[i + 1]
                i -= 1
            elif s[i] == "1" or (s[i] == "2" and (i + 1) < n and int(s[i + 1]) <= 6):
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]
        return dp[0]


if __name__ == "__main__":
    solu = Solution()
    s = "12"
    print(solu.numDecodings(s))
