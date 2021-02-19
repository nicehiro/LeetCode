from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        def flip(s, e):
            for i in range(s, e):
                A[i] = 0 if A[i] == 1 else 1

        n = len(A)

        def dp(s):
            """Dynamic programming."""
            if s > n - K:
                for i in range(s, n):
                    if A[i] == 0:
                        return -(2 ** 32)
                return 0
            if s >= n:
                return 0
            if A[s] == 1:
                return dp(s + 1)
            flip(s, s + K)
            return 1 + dp(s + 1)

        def difference_array():
            """Use difference array."""
            # reA means flips of A
            # d is difference array of reA, init is [0, ..., 0]
            d = [0 for _ in range(n + 1)]
            res_count = 0
            ans = 0
            for i in range(n):
                res_count += d[i]
                if A[i] + res_count % 2 == 0:
                    if i + K > n:
                        return -1
                    ans += 1
                    res_count += 1
                    d[i + K] -= 1
            return ans

        return difference_array()


if __name__ == "__main__":
    s = Solution()
    A = [1, 1]
    K = 2
    print(s.minKBitFlips(A, K))
