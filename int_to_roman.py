class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        nums = [1000, 500, 100, 50, 10, 5, 1]
        gaps = [4000, 900, 400, 90, 40, 9, 4]
        res = ''
        while num != 0:
            for i in range(7):
                t = int(num / nums[i])
                if t != 0:
                    if num >= gaps[i]:
                        if gaps[i] % 9 == 0:
                            res = res + romans[i+1] + romans[i-1]
                        elif gaps[i] % 4 == 0:
                            res = res + romans[i] + romans[i-1]
                        num -= gaps[i]
                    else:
                        res = res + romans[i] * t
                        num %= nums[i]
                    break
        return res


if __name__ == '__main__':
    s = Solution()
    num = 3
    print(s.intToRoman(num))
