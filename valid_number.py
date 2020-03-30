import re


class Solution:
    """Stupid description of this problem. So just need more try.
    """
    def isNumber(self, s: str) -> bool:
        regex = r'\s*[+-]?((([.]\d+)|(\d+([.]\d*)?))((e[+-]?\d+)?))\s*$'
        res = re.match(regex, s)
        return False if res is None else True


if __name__ == "__main__":
    s = Solution()
    st = ' '
    print(s.isNumber(st))