from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens or len(tokens) == 0:
            return 0
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        i, n = 0, len(tokens)
        res = 0
        while i < n:
            num = tokens[i]
            if num in ['+', '-', '*', '/']:
                r = int(stack.pop(-1))
                l = int(stack.pop(-1))
                if num == '+':
                    res = l + r
                elif num == '-':
                    res = l - r
                elif num == '*':
                    res = l * r
                else:
                    flag = -1 if (l > 0) ^ (r > 0) else 1
                    res = flag * (abs(l) // abs(r))
                stack.append(res)
            else:
                stack.append(num)
            i += 1
        return res


if __name__ == '__main__':
    solu = Solution()
    tokens = ['-6', '-4', '/']
    print(solu.evalRPN(tokens))
