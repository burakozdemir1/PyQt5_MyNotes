from PyQt5.QtWidgets import *
from anapencere_python import Ui_MainWindow
from urun_listele import UrunListelePage
from urun_kategori import UrunKategoriPage
class AnapencerePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.anapencereform = Ui_MainWindow()
        self.anapencereform.setupUi(self)
        self.urunlisteleform = UrunListelePage()
        self.urunkategoriformu = UrunKategoriPage()
        self.anapencereform.urunlistele.triggered.connect(self.UrunListeleFormu)
        self.anapencereform.kategoriEkle.triggered.connect(self.UrunKategori)
    def UrunListeleFormu(self):
        self.urunlisteleform.show()

    def UrunKategori(self):
        self.urunkategoriformu.show()






















