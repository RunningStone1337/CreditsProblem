from PyQt5 import QtWidgets
from CreditSolver import *
from saiio1 import Ui_MainWindow
from MyCreditsSolver import *


class CreditsProblem(QtWidgets.QMainWindow):
    def __init__(self):
        super(CreditsProblem, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Credits problem solver")
        self.ui.valuePerCredit.setPlaceholderText('enter value here')
        self.ui.solveButton.clicked.connect(self.solve)

    def solve(self):
        self.ui.resultText.setText('')
        self.ui.resultTextManual.setText('')
        cr_val=int(self.ui.valuePerCredit.text())
        solver = CreditSolver(credit_value=cr_val)
        result = solver.solve()
        self.ui.resultText.setText(result)
        manualSolver = MyCreditSolver(greens_per_credit=cr_val)
        result = manualSolver.solve()
        str_res = f"{result[0]} personal credits\n" \
                  f"{result[1]} auto credits\n" \
                  f"{result[2]} housing credits\n" \
                  f"{result[3]} agricult credits\n" \
                  f"{result[4]} business credits"
        self.ui.resultTextManual.setText(str_res)


app = QtWidgets.QApplication([])
application = CreditsProblem()
application.show()

sys.exit(app.exec())
