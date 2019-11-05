class Solution:

    def is_match(self, a, b):
        if (a == '(' and b == ')')\
             or (a == '[' and b == ']')\
                 or (a == '{' and b == '}'):
            return True
        return False

    def isValid(self, s: str) -> bool:
        left = ['(', '[', '{']
        right = [')', ']', '}']
        l = []
        for c in s:
            if c in left:
                l.append(c)
            elif c in right:
                if len(l) > 0 and self.is_match(l.pop(), c):
                    pass
                else:
                    return False
        return True if len(l) == 0 else False


if __name__ == '__main__':
    st = '()'
    s = Solution()
    print(s.isValid(st))