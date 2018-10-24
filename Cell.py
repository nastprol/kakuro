class Cell:
    def __init__(self, sum_column, sum_line, cur_sum_column, cur_sum_line):
        self.sum_cell = SumCell(cur_sum_column, cur_sum_line)
        self.band = Band(sum_column, sum_line, False)
        self.value = 0

    def set_new_value(self, value, sum_line, sum_column):
        cur_sum_line = sum_line + value - self.value
        cur_sum_column = sum_column + value - self.value
        self.sum_cell = SumCell(cur_sum_column, cur_sum_line)
        self.value = value


class Band:
    def __init__(self, column_sum, line_sum, is_completed):
        self.column_sum = column_sum
        self.line_sum = line_sum
        self.is_completed = is_completed


class SumCell:
    def __init__(self, column_sum, line_sum):
        self.column_sum = column_sum
        self.line_sum = line_sum


class SpecialCell:
    def __init__(self, column_sum, line_sum, value):
        self.column_sum = column_sum
        self.line_sum = line_sum
        self.value = value
