
from PyQt5 import QtWidgets, uic
from Codigo import Func


def cal():
    dado = str(Caulc.Monitor.text())
    D = dado.strip()
    print(D)


app = QtWidgets.QApplication([])
Caulc = uic.loadUi("CalculadoraDesigner.ui")

Caulc.Bok.clicked.connect(cal)

Caulc.B1.clicked.connect(Func.Dig1)
Caulc.B2.clicked.connect(Func.Dig2)
Caulc.B3.clicked.connect(Func.Dig3)
Caulc.B4.clicked.connect(Func.Dig4)
Caulc.B5.clicked.connect(Func.Dig5)
Caulc.B6.clicked.connect(Func.Dig6)
Caulc.B7.clicked.connect(Func.Dig7)
Caulc.B8.clicked.connect(Func.Dig8)
Caulc.B9.clicked.connect(Func.Dig9)
Caulc.B0.clicked.connect(Func.Dig0)
Caulc.Bmais.clicked.connect(Func.DigMais)
Caulc.Bmenos.clicked.connect(Func.DigMenos)
Caulc.Bx.clicked.connect(Func.Digmult)
Caulc.Bdivi.clicked.connect(Func.DigDiv)

Caulc.Bdel.clicked.connect(Func.DigDel)


Caulc.show()
app.exec_()