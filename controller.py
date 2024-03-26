from PyQt5.QtWidgets import *
from view import *
import view

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, view.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def makeUIWork(self):
        self.setFixedSize(self.size())
        self.pushButton.clicked.connect(self.submit)
        self.pushButton_2.clicked.connect(self.clear)

    def submit(self):
        if not self.lineEdit.text().isnumeric() or \
                not self.lineEdit_3.text().isnumeric() or \
                not self.lineEdit_2.text().isnumeric():
            self.summary.setText("Food, Drink, and Dessert need to be numeric.\ne. g. 10.25 not $10.25")
        else:
            if self.radioButton.isChecked():
                tipQ = .10
            elif self.radioButton_2.isChecked():
                tipQ = .15
            elif self.radioButton_3.isChecked():
                tipQ = .20
            food = float(self.lineEdit.text())
            drink = float(self.lineEdit_2.text())
            dessert = float(self.lineEdit_3.text())
            tax = (food + drink + dessert) * .10
            tip = (food + drink + dessert + tax) * tipQ
            total = food + drink + dessert + tax + tip
            self.summary.setText(f'\tSummary\n'
                                 f'Food:\t\t${food:.2f}\n'
                                 f'Drink:\t\t${drink:.2f}\n'
                                 f'Dessert:\t\t${dessert:.2f}\n'
                                 f'Tax:\t\t${tax:.2f}\n'
                                 f'Tip:\t\t${tip:.2f}\n\n'
                                 f'TOTAL:\t\t${total:.2f}\n')

        # def isFloat(num):
        #   try:
        #      float(num.strip())
        #     return True
        # except:
        #   return False

        # number = self.textEdit.text()

        # if isFloat(number):
        #   total = float(number.strip())
        #  self.summary.setText(f'{total} total')

    def clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.radioButton.setChecked(True)
        self.summary.clear()
