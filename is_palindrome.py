class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return 'false'
        s = str(x)
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        if i >= j:
            return 'true'
        return 'false'


if __name__ == '__main__':
    s = Solution()
    st = -121
    print(s.isPalindrome(st))
