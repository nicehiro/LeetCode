from typing import List
from copy import deepcopy


class Solution:
    def __init__(self):
        self.board = None
        self.word = None
        self.m = None
        self.n = None
        self.l = None

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.m = len(board)
        self.n = len(board[0])
        self.l = len(word)
        self.has_used = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        return self.recursive()

    def recursive(self) -> bool:
        has_used = [[False for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == self.word[0]:
                    # res = self.opt(i, j, 0, deepcopy(has_used))
                    res = self.opt2(i, j, 0)
                    if res:
                        return True
        return False

    def opt(self, i, j, k, u):
        if k >= self.l:
            return True
        if i < 0 or i >= self.m or j < 0 or j >= self.n or u[i][j] or self.board[i][j] != self.word[k]:
            return False
        # deepcopy method lost a lot of time
        u1 = deepcopy(u)
        u1[i][j] = True
        u2 = deepcopy(u)
        u2[i][j] = True
        u3 = deepcopy(u)
        u3[i][j] = True
        u4 = deepcopy(u)
        u4[i][j] = True
        return self.opt(i-1, j, k+1, u1) or\
               self.opt(i+1, j, k+1, u2) or\
               self.opt(i, j-1, k+1, u3) or\
               self.opt(i, j+1, k+1, u4)

    def opt2(self, i, j, k):
        if k == self.l - 1:
            return self.board[i][j] == self.word[k]
        if self.board[i][j] != self.word[k]:
            return False
        self.has_used[i][j] = True
        for direction in self.directions:
            i_, j_ = direction[0] + i, direction[1] + j
            if 0 <= i_ < self.m and 0 <= j_ < self.n and not self.has_used[i_][j_] and self.opt2(i_, j_, k+1):
                return True
        self.has_used[i][j] = False
        return False

        
if __name__ == "__main__":
    solu = Solution()
    # board = [['A','B','C','E'],
    #          ['S','F','C','S'],
    #          ['A','D','E','E']]
    # word = 'ABCCED'
    board = [['a']]
    word = 'a'
    print(solu.exist(board, word))