import sys
from Solver import Solver
from Cell import Cell
from Puzzle import Puzzle
import re


class Main:

    def main(self, height, width, file):
        height += 1
        width += 1

        puzzle = None

        with open(file) as f:
            input = [i.strip() for i in f.readlines()]

            try:
                puzzle = self.make_puzzle(height, width, input)
            except Exception:
                return None

        solver = Solver()
        solver.start(puzzle)
        print(solver.ANSWERS)
        return solver.ANSWERS


    def make_puzzle(self,height, width, input):
        table = [i.split(' ') for i in input]
        pattern_cell = re.compile('\d*')
        line_sum_board = []
        column_sum_board = []
        for i in range(height):
            line_sum_board.append([])
            column_sum_board.append([])
            line_sum = 0
            for j in range(width):
                if table[i][j] != '0' and table[i][j] != 'X':
                    if table[i][j].split('/')[1] != 'X':
                        line_sum = int(table[i][j].split('/')[1])
                    line_sum_board[i].append('X')
                elif table[i][j] == '0':
                    line_sum_board[i].append(line_sum)
                else:
                    line_sum_board[i].append('X')

        for j in range(width):
            column_sum = 0
            for i in range(height):
                if table[i][j] != '0' and table[i][j] != 'X':
                    if table[i][j].split('/')[0] != 'X':
                        column_sum = int(table[i][j].split('/')[0])
                    column_sum_board[i].append('X')
                elif table[i][j] == '0':
                    column_sum_board[i].append(column_sum)
                else:
                    column_sum_board[i].append('X')
        board = []
        for x in range(height):
            board.append([])
            for y in range(width):
                cell = table[x][y]
                if re.fullmatch(pattern_cell, cell):
                    board[x].append(Cell(column_sum_board[x][y], line_sum_board[x][y], 0, 0))
                else:
                    board[x].append('X')

        puzzle = Puzzle(board)
        return puzzle


if __name__ == '__main__':
    m = Main()
    m.main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
