# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todo_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 804)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_done = QtWidgets.QPushButton(Form)
        self.btn_done.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_done.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_done.setObjectName("btn_done")
        self.gridLayout.addWidget(self.btn_done, 0, 1, 1, 1)
        self.btn_block = QtWidgets.QPushButton(Form)
        self.btn_block.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_block.setObjectName("btn_block")
        self.gridLayout.addWidget(self.btn_block, 1, 1, 1, 1)
        self.btn_del = QtWidgets.QPushButton(Form)
        self.btn_del.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_del.setObjectName("btn_del")
        self.gridLayout.addWidget(self.btn_del, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 5, 1)
        self.btn_update = QtWidgets.QPushButton(Form)
        self.btn_update.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_update.setObjectName("btn_update")
        self.gridLayout.addWidget(self.btn_update, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textedit = QtWidgets.QTextEdit(Form)
        self.textedit.setMinimumSize(QtCore.QSize(0, 100))
        self.textedit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textedit.setObjectName("textedit")
        self.horizontalLayout.addWidget(self.textedit)
        self.btn_new = QtWidgets.QPushButton(Form)
        self.btn_new.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_new.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_new.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_new.setObjectName("btn_new")
        self.horizontalLayout.addWidget(self.btn_new)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.btn_new, self.textedit)
        Form.setTabOrder(self.textedit, self.btn_done)
        Form.setTabOrder(self.btn_done, self.btn_block)
        Form.setTabOrder(self.btn_block, self.btn_del)
        Form.setTabOrder(self.btn_del, self.btn_update)
        Form.setTabOrder(self.btn_update, self.listWidget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_done.setText(_translate("Form", "完成"))
        self.btn_block.setText(_translate("Form", "挂起"))
        self.btn_del.setText(_translate("Form", "删除"))
        self.btn_update.setText(_translate("Form", "更新"))
        self.btn_new.setText(_translate("Form", "新建"))
