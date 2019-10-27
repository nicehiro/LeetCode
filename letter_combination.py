from typing import List


class Solution:
    def __init__(self):
        self.memory = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        for i in digits:
            res = self.concat(res, self.memory[i])
        return res

    def concat(self, l1: list, l2: list) -> list:
        results = []
        if len(l1) == 0:
            return l2
        for i in l1:
            for j in l2:
                results.append(i + j)
        return results


if __name__ == '__main__':
    s = Solution()
    digits = '23'
    print(s.letterCombinations(digits))
