# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(340, 330))
        self.centralwidget.setMaximumSize(QtCore.QSize(340, 330))
        self.centralwidget.setObjectName("centralwidget")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(10, 210, 75, 51))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(100, 210, 75, 51))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(190, 210, 75, 51))
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(10, 150, 75, 51))
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(100, 150, 75, 51))
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(190, 150, 75, 51))
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(10, 90, 75, 51))
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(100, 90, 75, 51))
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(190, 90, 75, 51))
        self.btn9.setObjectName("btn9")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(10, 270, 71, 51))
        self.btn0.setObjectName("btn0")
        self.btnDot = QtWidgets.QPushButton(self.centralwidget)
        self.btnDot.setGeometry(QtCore.QRect(190, 270, 75, 51))
        self.btnDot.setObjectName("btnDot")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 10, 321, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.btnMult = QtWidgets.QPushButton(self.centralwidget)
        self.btnMult.setGeometry(QtCore.QRect(280, 90, 51, 51))
        self.btnMult.setObjectName("btnMult")
        self.btnSl = QtWidgets.QPushButton(self.centralwidget)
        self.btnSl.setGeometry(QtCore.QRect(280, 150, 51, 51))
        self.btnSl.setObjectName("btnSl")
        self.btnPlus = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlus.setGeometry(QtCore.QRect(280, 210, 51, 51))
        self.btnPlus.setObjectName("btnPlus")
        self.btnMinus = QtWidgets.QPushButton(self.centralwidget)
        self.btnMinus.setGeometry(QtCore.QRect(280, 270, 51, 51))
        self.btnMinus.setObjectName("btnMinus")
        self.end = QtWidgets.QPushButton(self.centralwidget)
        self.end.setGeometry(QtCore.QRect(100, 270, 75, 51))
        self.end.setObjectName("end")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btnDot.setText(_translate("MainWindow", "."))
        self.btnMult.setText(_translate("MainWindow", "*"))
        self.btnSl.setText(_translate("MainWindow", "/"))
        self.btnPlus.setText(_translate("MainWindow", "+"))
        self.btnMinus.setText(_translate("MainWindow", "-"))
        self.end.setText(_translate("MainWindow", "="))
