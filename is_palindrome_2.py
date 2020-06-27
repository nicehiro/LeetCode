class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < len(s) and j > -1:
            while i < len(s) and not self.is_number_or_alpha(s[i]):
                i += 1
            while j > -1 and not self.is_number_or_alpha(s[j]):
                j -= 1
            if i >= len(s) or j < 0:
                break
            x = ord(s[i])
            y = ord(s[j])
            if self.is_upper_alpha(x):
                x += 32
            if self.is_upper_alpha(y):
                y += 32
            if x != y:
                return False
            i += 1
            j -= 1
        return True

    def is_number_or_alpha(self, x):
        x = ord(x)
        return self.is_number(x) or self.is_upper_alpha(x) or self.is_lower_alpha(x)

    def is_number(self, x):
        return 48 <= x <= 57

    def is_upper_alpha(self, x):
        return 65 <= x <= 90

    def is_lower_alpha(self, x):
        return 97 <= x <= 122

    def is_alpha(self, x):
        return self.is_upper_alpha(x) or self.is_lower_alpha(x)


if __name__ == '__main__':
    s = " "
    solu = Solution()
    print(solu.isPalindrome(s))
