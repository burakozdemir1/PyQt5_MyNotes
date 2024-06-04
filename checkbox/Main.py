from cProfile import label

from PyQt5.QtWidgets import *

from onay_python import Ui_Form

class MainPage(QWidget):
    def __init__(self):
        self.secilensoslar = list()
        self.liste  = list()
        super().__init__()
        self.onay = Ui_Form()
        self.onay.setupUi(self)
        self.onay.pushButton_Goster.clicked.connect(self.Goster)


    def Goster(self):
            self.sosfiyat = {"mayonez":0,"ketcap":0,"acisos":0}
            if self.onay.checkBox_mayonez.isChecked():
                self.secilensoslar.append("Mayonez")
                self.sosfiyat
            if self.onay.checkBox_ketcap.isChecked():
                self.secilensoslar.append("Ketçap")            
            if self.onay.checkBox_acisos.isChecked():
                self.secilensoslar.append("Acı Sos")
            self.onay.label_soslar.setText(str(self.secilensoslar))



app = QApplication([])
pencere = MainPage()

pencere.show()

app.exec_()