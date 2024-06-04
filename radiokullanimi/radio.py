from PyQt5.QtWidgets import *

from radio_python import Ui_Form


class radioPage(QWidget):
    def __init__(self):
        super().__init__()
        self.radioform = Ui_Form()
        self.radioform.setupUi(self)

        #menu olayları

        self.radioform.radioButton_buyuk.toggled.connect(self.menusecim)
        self.radioform.radioButton_kucuk.toggled.connect(self.menusecim)
        self.radioform.radioButton_orta.toggled.connect(self.menusecim)
        self.radioform.radioButton_super.toggled.connect(self.menusecim)

        #icecek olayları

        self.radioform.radioButton_ayran.toggled.connect(self.iceceksecim)
        self.radioform.radioButton_kola.toggled.connect(self.iceceksecim)
        self.radioform.radioButton_su.toggled.connect(self.iceceksecim)
        self.radioform.radioButton_icetea.toggled.connect(self.iceceksecim)


    def menusecim(self):
        secim = self.sender()

        if secim.isChecked():
              menusecim = secim.text()
              print(menusecim)
        


    def iceceksecim(self):
        secim = self.sender()

        if secim.isChecked():
              iceceksecim = secim.text()
              print(iceceksecim)         





