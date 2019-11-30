from typing import List
import pprint
import ast

class Solution:
    """
    This method I use was stupid!

    Actually, just need one time search. Task 3 kinds of map to save
    number shows in different kinds of situation.
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(9):
            m = {str(i): 1 for i in range(1, 10)}
            m2 = {str(i): 1 for i in range(1, 10)}
            for j in range(9):
                if board[i][j] != '.':
                    if m[board[i][j]] <= 0:
                        return False
                    m[board[i][j]] -= 1
                if board[j][i] != '.':
                    if m2[board[j][i]] <= 0:
                        return False
                    m2[board[j][i]] -= 1
        for i in range(3):
            for j in range(3):
                m = {str(i): 1 for i in range(1, 10)}
                for k in range(9):
                    index = i * 27 + j * 3 + (k // 3) * 9 + k % 3
                    row = i * 3 + k // 3
                    column = j * 3 + k % 3
                    if board[row][column] == '.':
                        continue
                    if board[row][column] in m:
                        if m[board[row][column]] <= 0:
                            return False
                        m[board[row][column]] -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    board = '[[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]'
    board = ast.literal_eval(board)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(board)
    print(s.isValidSudoku(board))
