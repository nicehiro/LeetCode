from typing import List

class Solution:

    def __init__(self):
        self.results = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.sub('', 3, 3, 0)
        return self.results


    def sub(self, prefix, left_n, right_n, left_in_prefix_n):
        if left_n == 0:
            self.results.append(prefix + ')' * right_n)
            return
        if left_in_prefix_n == 0:
            prefix += '('
            left_in_prefix_n += 1
            left_n -= 1
            self.sub(prefix, left_n, right_n, left_in_prefix_n)
        else:
            self.sub(prefix+'(', left_n-1, right_n, left_in_prefix_n+1)
            self.sub(prefix+')', left_n, right_n-1, left_in_prefix_n-1)


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))