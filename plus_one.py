from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        f = False
        for i, d in enumerate(digits[::-1]):
            r = d + 1
            digits[l-1-i] = r if r <= 9 else 0
            if r <= 9:
                f = True
                break
        if not f:
            digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    s = Solution()
    l = [8, 9, 9]
    print(s.plusOne(l))
