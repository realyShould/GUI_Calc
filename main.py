import sys

from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow

def last_word(str):
    tmp_list = []
    for n in str:
        tmp_list.append(n)
    tmp_list.reverse()
    return str(tmp_list)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tmp = ''
        self.tmp2 = ''
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
        if self.active == True:
            self.ui.lcdNumber.display('')
        if self.ui.lcdNumber.intValue() == 0:
            self.active = False
            self.ui.lcdNumber.display('1')
            self.tmp += '1'
        else:
            self.active = False
            if last_word(self.tmp) == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '1')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '1')

    def btn2Clicked(self):
        if self.active == True:
            self.ui.lcdNumber.display('')
        if self.ui.lcdNumber.intValue() == 0:
            self.active = False
            self.ui.lcdNumber.display('2')
            self.tmp += '2'
        else:
            self.active = False
            if last_word(self.tmp) == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '2')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '2')
    def btn3Clicked(self):
        if self.active == True:
            self.ui.lcdNumber.display('')
        if self.ui.lcdNumber.intValue() == 0:
            self.active = False
            self.ui.lcdNumber.display('3')
            self.tmp += '3'
        else:
            self.active = False
            if last_word(self.tmp) == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '3')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '3')
    def btn4Clicked(self):
        if self.active == True:
            self.ui.lcdNumber.display('')
        if self.ui.lcdNumber.intValue() == 0:
            self.active = False
            self.ui.lcdNumber.display('4')
            self.tmp += '4'
        else:
            self.active = False
            if last_word(self.tmp) == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '4')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '4')
    def btn5Clicked(self):
        if self.active == True:
            self.ui.lcdNumber.display('')
        if self.ui.lcdNumber.intValue() == 0:
            self.active = False
            self.ui.lcdNumber.display('5')
            self.tmp += '5'
        else:
            self.active = False
            if last_word(self.tmp) == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '5')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '5')
    def btn6Clicked(self):
        if self.active == True:
            self.ui.lcdNumber.display('')
        if self.ui.lcdNumber.intValue() == 0:
            self.active = False
            self.ui.lcdNumber.display('6')
            self.tmp += '6'
        else:
            self.active = False
            if last_word(self.tmp) == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '6')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '6')
    def btn7Clicked(self):
        if self.active == True:
            self.ui.lcdNumber.display('')
        if self.ui.lcdNumber.intValue() == 0:
            self.active = False
            self.ui.lcdNumber.display('7')
            self.tmp += '7'
        else:
            self.active = False
            if last_word(self.tmp) == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '7')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '7')
    def btn8Clicked(self):
        if self.active == True:
            self.ui.lcdNumber.display('')
        if self.ui.lcdNumber.intValue() == 0:
            self.active = False
            self.ui.lcdNumber.display('8')
            self.tmp += '8'
        else:
            self.active = False
            if last_word(self.tmp) == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '8')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '8')
    def btn9Clicked(self):
        if self.active == True:
            self.ui.lcdNumber.display('')
        if self.ui.lcdNumber.intValue() == 0:
            self.active = False
            self.ui.lcdNumber.display('9')
            self.tmp += '9'
        else:
            self.active = False
            if last_word(self.tmp) == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '9')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '9')
    def btn0Clicked(self):
        if self.active == True:
            self.ui.lcdNumber.display('')
        if self.ui.lcdNumber.intValue() == 0:
            self.active = False
            self.ui.lcdNumber.display('0')
            self.tmp += '0'
        else:
            self.active = False
            if last_word(self.tmp) == '.':
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.value()) + '0')
            else:
                self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '0')
    def btnDotClicked(self):
        if self.active == True:
            self.ui.lcdNumber.display('')
        self.active = False
        self.ui.lcdNumber.display(str(self.ui.lcdNumber.intValue()) + '.')
        self.tmp += '.'
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