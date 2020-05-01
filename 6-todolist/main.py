import sys
import os
import time
import logging
import numpy as np
import pandas as pd
import sqlite3 as sq
import json as js

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import QSize, Qt
# from sqlalchemy import create_engine

from todo_mainwindow import *


# 数据库操作类，用来执行数据访问
class TodoDataControl():
    data_index_name = ".//resource//index.json"
    data_sql_name = ".//resource//data.db"
    data_sql_table_name = "DATA"
    data_sql = None
    data_df = None

    def __init__(self):
        self.index_init()
        self.sql_init()
        self.data_sql = sq.connect(self.data_sql_name)

    def __del__(self):
        self.data_sql.close()
        pass

    # 初始化JSON文件
    def index_init(self):
        data = {"index": 0}

        if not os.path.exists(self.data_index_name):
            with open(self.data_index_name, 'w', encoding='utf-8') as file:
                js.dump(data, file)

    # 获取数据索引值FROM配置文件，索引为唯一值, 获取后+1并写回配置文件，保证索引值持续自增不减少
    def index_create(self):
        with open(self.data_index_name, 'r+', encoding="utf-8") as file:
            load_data = js.load(file)
            load_data["index"] += 1

            file.seek(0, 0)  # 将游标定位到文件头，从头开始写配置
            js.dump(load_data, file)

        return load_data['index']

    # 初始化数据库文件
    def sql_init(self):
        if not os.path.exists(self.data_sql_name):
            with open(self.data_sql_name, 'w', encoding='utf-8') as file:
                self.sql_create()

    # 创建数据库，使用sqlite3接口
    def sql_create(self):
        sql = sq.connect(self.data_sql_name)
        c = sql.cursor()
        c.execute("""
                     CREATE TABLE DATA(
                     ID             INT     NOT NULL PRIMARY KEY,
                     START_TIME     TEXT    NOT NULL,
                     END_TIME       TEXT    NOT NULL,
                     CONTENT        TEXT    NOT NULL,
                     STATUS         TEXT    NOT NULL);
                 """)
        sql.commit()

    # 创建数据库，使用pandas接口
    def sql_pandas_create(self):
        # df = pd.DataFrame(columns=["ID","创建时间","截至时间","内容","状态"])
        # engine = create_engine(self.data_index_name)
        # df.to_sql('DATA', engine)
        pass

    # 获取数据库表全部数据，转换成pandas的dataframe
    def get_all(self):
        query = "SELECT * FROM " + self.data_sql_table_name
        df = pd.read_sql_query(query, self.data_sql)
        return df

    # 获取数据库表的某一索引，转换成pandas的series
    def get_by_key(self, id):
        query = f"""SELECT * FROM {self.data_sql_table_name} WHERE ID={id};"""
        df = pd.read_sql_query(query, self.data_sql)
        print(df)

    # 插入一条新的索引到数据库
    def insert(self, start_time, end_time, content, status):
        query = f"""INSERT INTO {self.data_sql_table_name} VALUES ({self.index_create()}, "{start_time}", "{end_time}", "{content}", "{status}");"""
        c = self.data_sql.cursor()
        c.execute(query)
        self.data_sql.commit()

    # 修改数据库中的某一索引
    def modify(self, id, start_time, end_time, content, status):
        query = f"""UPDATE {self.data_sql_table_name} SET 
                START_TIME = "{start_time}", 
                END_TIME = "{end_time}", 
                CONTENT = "{content}", 
                STATUS = "{status}" 
                WHERE ID = {id};"""
        c = self.data_sql.cursor()
        c.execute(query)
        self.data_sql.commit()

    # 删除数据库中的某一索引
    def delete(self, id):
        query = f"""DELETE FROM {self.data_sql_table_name} WHERE ID={id};"""
        c = self.data_sql.cursor()
        c.execute(query)
        self.data_sql.commit()

    # 删除数据库的全部数据
    def clear(self):
        query = f"""DELETE FROM {self.data_sql_table_name};"""
        c = self.data_sql.cursor()
        c.execute(query)
        self.data_sql.commit()


