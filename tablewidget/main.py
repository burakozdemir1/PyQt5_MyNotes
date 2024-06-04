from PyQt5.QtWidgets import *
from tableform_python import Ui_Form

class tablePage(QWidget):
    def __init__(self):
        super().__init__()
        self.sayfa = Ui_Form()
        self.sayfa.setupUi(self)
        self.listele()
        self.sayfa.pushButton_SatirEkle.clicked.connect(self.SatirEkle)
        self.sayfa.pushButton_SatirSil.clicked.connect(self.SatirSil)
        self.sayfa.pushButton_SutunEkle.clicked.connect(self.SutunEkle)
        self.sayfa.pushButton_SutunSil.clicked.connect(self.SutunSil)
        self.sayfa.tableWidget.clicked.connect(self.Tiklandi)
        self.sayfa.tableWidget.cellChanged.connect(self.HucreChange) # hücrede değişiklik olduğunda slot oluşur

        
    def HucreChange(self):
        icerik = self.sayfa.tableWidget.currentItem().text() 
        secilisatir = self.sayfa.tableWidget.currentRow()
        secilisutun = self.sayfa .tableWidget.currentColumn()
        id=self.sayfa.tableWidget.item(secilisatir,0).text()
        print("seçili id :",id)
        print("seçili sütun :",secilisutun)
        print("yeni değer :",icerik)

    def Tiklandi(self):
        secilisatir = self.sayfa.tableWidget.currentRow() # o an seçili satırı alır
        secili_id = self.sayfa.tableWidget.item(secilisatir,0).text() # tabloda id 0.sütunda old için
        #print("Seçili ID: ",secili_id)


    def listele(self):
        self.sayfa.tableWidget.setColumnWidth(0,60)  # 0. sütunun genişliği
        self.sayfa.tableWidget.setColumnWidth(1,130)
        self.sayfa.tableWidget.setColumnWidth(2,130)
        self.sayfa.tableWidget.setColumnWidth(3,130)

        # veri tabani verileri

        kisiler = [{"id":"1","ad":"Burak","soyad":"Özdemir","tel":"05568465"},
                   {"id":"2","ad":"Murat","soyad":"Kaya","tel":"05641586"},
                   {"id":"3","ad":"Elif","soyad":"Yıldırım","tel":"054189465"}
                   ]

        self.sayfa.tableWidget.setRowCount(len(kisiler))
        satir = 0
        for veri in kisiler:
            self.sayfa.tableWidget.setItem(int(satir),0,QTableWidgetItem(str(veri["id"]))) #0.kolona id leri yazdık
            self.sayfa.tableWidget.setItem(int(satir),1,QTableWidgetItem(str(veri["ad"])))
            self.sayfa.tableWidget.setItem(int(satir),2,QTableWidgetItem(str(veri["soyad"])))
            self.sayfa.tableWidget.setItem(int(satir),3,QTableWidgetItem(str(veri["tel"])))

            satir+=1

    def SatirEkle(self):
        secilisatir = self.sayfa.tableWidget.currentRow()+1 # seçilen satırdan hemen sonra ekle
        self.sayfa.tableWidget.insertRow(secilisatir)
    def SatirSil(self):
        secilisatir = self.sayfa.tableWidget.currentRow()
        self.sayfa.tableWidget.removeRow(secilisatir) # seçili satırı siler
    def SutunEkle(self):
        secilisutun = self.sayfa.tableWidget.currentColumn()+1 # seçilen sütundan hemen sonra ekle
        self.sayfa.tableWidget.insertColumn(secilisutun)
    def SutunSil(self):
        secilisutun = self.sayfa.tableWidget.currentColumn() # seçilen sütunu siler
        self.sayfa.tableWidget.removeColumn(secilisutun)



app = QApplication([])

pencere = tablePage()
pencere.show()

app.exec_()






