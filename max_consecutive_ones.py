from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        return self.method2(A, K)

    def method1(self, A, K):
        P = [0]
        for i in range(len(A)):
            P.append(P[-1] + 1 - A[i])
        res = 0
        for right in range(len(A)):
            left = self.bisect(P, P[right + 1] - K)
            res = max(res, right - left + 1)
        return res

    def bisect(self, A, obj):
        n = len(A)
        l = 0
        r = n
        m = 0
        while l < r:
            m = (l + r) // 2
            if A[m] == obj:
                while m >= 0:
                    if A[m] != obj:
                        break
                    m -= 1
                return m + 1
            if A[m] < obj:
                l = m + 1
            else:
                r = m
        return m

    def method2(self, A, K):
        left, lsum, rsum = 0, 0, 0
        res = 0
        for right in range(len(A)):
            rsum += 1 - A[right]
            while rsum - lsum > K:
                lsum += 1 - A[left]
                left += 1
            res = max(res, right - left + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    A = [0, 0, 1, 1, 1, 0, 0]
    K = 0
    print(s.longestOnes(A, K))
