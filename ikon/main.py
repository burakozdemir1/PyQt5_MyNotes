from PyQt5.QtWidgets import *

from ikon_python import Ui_Form


class ikonPage(QWidget):
    def __init__(self):
        super().__init__()
        self.dondurmasayisi=0
        self.ikon = Ui_Form()
        self.ikon.setupUi(self)
        self.ikon.pushButton.clicked.connect(self.arttir)
        self.ikon.pushButton_2.clicked.connect(self.azalt)
    def arttir(self):
        self.dondurmasayisi += 1
        self.ikon.label.setText(str(self.dondurmasayisi))
        print("asf")


    def azalt(self):
        self.dondurmasayisi -= 1
        self.ikon.label.setText(str(self.dondurmasayisi))       


app = QApplication([])

pencere = ikonPage()

pencere.show()

app.exec_()