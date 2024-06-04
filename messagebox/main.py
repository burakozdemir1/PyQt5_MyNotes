from PyQt5.QtWidgets import *
from messagebox_python import Ui_Form


class Mesaj(QWidget):
    def __init__(self):
        super(). __init__()
        self.mform = Ui_Form()
        self.mform.setupUi(self)
        self.mform.pushButton_MessageBox.clicked.connect(self.mesajver) #mesajver slotu oluşur


    def mesajver(self):
        #QMessageBox.information(self,"Bilgi","Butona Tıkladınız",QMessageBox.Close) # bilgi amaçlı mesaj kutusu çıkartır karşına
                                                                                    # QMessageBox.Close-> Kutun altında ok yerine close diye mesaj kutusunu kapat diye buton ekler
        
        #yanit = QMessageBox.information(self,"Bilgi","Evli misiniz ? ",QMessageBox.Yes,QMessageBox.No) #mesaj kutusunda yes ve no diye iki adet buton çıkarır

        #if yanit == QMessageBox.Yes:
        #    print("Evet")
        #elif yanit==QMessageBox.No:
        #    print("Hayır")    

        # information -> mesaj kutusunda i iconu olur
        # question -> mesa kutusunda ? ikonu olur
        # critical -> mesa kutusunda X ikonu yani hata uyarısı verir
        # warning -> mesaj kutusunda uyarı ikonu alırsın

        # QMessageBox.Close
        # QMessageBox.Yes
        # QMessageBox.No
        # QMessageBox.Ok
        # QMessageBox.Save
        # QMessageBox.Cancel
        # QMessageBox.Abort
        # QMessageBox.Retry
        # QMessageBox.Ignore


      #  QMessageBox.aboutQt(self,"Başlık") # qt designer hakkında bilgi verir

      #  QMessageBox.about(self,"Başlık","Deneme") # pencerenin ikonunu büyütüp mesaj olarak Deneme yazdırır

        # NOT :  QMessageBox.about(self,"Başlık","Deneme") Bu "Deneme" ksımını istediğin gibi özelleştirebilirsin çünkü burası html tabanlı bir şekilde çalışır


        mesajobje = QMessageBox()

        mesajobje.setIcon(QMessageBox.Warning)
        mesajobje.setText("Yaşınız 18'den büyük mü ?")
        mesajobje.setWindowTitle("Yaş Kısıtlaması")
        mesajobje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        mesajobje.setEscapeButton(QMessageBox.No)  # esc tuşuna bastığımda ne olacağını belirledik
        mesajobje.button(QMessageBox.Yes).setText("Evet,Büyüktür")
        mesajobje.button(QMessageBox.No).setText("Hayır,Küçüktür")
        yanit = mesajobje.exec_()  # mesajobje.exec_() -> BU YANITTIR
        if yanit == QMessageBox.Yes:
            print("Yaşınız Reşit")
        if yanit == QMessageBox.No:
            print("Reşit değilsiniz")    


app = QApplication([])

pencere = Mesaj()
pencere.show()
app.exec_()