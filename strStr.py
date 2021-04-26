class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        nexts = [0] * n

        j = 0
        for i in range(1, n):
            while j > 0 and needle[i] != needle[j]:
                j = nexts[j - 1]
            if needle[i] == needle[j]:
                j += 1
            nexts[i] = j

        j = 0
        for i in range(0, m):
            while j > 0 and haystack[i] != needle[j]:
                j = nexts[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return i - m + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    haystack = "hello"
    needle = "ll"
    print(s.strStr(haystack, needle))
