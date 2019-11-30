class Solution:
    def countAndSay(self, n: int) -> str:
        first = 1
        res = str(first)
        for i in range(2, n + 1):
            temp = res
            res = ''
            j = 0
            while j < len(temp):
                a = temp[j]
                k = j
                count = 0
                while k < len(temp) and temp[k] == a:
                    count += 1
                    k += 1
                res += '%d%s' % (count, a)
                j = k
        return res


if __name__ == '__main__':
    s = Solution()
    n = 1
    print(s.countAndSay(n))
