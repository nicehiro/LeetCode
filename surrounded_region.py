from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return board
        m, n = len(board), len(board[0])

        def check(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if board[i][j] == 'X' or board[i][j] == 'U':
                return
            if board[i][j] == 'O':
                board[i][j] = 'U'
            check(i+1, j)
            check(i, j+1)
            check(i, j-1)
            check(i-1, j)

        for i in range(n):
            if board[0][i] == 'O':
                # check all 'O' item connect with this item
                check(0, i)
            if board[-1][i] == 'O':
                check(m-1, i)
        for i in range(m):
            if board[i][0] == 'O':
                check(i, 0)
            if board[i][-1] == 'O':
                check(i, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'U':
                    board[i][j] = 'O'


if __name__ == '__main__':
    solu = Solution()
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    # board = [["O","X","O"],["X","O","X"],["O","X","O"]]
    solu.solve(board)
    print(board)