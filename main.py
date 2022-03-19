import sys
from PyQt5 import QtWidgets
import saiio1
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
        solver = CreditSolver(credit_value=int(self.ui.valuePerCredit.text()))
        result = solver.solve()
        self.ui.resultText.setText(result)
        manualSolver = MyCreditSolver(greensPerCredit=int(self.ui.valuePerCredit.text()))
        result = manualSolver.solve()
        self.ui.resultTextManual.setText(result)






app = QtWidgets.QApplication([])
application = CreditsProblem()
application.show()

sys.exit(app.exec())



