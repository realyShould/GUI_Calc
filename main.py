import sys

from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tmp = ''
        self.active = False

        self.ui.btn1.clicked.connect(self.btn1Clicked)
        self.ui.btn2.clicked.connect(self.btn2Clicked)
        self.ui.btn3.clicked.connect(self.btn3Clicked)
        self.ui.btn4.clicked.connect(self.btn4Clicked)
        self.ui.btn5.clicked.connect(self.btn5Clicked)
        self.ui.btn6.clicked.connect(self.btn6Clicked)
        self.ui.btn7.clicked.connect(self.btn7Clicked)
        self.ui.btn8.clicked.connect(self.btn8Clicked)
        self.ui.btn9.clicked.connect(self.btn9Clicked)
        self.ui.btn0.clicked.connect(self.btn0Clicked)
        self.ui.btnDot.clicked.connect(self.btnDotClicked)

        self.ui.btnPlus.clicked.connect(self.btnPlusClicked)
        self.ui.btnMinus.clicked.connect(self.btnMinusClicked)
        self.ui.btnMult.clicked.connect(self.btnMultClicked)
        self.ui.btnSl.clicked.connect(self.btnSlClicked)
        self.ui.end.clicked.connect(self.endClicked)

    def btn1Clicked(self):
        self.tmp += '1'
        if self.active == True:
            self.ui.lcdNumber.display('')
        if str(self.ui.lcdNumber.intValue()) == '0':
            try:
                if self.tmp[-1] != '.':
                    self.active = False
                    self.ui.lcdNumber.display('1')
            except:
                pass
        else:
            self.active = False
            if self.tmp[-1] == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '1')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '1')

    def btn2Clicked(self):
        self.tmp += '2'
        if self.active == True:
            self.ui.lcdNumber.display('')
        if str(self.ui.lcdNumber.intValue()) == '0':
            try:
                if self.tmp[-1] != '.':
                    self.active = False
                    self.ui.lcdNumber.display('2')
            except:
                pass
        else:
            self.active = False
            if self.tmp[-1] == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '2')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '2')
    def btn3Clicked(self):
        self.tmp += '3'
        if self.active == True:
            self.ui.lcdNumber.display('')
        if str(self.ui.lcdNumber.intValue()) == '0':
            try:
                if self.tmp[-1] != '.':
                    self.active = False
                    self.ui.lcdNumber.display('3')
            except:
                pass
        else:
            self.active = False
            if self.tmp[-1] == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '3')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '3')
    def btn4Clicked(self):
        self.tmp += '4'
        if self.active == True:
            self.ui.lcdNumber.display('')
        if str(self.ui.lcdNumber.intValue()) == '0':
            try:
                if self.tmp[-1] != '.':
                    self.active = False
                    self.ui.lcdNumber.display('4')
            except:
                pass
        else:
            self.active = False
            if self.tmp[-1] == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '4')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '4')
    def btn5Clicked(self):
        self.tmp += '5'
        if self.active == True:
            self.ui.lcdNumber.display('')
        if str(self.ui.lcdNumber.intValue()) == '0':
            try:
                if self.tmp[-1] != '.':
                    self.active = False
                    self.ui.lcdNumber.display('5')
            except:
                pass
        else:
            self.active = False
            if self.tmp[-1] == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '5')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '5')
    def btn6Clicked(self):
        self.tmp += '6'
        if self.active == True:
            self.ui.lcdNumber.display('')
        if str(self.ui.lcdNumber.intValue()) == '0':
            try:
                if self.tmp[-1] != '.':
                    self.active = False
                    self.ui.lcdNumber.display('6')
            except:
                pass
        else:
            self.active = False
            if self.tmp[-1] == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '6')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '6')
    def btn7Clicked(self):
        self.tmp += '7'
        if self.active == True:
            self.ui.lcdNumber.display('')
        if str(self.ui.lcdNumber.intValue()) == '0':
            try:
                if self.tmp[-1] != '.':
                    self.active = False
                    self.ui.lcdNumber.display('7')
            except:
                pass
        else:
            self.active = False
            if self.tmp[-1] == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '7')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '7')
    def btn8Clicked(self):
        self.tmp += '8'
        if self.active == True:
            self.ui.lcdNumber.display('')
        if str(self.ui.lcdNumber.intValue()) == '0':
            try:
                if self.tmp[-1] != '.':
                    self.active = False
                    self.ui.lcdNumber.display('8')
            except:
                pass
        else:
            self.active = False
            if self.tmp[-1] == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '8')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '8')
    def btn9Clicked(self):
        self.tmp += '9'
        if self.active == True:
            self.ui.lcdNumber.display('')
        if str(self.ui.lcdNumber.intValue()) == '0':
            try:
                if self.tmp[-1] != '.':
                    self.active = False
                    self.ui.lcdNumber.display('9')
            except:
                pass
        else:
            self.active = False
            if self.tmp[-1] == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '9')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '9')
    def btn0Clicked(self):
        self.tmp += '0'
        if self.active == True:
            self.ui.lcdNumber.display('')
        if str(self.ui.lcdNumber.intValue()) == '0':
            try:
                if self.tmp[-1] != '.':
                    self.active = False
                    self.ui.lcdNumber.display('0')
            except:
                pass
        else:
            self.active = False
            if self.tmp[-1] == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '0')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '0')
    def btnDotClicked(self):
        if self.active == True:
            self.ui.lcdNumber.display('')
        self.active = False
        self.tmp += '.'
        self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '.')
#####################
    def btnPlusClicked(self):
        if self.tmp != '':
            self.tmp += '+'
            self.ui.lcdNumber.display('')
    def btnMinusClicked(self):
        if self.tmp != '':
            self.tmp += '-'
            self.ui.lcdNumber.display('')
    def btnMultClicked(self):
        if self.tmp != '':
            self.tmp += '*'
            self.ui.lcdNumber.display('')
    def btnSlClicked(self):
        if self.tmp != '':
            self.tmp += '/'
            self.ui.lcdNumber.display('')
    def endClicked(self):
        if self.tmp != '':
            self.ui.lcdNumber.display(str(eval(self.tmp)))
            self.tmp = ''
            self.active = True

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())