class MyCreditSolver:
    credits_num: int
    # simplex table
    table: [[]]
    rows: int
    cols: int
    # basis vars list
    basis: []

    def __init__(self, greens_per_credit: int):
        self.credits_num = int(1200000 / greens_per_credit)
        # canonical view
        matrix = [[self.credits_num, 1, 1, 1, 1, 1],  # sum constraint
                  [0, 1.5, 0.75, -0.25, 0.25, -0.5],  # non-return constraint
                  [0, 0.4, 0.4, 0.4, -0.6, -0.6],  # 40% constraint
                  [0, -0.5, -0.5, -0.5, 0.5, 0.5],  # 50% constraint
                  [0, -0.14, -0.13, -0.12, -0.125, -0.1]]  # target func
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        # creating simplex table with additional basis variables columns
        self.table = [[0 for _ in range(self.cols + self.rows - 1)] for _ in range(self.rows)]
        self.basis = []
        # filling table with default values
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                if c < self.cols:
                    self.table[r][c] = matrix[r][c]
                else:
                    self.table[r][c] = 0
            # sets coef 1 on basis var in a row
            if (self.cols + r) < len(self.table[0]):
                self.table[r][self.cols + r] = 1
                self.basis.append(self.cols + r)
        self.cols = len(self.table[0])

    def find_resolving_row(self, main_col: int):
        main_row = 0
        for r in range(0, self.rows - 1):
            if self.table[r][main_col] > 0:
                main_row = r
                break
        for r in range(main_row + 1, self.rows - 1):
            if (self.table[r][main_col] > 0) and ((self.table[r][0] / self.table[r][main_col]) < (
                    self.table[main_row][0] / self.table[main_row][main_col])):
                main_row = r
        return main_row

    def is_solution_founded(self):
        for r in range(1, self.cols):
            if self.table[self.rows - 1][r] < 0:
                return False
        return True

    def find_resolving_col(self):
        main_col = 1
        for j in range(2, self.cols):
            # searching the smallest element in the last row, which probably represents the solution
            if self.table[self.rows - 1][j] < self.table[self.rows - 1][main_col]:
                main_col = j
        return main_col

    def solve(self):
        # temp main column and row in table
        main_col: int
        main_row: int
        # result coefficients
        result = []
        while not self.is_solution_founded():
            main_col = self.find_resolving_col()
            main_row = self.find_resolving_row(main_col)
            self.basis[main_row] = main_col
            new_table = [[0 for _ in range(0, self.cols)] for _ in range(self.rows)]
            # divide all elements in the resolving row by resolving value
            for j in range(0, self.cols):
                new_table[main_row][j] = self.table[main_row][j] / self.table[main_row][main_col]
            # recalc all element according to the resolving row
            for i in range(0, self.rows):
                if i == main_row:
                    continue
                for j in range(0, self.cols):
                    new_table[i][j] = self.table[i][j] - self.table[i][main_col] * new_table[main_row][j]
            # reset table
            self.table = new_table
        for i in range(0, 5):
            if i + 1 in self.basis:
                k = self.basis.index(i + 1)
                result.append(round(self.table[k][0]))
            else:
                result.append(0)
        return result
