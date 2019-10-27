class Solution:
    def myAtoi(self, str: str) -> int:
        new_s = str.strip()
        sign = 1
        res = 0
        if new_s == '':
            return 0
        sign = new_s[0]
        int_max = 2 ** 31 - 1
        int_min = -1 * 2 ** 31
        if sign == '+':
            sign = 1
        elif sign == '-':
            sign = -1
        elif sign >= '0' and sign <= '9':
            res = int(sign)
            sign = 1
        else:
            return 0
        for c in new_s[1:]:
            if c >= '0' and c <= '9':
                if sign == 1 and (res > int_max // 10 or (res == int_max // 10 and int(c) > int_max % 10)):
                    return int_max
                if sign == -1 and (res * sign < int(int_min / 10) or (res * sign == int(int_min / 10) and int(c) > abs(int_min) % 10)):
                    return int_min
                res = res * 10 + int(c)
            else:
                return res * sign
        return res * sign


if __name__ == '__main__':
    s = Solution()
    st = "-2147483649"
    print(s.myAtoi(st))
