from __future__ import print_function
from Cell import Cell
from copy import deepcopy


class Solver:

    def __init__(self):
        self.ANSWERS = []

    def start(self, puzzle):
        next = self.find_empty(puzzle)
        if not next[0]:
            self.ANSWERS.append(str(puzzle))
            self.answer(puzzle)
        else:
            x = next[1][0]
            y = next[1][1]
            possible_values = self.find_possible_values(x, y, puzzle)
            for value in possible_values:
                cur_sum_horizontal = 0
                cur_sum_vertical = 0
                new_puzzle = deepcopy(puzzle)
                if new_puzzle.puzzle[x][y - 1] != 'X':
                    cur_sum_horizontal = new_puzzle.puzzle[x][y - 1].sum_cell.line_sum
                if new_puzzle.puzzle[x - 1][y] != 'X':
                    cur_sum_vertical = new_puzzle.puzzle[x - 1][y].sum_cell.column_sum
                if (puzzle.puzzle[x][y + 1] == 'X' and
                        cur_sum_horizontal + value !=
                        puzzle.puzzle[x][y].band.line_sum):
                    continue
                elif (puzzle.puzzle[x + 1][y] == 'X' and
                      cur_sum_vertical + value !=
                      puzzle.puzzle[x][y].band.column_sum):
                    continue
                elif cur_sum_horizontal + value > puzzle.puzzle[x][y].band.line_sum:
                    continue
                elif cur_sum_vertical + value > puzzle.puzzle[x][y].band.column_sum:
                    continue
                new_puzzle.puzzle[x][y].set_new_value(value, cur_sum_horizontal, cur_sum_vertical)
                self.start(new_puzzle)

    def find_possible_values(self, x, y, puzzle):
        possible_values = set(i for i in range(10) if i > 0)
        for i in range(puzzle.height):
            if isinstance(puzzle.puzzle[i][y], Cell) and puzzle.puzzle[i][y].value in possible_values:
                possible_values.remove(puzzle.puzzle[i][y].value)
        for i in range(puzzle.width):
            if isinstance(puzzle.puzzle[x][i], Cell) and puzzle.puzzle[x][i].value in possible_values:
                possible_values.remove(puzzle.puzzle[x][i].value)
        return possible_values

    def find_empty(self, puzzle):
        for x in range(puzzle.height):
            for y in range(puzzle.width):
                if isinstance(puzzle.puzzle[x][y], Cell) and puzzle.puzzle[x][y].value == 0:
                    return True, (x, y)
        return False, (0, 0)

    def answer(self, puzzle):
        for i in range(puzzle.height):
            for j in range(puzzle.width):
                if puzzle.puzzle[i][j] == 'X':
                    print('X', end=' ')
                else:
                    t = puzzle.puzzle[i][j].value
                    print(str(t), end=' ')
            print('\n')
