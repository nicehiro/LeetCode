class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        positive = '-' if (numerator > 0) ^ (denominator > 0) else ''
        numerator, denominator = abs(numerator), abs(denominator)
        quotient = int(numerator / denominator)
        remainder = numerator % denominator
        res = str(quotient)
        if remainder == 0:
            if quotient == 0:
                return res
            return positive + res
        res += '.'
        position_map = {remainder: 0}
        i = 0
        t = ''
        while remainder != 0:
            q_ = int(remainder * 10 / denominator)
            remainder = remainder * 10 % denominator
            t += str(q_)
            if remainder in position_map:
                r = t[:position_map[remainder]] + '(' + t[position_map[remainder]:] + ')'
                res = positive + res + r
                return res
            i += 1
            position_map[remainder] = i
        res = positive + res + t
        return res


if __name__ == '__main__':
    solu = Solution()
    print(solu.fractionToDecimal(-214747474747, 1))