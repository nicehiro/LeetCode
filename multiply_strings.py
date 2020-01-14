class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i in range(len(num2)-1, -1, -1):
            a = int(num2[i])
            for j in range(len(num1)-1, -1, -1):
                b = int(num1[j])
                res += a * b * 10 ** (len(num1) + len(num2) - i - j - 2)
        return str(res)

    def add_strnum(self, num1, num2):
        """Add two str number.
        """
        l1, l2 = len(num1), len(num2)
        if l1 >= l2:
            l_min, l_max = l2, l1
        else:
            l_min, l_max = l1, l2
            num1, num2 = num2, num1
        res = [0] * (l_max + 1)
        for i in range(l_min):
            res[l_max - i] += (int(num1[l_max-1-i]) + int(num2[l_min-1-i])) % 10
            res[l_max - i - 1] += (int(num1[l_max-1-i]) + int(num2[l_min-1-i])) // 10
        if l1 != l2:
            for i in range(l_max - l_min):
                res[l_max - l_min - i] += int(num1[l_max - l_min - 1 - i]) % 10
                res[l_max - l_min - i - 1] += int(num1[l_max - l_min - 1 - i]) // 10
        if res[0] == 0:
            return "".join([str(x) for x in res[1:]])
        else:
            return "".join([str(x) for x in res])



if __name__ == "__main__":
    s = Solution()
    num1 = '123'
    num2 = '11957'
    # print(s.add_strnum(num1, num2))
    print(s.multiply(num1, num2))
