from PyQt5.QtWidgets import *
from signalslot_python import Ui_MainWindow

class signalslotPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sayfa = Ui_MainWindow()
        self.sayfa.setupUi(self)
        self.sayfa.verticalScrollBar.valueChanged[int].connect(self.prfunc)

    def prfunc(self,myvalue):
        self.sayfa.progressBar.setValue(myvalue)


uygulama = QApplication([])

pencere = signalslotPage()

pencere.show()

uygulama.exec_()