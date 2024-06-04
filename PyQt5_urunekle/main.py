import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *  # sayfamdaki tüm widgetların önüne QtWidgets.xxx gibi eklemeler yapmamız lazım ama QtWidgets dakilerin hepsini import edersek başlarına QtWidgets yazmamıza gerek kalmaz
# eğer * koymazsan qmessagebox gibi widget i bulamaz,* ı koyarsan veya * olmasa bile PyQt5.QtWidgets bunu dahil etmezsen direkt ismiyle kullanamazsın 

from Urun_Ekle import *



uygulama = QApplication(sys.argv) # burada,uygulamamızdaki tüm argümanları çağırırız

pencere = QMainWindow()

ui = Ui_MainWindow() # bizim widget lar bunun içinde


ui.setupUi(pencere) # burada,tanımlamış olduğumuz penecreyi form ile birleştirmiş oluruz

pencere.show()


# veri tabanı işlemleri

import sqlite3

baglanti = sqlite3.connect("urunler.db")

islem = baglanti.cursor() # bu bir imleçtir,veritabanındaki işlemleri bununla yaparız

baglanti.commit() # yapmış olduğumuz değişiklikleri veritabanına kaydeder


table = islem.execute("create table if not exists urun(urunKodu int,urunAdi text,birimFiyat int,stokMiktari int,urunAciklamasi text,marka text,kategori text)")

baglanti.commit()


def kayit_ekle():
    urunKodu = int(ui.lneurunKodu.text()) # ui = Ui_MainWindow() -> bizim widget lar bunun içinde , lneurunKodu -> bu bizim exe de qlineedit e benim verdiğim isim
    urunAdi = ui.lneurunAdi.text()
    birimFiyat = int(ui.lnebirimFiyat.text())
    stokMiktari = int(ui.lnestokMiktari.text())
    urunAciklamasi = ui.lneurunAciklamasi.text()
    marka = ui.cmbMarka.currentText()  # combobox a biz cmbMarka ismini verdik. currentText -> seçildiği anda hangisi seçilmişse o dur,onu versin bize diye
    kategori = ui.cmbKategori.currentText()

    try:
        ekle = "Insert into urun (urunKodu,urunAdi,birimFiyat,stokMiktari,urunAciklamasi,marka,kategori) values (?,?,?,?,?,?,?)"
        islem.execute(ekle,(urunKodu,urunAdi,birimFiyat,stokMiktari,urunAciklamasi,marka,kategori)) # (urunKodu buradaki parantezi açmazsan database e veri eklenmez hata alırsın,demet şeklinde olmalı yani
        baglanti.commit()
        kayit_listele()
        ui.statusbar.showMessage("Kayıt ekleme işlemi başarılı",10000) # burdakai 10000,10 saniye bu yazının beklemesi için
    except Exception as error: # çıkan hataya error ismini verdik
        ui.statusbar.showMessage("Kayıt eklenemedi Hata Çıktı ==="+str(error))

def kayit_listele():
    ui.tblListele.clear() # eğer tekrar lislemek istersek önceki listenenleri temizlemesi için
    ui.tblListele.setHorizontalHeaderLabels(("Ürün Kodu","Ürün Adı","Birim Fiyatı","Stok Miktarı","Ürün Açıklama","Marka","Kategori")) # tablomuzun başlıklarını oluşturduk
    
    ui.tblListele.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # tablonun altında scrolbar oluşacak sığmayan verileri sağa sola kaydıran,onu iptal ettik
    
    sorgu = "select * from urun" # urun tablosundaki tüm verileri çeker
    islem.execute(sorgu)

    for indexSatir,kayitNumarasi in enumerate(islem):
        for indexSutun,kayitSutun in enumerate(kayitNumarasi):
            ui.tblListele.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))


def kategoriye_gore_listele():
    listenecek_kategori = ui.cmbKategoriListele.currentText() # o an hangisi seçilmişse onun metnini verir

    sorgu = "select * from urun where kategori = ?"
    islem.execute(sorgu,(listenecek_kategori,))
    ui.tblListele.clear()
    for indexSatir,kayitNumarasi in enumerate(islem):
        for indexSutun,kayitSutun in enumerate(kayitNumarasi):
            ui.tblListele.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))