class TodoWindow(QWidget, Ui_Form):
    def __init__(self):
        super(TodoWindow, self).__init__()

        self.data = TodoDataControl()

        self.setupUi(self)
        self.btn_new.setFocus()
        self.btn_new.setDefault(True)

        self.btn_new.clicked.connect(self.clicked_new)
        self.btn_update.clicked.connect(self.clicked_update)
        self.btn_done.clicked.connect(self.clicked_done)
        self.btn_del.clicked.connect(self.clicked_del)

    def listitem_widget_create(self):
        listitem_widget = QWidget()
        listitem_layout = QGridLayout()
        listitem_textedit = QTextEdit()
        listitem_layout.addItem(listitem_textedit, 0, 0)
        return listitem_widget

    def clicked_ok(self):
        print("Push OK")

        label_time_start = QLabel("2020/04/26")
        label_time_end = QLabel("2020/04/27")
        label_time_mid = QLabel(" - ")
        label_time_used = QLabel("【1天】")
        label_status = QLabel("--进行中--")
        label_text = QLabel(
            "我爱北京天安门，天安门上太阳升，伟大领袖毛主席，带领我们向前进！向前进！向前进！向前进！向前进！向前进！向前进！向前进！向前进！向前进！向前进！向前进！向前进！向前进！向前进！向前进！向前进！向前进！")
        spacer_right = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # line_bottom = QFrame()
        # line_bottom.setFrameShape(QtWidgets.QFrame.HLine)

        label_text.setWordWrap(True)
        label_time_start.setFont(QFont("华文琥珀", 10))
        label_time_end.setFont(QFont("华文琥珀", 10))
        label_time_mid.setFont(QFont("华文琥珀", 10))
        label_time_used.setFont(QFont("华文琥珀", 10))
        label_status.setFont(QFont("华文琥珀", 10))
        label_text.setFont(QFont("华文仿宋", 12))
        label_text.setAlignment((Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop))
        # label_text.setToolTip(label_text.text())

        # label.setText("<h1>Hello</h1>")
        widget_listitem = QWidget()
        layout_listitem = QGridLayout()
        layout_listitem.addWidget(label_time_start, 0, 0)
        layout_listitem.addWidget(label_time_mid, 0, 1)
        layout_listitem.addWidget(label_time_end, 0, 2)
        layout_listitem.addWidget(label_time_used, 0, 3)
        layout_listitem.addWidget(label_status, 0, 4)
        layout_listitem.addItem(spacer_right, 0, 5)

        layout_listitem.addWidget(label_text, 1, 0, 1, 6)
        # layout_listitem.addWidget(line_bottom, 2, 0, 1, 5)
        widget_listitem.setLayout(layout_listitem)

        item = QListWidgetItem()
        item.setSizeHint(QSize(0, 100))
        # item.setText("<h1>Hello</h1>")
        # item.setText(self.textEdit_2.toPlainText())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, widget_listitem)
        # self.listWidget.setResizeMode(QHeaderView.ResizeToContents)

        # self.data.data_modify(self.textEdit_2.toPlainText(), "2020/04/50", "2020/04/40","我爱你！", "已完成")
        # self.data.data_delete(int(self.textEdit_2.toPlainText()))
        # self.data.data_get_by_key(int(self.textEdit_2.toPlainText()))
        logging.warning("This is a log!")

    def clicked_new(self):
        self.data.insert(time.strftime("%Y-%m-%d", time.localtime()), time.strftime("%Y-%m-%d", time.localtime()),
                         self.textedit.toPlainText(), "处理中")
        self.textedit.setText("")

        print("Push new")

    def clicked_done(self):
        content = f"""
                     <font face="华文琥珀", size="1">2020/05/01 - 2020/05/01  【01天】 --进行中--</font><br/>
                     <font face="华文仿宋", size="4">我爱北京天安门！天安门上太阳升！</font>
                  """
        self.textedit.setText(content)
        pass

    def clicked_del(self):
        pass

    def clicked_block(self):
        pass

    def clicked_update(self):
        self.list_update()

    # 当数据改变时，更新LIST_WIDGET试图
    def list_update(self):
        df = self.data.get_all()

        listitem_widget = QWidget()
        listitem_textedit = QTextEdit(listitem_widget)
        listitem_layout = QGridLayout(listitem_widget)
        listitem_layout.addItem(listitem_textedit, 0, 0)

        content = f"""
                     <font face="华文琥珀", size="1">{} - {}  【{}天】 --{}--</font><br/>
                     <font face="华文仿宋", size="4">{}</font>
                  """


        print(df)

    # 单击时，选中LIST的条目，获取条目的索引用，用来做其他事情
    def list_single_clicked(self):
        pass

    # 双击时，打开修改界面，对条目进行修改
    def list_double_clicked(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    wm = TodoWindow()
    wm.show()

    sys.exit(app.exec_())
