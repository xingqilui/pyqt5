# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

w = QWidget()
w.resize(480, 320)
w.move(300, 300)
w.setWindowTitle("MainWindow")
w.setWindowIcon(QIcon("image/fengxinpinggu.png"))

b1 = QPushButton("OK", w)
b1.resize(b1.sizeHint())
b1.move(50, 50)



print("Hello world!")
w.show()
sys.exit(app.exec_())
