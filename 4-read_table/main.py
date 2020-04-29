# -*- coding: UTF-8 -*-
import sys
import xlwings as xw
import numpy as np
import pandas as pd

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from mainwindow import *


@staticmethod
def private_init(self, items):
    """
    initial function
    :param self:
    :param items: the items of the list
    """
    self.items = items
    self.checkbox_list = []  # selected items
    checklist = QListWidget()
    self.checklist = checklist
    self.setModel(checklist.model())
    self.setView(checklist)

    for i in range(len(self.items)):
        self.checkbox_list.append(QCheckBox())
        self.checkbox_list[i].setText(self.items[i])
        self.checkbox_list[i].setChecked(True)
        item = QListWidgetItem(checklist)
        checklist.setItemWidget(item, self.checkbox_list[i])
        # self.box_list[i].stateChanged.connect(self.show_selected)


@staticmethod
def private_get_selected(self) -> list:
    """
    get selected items
    :return:
    """
    print(self.items)
    ret = []
    for i in range(len(self.items)):
        if self.checkbox_list[i].isChecked():
            ret.append(self.checkbox_list[i].text())

    return ret


QComboBox.checklist = []
QComboBox.checkbox_list = []
QComboBox.private_init = private_init
QComboBox.private_get_selected = private_get_selected


class MainWindow(QWidget, Ui_Form):
    df = pd.DataFrame()
    df_filter = pd.DataFrame()
    col_filter = []

    def __init__(self):
        super(MainWindow, self).__init__()  # 使用super()调用父类构造函数
        # QWidget.__init__(self) # 使用另一种方式调用父类构造函数
        # Ui_Form.__init__(self) # 使用另一种方式调用父类构造函数

        self.setupUi(self)
        self.btn_ok.clicked.connect(self.input_data)
        self.btn_open.clicked.connect(self.open_file)

    def table_update(self):
        col = len(self.df_filter.columns)
        row = len(self.df_filter.index)
        print(col, row)

        self.table.clear()
        # self.table.setFrameShape(QFrame.NoFrame)  # 设置无边框
        self.table.set
        self.table.setColumnCount(col)  # 设置列数
        self.table.setRowCount(row)  # 设置行数
        self.table.setHorizontalHeaderLabels(self.df_filter.columns)  # 设置列标题
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止编辑单元格
        # self.table.resizeColumnsToContents() # 根据内容调整列宽
        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 设置表格宽度铺满两端
        # self.table.setGeometry(50, 50, 1400, 500) #设置位置坐标和大小
        self.table.verticalHeader().setDisabled(True)  # 禁止修改行高

        for i in range(0, row):
            for j in range(0, col):
                self.table.setItem(i, j, QTableWidgetItem(str(self.df_filter.values[i, j])))

    def combo_update(self):
        items = self.df_filter.columns.tolist()
        self.combo_box.addItems(items)
        self.combo_box.private_init(self.combo_box, items)

        for i in range(len(self.combo_box.checkbox_list)):
            self.combo_box.checkbox_list[i].stateChanged.connect(self.df_update)

    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./resource/",
                                                         "All Files (*);;Excel Files (.xlsx)")
        if filename is '':
            return

        self.df_filter = self.df = pd.read_excel(filename, sheet_name="Sheet1", header=0, decode="utf-8")
        self.combo_update()
        self.table_update()

    def input_data(self):
        self.textEdit.setText("aaa")

    def df_update(self):
        print("Signal 1 is coming")
        self.col_filter.clear()

        for i in range(len(self.combo_box.checkbox_list)):
            if self.combo_box.checkbox_list[i].isChecked():
                self.col_filter.append(self.combo_box.checkbox_list[i].text())
                print(self.combo_box.checkbox_list[i].text())

        self.df_filter = self.df[self.col_filter]
        self.table_update()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
