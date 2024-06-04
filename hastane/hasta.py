from PyQt5.QtWidgets import *
from hasta_python import Ui_HastaEkrani
from PyQt5.QtCore import pyqtSignal

class HastaPage(QWidget):
    hastasinyali = pyqtSignal(str) # emit deki sinyali yani bilgi yi bu arkadaş gönderir
    def __init__(self):
        super().__init__()
        self.HastaFormu = Ui_HastaEkrani()
        self.HastaFormu.setupUi(self)
        self.HastaFormu.pushButton_gonder.clicked.connect(self.HastaMesaj) #butona tıkladığında slot oluşur


    def HastaMesaj(self):
        bilgi=self.HastaFormu.textEdit_hastamesaj.toPlainText() #texedit te metni bu şekilde alırız
        self.hastasinyali.emit(bilgi) # emit ile bilgi sinyali gönderilir










