from PyQt5 import uic

with open("resources_2.py","w",encoding="utf-8") as fout:
    uic.compileUi("resources.qrc",fout)
