from PyQt5.QtWidgets import *
from doktor_python import Ui_DoktorEkrani
from hasta import HastaPage
from PyQt5.QtCore import pyqtSignal


class HastaneSistemi(QWidget):
    def __init__(self):
        super().__init__()
        self.doktor = Ui_DoktorEkrani()
        self.doktor.setupUi(self)
        self.hasta = HastaPage()
        self.hasta.show()
        self.hasta.hastasinyali.connect(self.HastaBilgi) #hastaPage den bir sinyal gelirse (oradan gelen sinyali from hasta import HastaPage ile alırız)
        self.doktor.pushButton_gonder.clicked.connect(self.doktorBilgi)


    def HastaBilgi(self,bilgi): # hasta dan emit ile aldığımız bilgi :)
        self.doktor.label_doktorbilgi.setText(bilgi)


    def doktorBilgi(self): # doktor ekranından hasta ekranına mesaj gönderir
        doktorBilgi = self.doktor.textEdit_doktormesaj.toPlainText()
        self.hasta.HastaFormu.label_hastabilgi.setText(doktorBilgi)

app = QApplication([])
pencere = HastaneSistemi()
pencere.show()        
app.exec_()