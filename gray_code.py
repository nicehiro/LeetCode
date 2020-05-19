from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res, extra = [0], 1
        for _ in range(n):
            t = len(res)
            for j in range(t-1, -1, -1):
                res.append(res[j] + extra)
            extra <<= 1
        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.grayCode(0))
                