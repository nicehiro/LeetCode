import re


class Solution:
    def isNumber(self, s: str) -> bool:
        regex = r'\s*[+-]?((([.]\d+)|(\d+([.]\d+)))|(\d+([.]\d+)?(e[+-]?\d+([.]\d+))?))\s*$'
        res = re.match(regex, s)
        return False if res is None else True


if __name__ == "__main__":
    s = Solution()
    st = ' '
    print(s.isNumber(st))