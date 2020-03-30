class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l_a, l_b = len(a), len(b)
        l = max(l_a, l_b)
        res = ''
        c = 0
        for i in range(l):
            if i < l_a and i < l_b:
                t = int(a[l_a-1-i]) + int(b[l_b-1-i]) + c
            elif i < l_a:
                t = int(a[l_a-1-i]) + c
            elif i < l_b:
                t = int(b[l_b-1-i]) + c
            if t >= 2:
                t, c = t-2, 1
            else:
                c = 0
            res = str(t) + res
        if c != 0:
            res = str(c) + res
        return res


if __name__ == "__main__":
    s = Solution()
    a = '100'
    b = '110010'
    print(s.addBinary(a, b))
