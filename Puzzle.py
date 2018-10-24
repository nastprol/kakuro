class Puzzle:
    def __init__(self, puzzle):
        self.height = len(puzzle)
        self.width = len(puzzle[0])
        self.puzzle = puzzle

    def __str__(self):
        s = ''
        for i in range(self.height):
            for j in range(self.width):
                if self.puzzle[i][j] == 'X':
                    s += 'X '
                else:
                    s += str(self.puzzle[i][j].value) + ' '
            s += '\n'
        return s
