from pulp import *


class CreditSolver:
    credits_num = 0

    def __init__(self, credit_value: int):
        self.credits_num = int(1200000 / credit_value)

    def solve(self):
        model = LpProblem("Maximize profit", LpMaximize)
        personal = LpVariable('personal', lowBound=0, cat='Integer')  # 50
        auto = LpVariable('auto', lowBound=0, cat='Integer')  # 50
        housing = LpVariable('housing', lowBound=0, cat='Integer')  # 50
        agricult = LpVariable('agricultural industry', lowBound=0, cat='Integer')  # 40
        business = LpVariable('business', lowBound=0, cat='Integer')  # 40
        # var template  personal + auto + housing + agricult + business
        model += 0.14 * personal + 0.13 * auto + 0.12 * housing + 0.125 * agricult + 0.1 * business  # target func
        model += personal + auto + housing + agricult + business <= self.credits_num  # summary constraint
        model += 0.1 * personal + 0.07 * auto + 0.03 * housing + 0.05 * agricult + 0.02 * business <= 0.04 * (
                personal + auto + housing + agricult + business)  # non-return constraint
        model += 0.4 * (personal + auto + housing + agricult + business) <= agricult + business  # 40% constraint
        model += 0.5 * (personal + auto + housing + agricult + business) <= personal + auto + housing  # 50% constraint
        model.solve()
        return str(f"{personal.varValue} personal credits\n"
                   f"{auto.varValue} auto credits\n"
                   f"{housing.varValue} housing credits\n"
                   f"{agricult.varValue} agricult credits\n"
                   f"{business.varValue} business credits\n"
                   f"{0.14 * personal.varValue + 0.13 * auto.varValue + 0.12 * housing.varValue + 0.125 * agricult.varValue + 0.1 * business.varValue} total profit")