def kayit_sil():
    sil_mesaj = QMessageBox.question(pencere,"Silme Onayı","Silmek İstediğinizden Emin Misiniz ?",QMessageBox.Yes | QMessageBox.No) # silme işlemi için son kez onay ister

    if sil_mesaj == QMessageBox.Yes :
        secilen_kayit = ui.tblListele.selectedItems() # sileceğimiz şeyi listeden-tabloadan seçerek silelim diye
        silinecek_kayit = secilen_kayit[0].text() # 0.indekste seçilen ürünün ürün kodu vardı.

        sorgu = "delete from urun where urunKodu = ?"
        try:
            islem.execute(sorgu,(silinecek_kayit,))
            baglanti.commit()
            ui.statusbar.showMessage("Kayıt Başarıyla Silindi")
            kayit_listele()
        except Exception as error:
            ui.statusbar.showMessage("Silinirken Hata Çıktı ==="+str(error) )    
    else:
        ui.statusbar.showMessage("Silme İşlemi İptal Edildi")



def kayit_guncelle():
    guncelle_mesaj = QMessageBox.question(pencere,"Güncelleme Onayı","Güncellemek İstediğinizden Emin Misiniz ?",QMessageBox.Yes | QMessageBox.No) # "Güncelleme Onayı" -> önümüze çıkacak mesaj kutusunun başlığıdır
    if guncelle_mesaj == QMessageBox.Yes:
        #¯urunKodu,urunAdi,birimFiyat,stokMiktari,urunAciklamasi,marka,kategori
        try:
            urun_kodu = ui.lneurunKodu.text()
            urun_adi = ui.lneurunAdi.text()
            birim_fiyat = ui.lnebirimFiyat.text()
            stok_miktari = ui.lnestokMiktari.text()
            urun_aciklama = ui.lneurunAciklamasi.text()
            marka = ui.cmbMarka.currentText()
            kategori = ui.cmbKategori.currentText()

            if urun_adi == "" and birim_fiyat == "" and stok_miktari==""  and urun_aciklama=="" and marka=="" :
                islem.execute("update urun set kategori = ? where urunKodu = ?",(kategori,urun_kodu))

            elif urun_adi == "" and birim_fiyat == "" and stok_miktari==""  and urun_aciklama=="" and kategori=="" : # ürün kodunu girmesi zorunlu sadece markayı günceller
                islem.execute("update urun set marka = ? where urunKodu = ?",(marka,urun_kodu))    

            elif urun_adi == "" and birim_fiyat == "" and stok_miktari==""  and marka=="" and kategori=="" : # ürün kodunu girmesi zorunlu sadece urun açıklamasını günceller
                islem.execute("update urun set urunAciklamasi = ? where urunKodu = ?",(urun_aciklama,urun_kodu))    

            elif urun_adi == "" and birim_fiyat == "" and urun_aciklama==""  and marka=="" and kategori=="" : # sadece stok miktarını günceller
                islem.execute("update urun set stokMiktari = ? where urunKodu = ?",(stok_miktari,urun_kodu)) 

            elif urun_adi == "" and stok_miktari == "" and urun_aciklama==""  and marka=="" and kategori=="" : # sadece birim fiyatını günceller
                islem.execute("update urun set birimFiyat = ? where urunKodu = ?",(birim_fiyat,urun_kodu))   

            elif birim_fiyat == "" and stok_miktari == "" and urun_aciklama==""  and marka=="" and kategori=="" : # sadece urun adını günceller
                islem.execute("update urun set urunAdi = ? where urunKodu = ?",(urun_adi,urun_kodu))

            else:
                islem.execute("update urun set urunAdi = ?,birimFiyat = ?, stokMiktari = ? ,urunAciklamasi = ?,marka=?, kategori = ? where urunKodu = ?",(urun_adi,birim_fiyat,stok_miktari,urun_aciklama,marka,kategori,urun_kodu))
            baglanti.commit()
            kayit_listele()
            ui.statusbar.showMessage("Kayıt Başarıyla Güncellendi")
        except Exception as error:
            ui.statusbar.showMessage("Kayıt Güncellemede Hata Çıktı ==="+str(error))
    else:
        ui.statusbar.showMessage("Güncelleme İptal Edildi")
# BUTONLAR

ui.btnEkle.clicked.connect(kayit_ekle)

ui.btnListele.clicked.connect(kayit_listele)

ui.btnKategoriyeGoreListele.clicked.connect(kategoriye_gore_listele)

ui.btnSil.clicked.connect(kayit_sil)

ui.btnGuncelle.clicked.connect(kayit_guncelle)





sys.exit(uygulama.exec_())













