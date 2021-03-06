from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]

        res = [0, 1]
        highbits = 0
        # for i in range(2, num + 1):
        #     binary_code = self.binary_code(i)
        #     res.append(1 + res[self.binary2int(binary_code[1:])])
        for i in range(2, num + 1):
            if i & (i - 1) == 0:
                highbits = i
            res.append(1 + res[i - highbits])
        return res

    def binary_code(self, num):
        if num <= 1:
            return str(num)
        return self.binary_code(num // 2) + str(num % 2)

    def binary2int(self, code):
        l = len(code)
        res = 0
        for i in range(l):
            if code[i] == "1":
                res += 2 ** (l - i - 1)
        return res


if __name__ == "__main__":
    s = Solution()
    num = 10
    print(s.countBits(num))
