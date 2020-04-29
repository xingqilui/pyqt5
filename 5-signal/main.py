# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QFileDialog, QTableView, QTableWidget, QFrame, QAbstractItemView, QTableWidgetItem
from PyQt5.QtGui import QIcon, QFont
from mainwindow import *



if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = QWidget()

    ui = Ui_Form()
    ui.setupUi(mw)

    mw.show()
    sys.exit(app.exec_())
