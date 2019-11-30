from typing import List
import pprint
import ast


class Solution:
    def __init__(self):
        self.solved = False
        self.matrix_n = 3
        self.row = self.column = 9
        self.rows = [[True for i in range(10)] for j in range(9)]
        self.columns = [[True for i in range(10)] for j in range(9)]
        self.boxes = [[True for i in range(10)] for j in range(9)]
        
    def idx(self, x, y):
        return (x // self.matrix_n) * 3 + y // self.matrix_n

    def place_number(self, d, x, y):
        self.rows[x][d] = self.columns[y][d] = self.boxes[self.idx(x, y)][d] = False
        self.board[x][y] = str(d)

    def could_place(self, d, x, y):
        return self.rows[x][d] and self.columns[y][d] and self.boxes[self.idx(x, y)][d]

    def place_next_number(self, x, y):
        if x == self.row - 1 and y == self.column - 1:
            self.solved = True
        elif y == self.row - 1:
            self.back_track(x + 1, 0)
        else:
            self.back_track(x, y + 1)

    def remove_number(self, d, x, y):
        self.rows[x][d] = self.columns[y][d] = self.boxes[self.idx(x, y)][d] = True
        self.board[x][y] = '.'

    def back_track(self, x, y):
        if self.board[x][y] == '.':
            for i in range(1, 10):
                if self.could_place(i, x, y):
                    self.place_number(i, x, y)
                    self.place_next_number(x, y)
                    if not self.solved:
                        self.remove_number(i, x, y)
        else:
            self.place_next_number(x, y)

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        for i in range(self.row):
            for j in range(self.column):
                if self.board[i][j] != '.':
                    self.place_number(int(self.board[i][j]), i, j)
        self.back_track(0, 0)


if __name__ == '__main__':
    s = Solution()
    st = '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
    board = ast.literal_eval(st)
    pp = pprint.PrettyPrinter(indent=4)
    s.solveSudoku(board)
    pp.pprint(s.board)