# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

w = QWidget()
w.resize(480, 320)
w.move(300, 300)
w.setWindowTitle("MainWindow")
w.show()


print("Hello world!")
sys.exit(app.exec_())
