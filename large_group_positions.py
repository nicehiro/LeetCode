from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l = r = 0
        res = []
        while r < len(s) + 1:
            if r == len(s) or s[l] != s[r]:
                if r - l >= 3:
                   res.append([l, r-1])
                l = r
            r += 1
        return res


if __name__ == '__main__':
    s = 'abbxxxxzzy'
    solu = Solution()
    print(solu.largeGroupPositions(s))
