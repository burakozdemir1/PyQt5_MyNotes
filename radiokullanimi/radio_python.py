# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radio.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 480)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(290, 70, 241, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_ayran = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_ayran.setGeometry(QtCore.QRect(20, 40, 95, 20))
        self.radioButton_ayran.setObjectName("radioButton_ayran")
        self.radioButton_su = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_su.setGeometry(QtCore.QRect(20, 80, 95, 20))
        self.radioButton_su.setObjectName("radioButton_su")
        self.radioButton_kola = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_kola.setGeometry(QtCore.QRect(20, 130, 95, 20))
        self.radioButton_kola.setObjectName("radioButton_kola")
        self.radioButton_icetea = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_icetea.setGeometry(QtCore.QRect(20, 190, 95, 20))
        self.radioButton_icetea.setObjectName("radioButton_icetea")
        self.groupBox_menusecenekleri = QtWidgets.QGroupBox(Form)
        self.groupBox_menusecenekleri.setGeometry(QtCore.QRect(30, 70, 241, 241))
        self.groupBox_menusecenekleri.setObjectName("groupBox_menusecenekleri")
        self.radioButton_kucuk = QtWidgets.QRadioButton(self.groupBox_menusecenekleri)
        self.radioButton_kucuk.setGeometry(QtCore.QRect(20, 40, 95, 20))
        self.radioButton_kucuk.setObjectName("radioButton_kucuk")
        self.radioButton_orta = QtWidgets.QRadioButton(self.groupBox_menusecenekleri)
        self.radioButton_orta.setGeometry(QtCore.QRect(20, 80, 95, 20))
        self.radioButton_orta.setObjectName("radioButton_orta")
        self.radioButton_buyuk = QtWidgets.QRadioButton(self.groupBox_menusecenekleri)
        self.radioButton_buyuk.setGeometry(QtCore.QRect(20, 120, 95, 20))
        self.radioButton_buyuk.setObjectName("radioButton_buyuk")
        self.radioButton_super = QtWidgets.QRadioButton(self.groupBox_menusecenekleri)
        self.radioButton_super.setGeometry(QtCore.QRect(20, 170, 95, 20))
        self.radioButton_super.setObjectName("radioButton_super")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 370, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_3.setTitle(_translate("Form", "İçecek Seçenekleri"))
        self.radioButton_ayran.setText(_translate("Form", "Ayran"))
        self.radioButton_su.setText(_translate("Form", "Su"))
        self.radioButton_kola.setText(_translate("Form", "Kola"))
        self.radioButton_icetea.setText(_translate("Form", "ice Tea"))
        self.groupBox_menusecenekleri.setTitle(_translate("Form", "Menü Seçenekleri"))
        self.radioButton_kucuk.setText(_translate("Form", "Küçük "))
        self.radioButton_orta.setText(_translate("Form", "Orta"))
        self.radioButton_buyuk.setText(_translate("Form", "Büyük"))
        self.radioButton_super.setText(_translate("Form", "Süper"))
        self.pushButton.setText(_translate("Form", "Öde"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
