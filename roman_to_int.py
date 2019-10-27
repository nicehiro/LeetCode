class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'M': 1000,
                  'D': 500,
                  'C': 100,
                  'L': 50,
                  'X': 10,
                  'V': 5,
                  'I': 1}
        length = len(s)
        i = 0
        res = 0
        while i < length:
            if s[i] == 'I' and i+1 < length and (s[i+1] == 'X' or s[i+1] == 'V'):
                res += romans[s[i+1]] - 1
                i += 2
            elif s[i] == 'X' and i+1 < length and (s[i+1] == 'L' or s[i+1] == 'C'):
                res += romans[s[i+1]] - 10
                i += 2
            elif s[i] == 'C' and i+1 < length and (s[i+1] == 'D' or s[i+1] == 'M'):
                res += romans[s[i+1]] - 100
                i += 2
            else:
                res += romans[s[i]]
                i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    st = 'MCMXCIV'
    print(s.romanToInt(st))
