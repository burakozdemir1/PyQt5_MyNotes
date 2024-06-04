from PyQt5.QtWidgets import *
from urun_kategori_python import Ui_Form

class UrunKategoriPage(QWidget):
    def __init__(self):
        super().__init__()
        self.kategoriform = Ui_Form()
        self.kategoriform.setupUi(self)
        