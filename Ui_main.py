# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/catsatan/Документы/yandex/yandex_repos/coffee_tasks/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButton_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.horizontalLayout.addWidget(self.pushButton_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setObjectName("pushButton_update")
        self.verticalLayout.addWidget(self.pushButton_update)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menu.addAction(self.action_exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Эсперссо"))
        self.pushButton_add.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_edit.setText(_translate("MainWindow", "Редактировать выбранное"))
        self.pushButton_update.setText(_translate("MainWindow", "Обновить"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action_exit.setText(_translate("MainWindow", "Выход"))
