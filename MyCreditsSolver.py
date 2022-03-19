import numpy as np


class MyCreditSolver:
    credits_num: int
    # simplex table
    table: [[]]
    # rows
    m: int
    # cols
    n: int
    # basis vars list
    basis: []

    def __init__(self, greensPerCredit: int):
        self.credits_num = 1200000 / greensPerCredit
        # canonical view
        matrix = [[self.credits_num, 1, 1, 1, 1, 1],  # sum constraint
                  [0, 1.5, 0.75, -0.25, 0.25, -0.5],  # non-return constraint
                  [0, 0.4, 0.4, 0.4, -0.6, -0.6],  # 40% constraint
                  [0, -0.5, -0.5, -0.5, 0.5, 0.5],  # 50% constraint
                  [0, -0.14, -0.13, -0.12, -0.125, -0.1]]  # target func
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.table = [[0 for _ in range(self.n + self.m - 1)] for i in range(self.m)]
        self.basis = []
        for r in range(0, self.m):
            for c in range(0, self.n):
                if c < self.n:
                    self.table[r][c] = matrix[r][c]
                else:
                    self.table[r][c] = 0
            # sets coef 1 on basis var in a row
            if (self.n + r) < len(self.table[0]):
                self.table[r][self.n + r] = 1
                self.basis.append(self.n + r)
        self.n = len(self.table[0])

    def find_main_row(self, main_col: int):
        main_row = 0
        for r in range(0, self.m - 1):
            if self.table[r][main_col] > 0:
                main_row = r
                break
        for r in range(main_row + 1, self.m - 1):
            if (self.table[r][main_col] > 0) and ((self.table[r][0] / self.table[r][main_col]) < (
                    self.table[main_row][0] / self.table[main_row][main_col])):
                main_row = r
        return main_row

    def IsItEnd(self):
        flag = True
        for r in range(1, self.n):
            if self.table[self.m - 1][r] < 0:
                flag = False
                break
        return flag

    def find_main_col(self):
        main_col = 1
        for j in range(2, self.n):
            if self.table[self.m - 1][j] < self.table[self.m - 1][main_col]:
                main_col = j
        return main_col

    def solve(self):
        mainCol: int
        mainRow: int
        result = []
        while not self.IsItEnd():
            mainCol = self.find_main_col()
            mainRow = self.find_main_row(mainCol)
            self.basis[mainRow] = mainCol
            new_table = [[0 for _ in range(0, self.n)] for _ in range(self.m)]
            for j in range(0, self.n):
                new_table[mainRow][j] = self.table[mainRow][j] / self.table[mainRow][mainCol]
            for i in range(0, self.m):
                if i == mainRow:
                    continue
                for j in range(0, self.n):
                    new_table[i][j] = self.table[i][j] - self.table[i][mainCol] * new_table[mainRow][j]
            self.table = new_table
        for i in range(0, 5):
            k = self.basis.index(i + 1)
            if k != -1:
                result.append(int(self.table[k][0]))
            else:
                result.append(0)
        return result
    # self.equations.append((Variable('personal', 0.14), Variable('auto', 0.13), Variable('housing', 0.12),
    # Variable('agricult', 0.125), Variable('business', 0.1)), 1) model += 0.14 * personal + 0.13 * auto + 0.12 *
    # housing + 0.125 * agricult + 0.1 * business  # target func model += personal + auto + housing + agricult +
    # business <= self.credits_num  # summary constraint model += 0.1 * personal + 0.07 * auto + 0.03 * housing +
    # 0.05 * agricult + 0.02 * business <= 0.04 * ( personal + auto + housing + agricult + business)  # non-return
    # constraint model += agricult + business >= 0.4 * (personal + auto + housing + agricult + business)  # 40%
    # constraint model += personal + auto + housing >= 0.5 * (personal + auto + housing + agricult + business)  # 50%
    # constraint
