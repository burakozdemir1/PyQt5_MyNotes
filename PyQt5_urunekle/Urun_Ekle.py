# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urun_ekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 101, 21))
        self.label_5.setObjectName("label_5")
        self.cmbMarka = QtWidgets.QComboBox(self.centralwidget)
        self.cmbMarka.setGeometry(QtCore.QRect(10, 320, 121, 31))
        self.cmbMarka.setObjectName("cmbMarka")
        self.cmbMarka.addItem("")
        self.cmbMarka.addItem("")
        self.cmbMarka.addItem("")
        self.cmbMarka.addItem("")
        self.cmbKategori = QtWidgets.QComboBox(self.centralwidget)
        self.cmbKategori.setGeometry(QtCore.QRect(140, 320, 121, 31))
        self.cmbKategori.setObjectName("cmbKategori")
        self.cmbKategori.addItem("")
        self.cmbKategori.addItem("")
        self.cmbKategori.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(140, 300, 91, 16))
        self.label_7.setObjectName("label_7")
        self.lneurunAciklamasi = QtWidgets.QLineEdit(self.centralwidget)
        self.lneurunAciklamasi.setGeometry(QtCore.QRect(10, 230, 251, 41))
        self.lneurunAciklamasi.setObjectName("lneurunAciklamasi")
        self.tblListele = QtWidgets.QTableWidget(self.centralwidget)
        self.tblListele.setGeometry(QtCore.QRect(290, 70, 551, 281))
        self.tblListele.setRowCount(30)
        self.tblListele.setColumnCount(7)
        self.tblListele.setObjectName("tblListele")
        self.cmbKategoriListele = QtWidgets.QComboBox(self.centralwidget)
        self.cmbKategoriListele.setGeometry(QtCore.QRect(430, 30, 141, 31))
        self.cmbKategoriListele.setObjectName("cmbKategoriListele")
        self.cmbKategoriListele.addItem("")
        self.cmbKategoriListele.addItem("")
        self.cmbKategoriListele.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 30, 121, 31))
        self.label_8.setObjectName("label_8")
        self.btnKategoriyeGoreListele = QtWidgets.QPushButton(self.centralwidget)
        self.btnKategoriyeGoreListele.setGeometry(QtCore.QRect(590, 30, 141, 31))
        self.btnKategoriyeGoreListele.setObjectName("btnKategoriyeGoreListele")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 91, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(100, 70, 161, 111))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lneurunKodu = QtWidgets.QLineEdit(self.widget1)
        self.lneurunKodu.setObjectName("lneurunKodu")
        self.verticalLayout_2.addWidget(self.lneurunKodu)
        self.lneurunAdi = QtWidgets.QLineEdit(self.widget1)
        self.lneurunAdi.setObjectName("lneurunAdi")
        self.verticalLayout_2.addWidget(self.lneurunAdi)
        self.lnebirimFiyat = QtWidgets.QLineEdit(self.widget1)
        self.lnebirimFiyat.setObjectName("lnebirimFiyat")
        self.verticalLayout_2.addWidget(self.lnebirimFiyat)
        self.lnestokMiktari = QtWidgets.QLineEdit(self.widget1)
        self.lnestokMiktari.setObjectName("lnestokMiktari")
        self.verticalLayout_2.addWidget(self.lnestokMiktari)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 370, 591, 30))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnEkle = QtWidgets.QPushButton(self.widget2)
        self.btnEkle.setObjectName("btnEkle")
        self.horizontalLayout.addWidget(self.btnEkle)
        self.btnSil = QtWidgets.QPushButton(self.widget2)
        self.btnSil.setObjectName("btnSil")
        self.horizontalLayout.addWidget(self.btnSil)
        self.btnGuncelle = QtWidgets.QPushButton(self.widget2)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.horizontalLayout.addWidget(self.btnGuncelle)
        self.btnListele = QtWidgets.QPushButton(self.widget2)
        self.btnListele.setObjectName("btnListele")
        self.horizontalLayout.addWidget(self.btnListele)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cmbMarka.setCurrentIndex(-1)
        self.cmbKategori.setCurrentIndex(-1)
        self.cmbKategoriListele.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Ürün Açıklaması"))
        self.cmbMarka.setItemText(0, _translate("MainWindow", "Acer"))
        self.cmbMarka.setItemText(1, _translate("MainWindow", "Samsung"))
        self.cmbMarka.setItemText(2, _translate("MainWindow", "Apple"))
        self.cmbMarka.setItemText(3, _translate("MainWindow", "Oppo"))
        self.cmbKategori.setItemText(0, _translate("MainWindow", "Telefon"))
        self.cmbKategori.setItemText(1, _translate("MainWindow", "Bilgisayar"))
        self.cmbKategori.setItemText(2, _translate("MainWindow", "Beyaz Eşya"))
        self.label_6.setText(_translate("MainWindow", "Ürün Markası"))
        self.label_7.setText(_translate("MainWindow", "Ürün Kategorisi"))
        self.cmbKategoriListele.setItemText(0, _translate("MainWindow", "Telefon"))
        self.cmbKategoriListele.setItemText(1, _translate("MainWindow", "Bilgisayar"))
        self.cmbKategoriListele.setItemText(2, _translate("MainWindow", "Beyaz Eşya"))
        self.label_8.setText(_translate("MainWindow", "Kategoriye Göre Listele"))
        self.btnKategoriyeGoreListele.setText(_translate("MainWindow", "Kategoriye Göre Listele"))
        self.label.setText(_translate("MainWindow", "Ürün Kodu"))
        self.label_2.setText(_translate("MainWindow", "Ürün Adı"))
        self.label_3.setText(_translate("MainWindow", "Birim Fiyatı"))
        self.label_4.setText(_translate("MainWindow", "Stok Miktarı"))
        self.btnEkle.setText(_translate("MainWindow", "Ürün Ekle"))
        self.btnSil.setText(_translate("MainWindow", "Ürün Sil"))
        self.btnGuncelle.setText(_translate("MainWindow", "Ürün Güncelle"))
        self.btnListele.setText(_translate("MainWindow", "Ürün Listeleme"))
