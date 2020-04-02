from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.mtd_1(matrix)

    def mtd_1(self, m):
        """O(m+n) spaces

        官方 O(1) 空间算法并不严谨，所以我不打算实现了
        """
        l_m = len(m)
        l_n = len(m[0])
        f_m = [1 for _ in range(l_m)]
        f_n = [1 for _ in range(l_n)]
        for i in range(l_m):
            for j in range(l_n):
                if m[i][j] == 0:
                    f_m[i] = f_n[j] = 0
        for i in range(l_m):
            for j in range(l_n):
                m[i][j] = 0 if f_m[i] == 0 or f_n[j] == 0 else m[i][j]
        

if __name__ == "__main__":
    s = Solution()
    # matrix = [[1,1,1],
    #           [1,0,1],
    #           [1,1,1]]
    matrix = [[0,1,2,0],
              [3,4,5,2],
              [1,3,1,5]]
    s.setZeroes(matrix)
    print(matrix)