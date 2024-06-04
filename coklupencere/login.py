
# login, login_python dan çalışacak

from PyQt5.QtWidgets import *
from login_python import Ui_Form
from anapencere import AnapencerePage


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self) # setupUi ui_form daki fonks.
        self.anapencereac  = AnapencerePage()
        self.loginform.pushButton.clicked.connect(self.GirisYap)


    def GirisYap(self):
        kadi = self.loginform.lineEdit_kullaniciadi.text()
        sifre = self.loginform.lineEdit_sifre.text()

        if kadi =="burak" and sifre=="123":
            self.hide()
            self.anapencereac.show()