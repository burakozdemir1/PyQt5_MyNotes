from PyQt5.QtWidgets import QApplication

from radio import radioPage


app = QApplication([])

pencere = radioPage()

pencere.show()

app.exec_()
