from PyQt5 import uic

with open("ui3.py","w",encoding="utf-8") as fout:
    uic.compileUi("loginUi3.ui",fout)


# NOT: qt.exe de gerçekleştirdiğin veya değiştirdiğin her şey için bu kodu tekrar çalıştır ki kod kendini güncellesin