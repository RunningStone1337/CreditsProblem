# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\PythonProjs\SAiIO1\saiio1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 369)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.solveButton = QtWidgets.QPushButton(self.centralwidget)
        self.solveButton.setGeometry(QtCore.QRect(16, 86, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.solveButton.setFont(font)
        self.solveButton.setObjectName("solveButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.valuePerCredit = QtWidgets.QLineEdit(self.centralwidget)
        self.valuePerCredit.setGeometry(QtCore.QRect(270, 90, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.valuePerCredit.setFont(font)
        self.valuePerCredit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.valuePerCredit.setObjectName("valuePerCredit")
        self.resultText = QtWidgets.QTextEdit(self.centralwidget)
        self.resultText.setGeometry(QtCore.QRect(20, 170, 241, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.resultText.setFont(font)
        self.resultText.setReadOnly(True)
        self.resultText.setObjectName("resultText")
        self.resultTextManual = QtWidgets.QTextEdit(self.centralwidget)
        self.resultTextManual.setGeometry(QtCore.QRect(270, 170, 231, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.resultTextManual.setFont(font)
        self.resultTextManual.setReadOnly(True)
        self.resultTextManual.setObjectName("resultTextManual")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.solveButton.setText(_translate("MainWindow", "Solve"))
        self.label.setText(_translate("MainWindow", "$ per credit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
