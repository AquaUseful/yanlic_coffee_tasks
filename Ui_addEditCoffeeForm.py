# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/catsatan/Документы/yandex/yandex_repos/coffee_tasks/addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 120)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.spinBox_pack_size = QtWidgets.QSpinBox(Form)
        self.spinBox_pack_size.setMinimum(1)
        self.spinBox_pack_size.setMaximum(1000000)
        self.spinBox_pack_size.setObjectName("spinBox_pack_size")
        self.gridLayout.addWidget(self.spinBox_pack_size, 2, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.spinBox_price = QtWidgets.QSpinBox(Form)
        self.spinBox_price.setMinimum(1)
        self.spinBox_price.setMaximum(1000000)
        self.spinBox_price.setObjectName("spinBox_price")
        self.gridLayout.addWidget(self.spinBox_price, 2, 4, 1, 1)
        self.lineEdit_taste = QtWidgets.QLineEdit(Form)
        self.lineEdit_taste.setObjectName("lineEdit_taste")
        self.gridLayout.addWidget(self.lineEdit_taste, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_type = QtWidgets.QComboBox(Form)
        self.comboBox_type.setObjectName("comboBox_type")
        self.gridLayout.addWidget(self.comboBox_type, 2, 2, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.lineEdit_id = QtWidgets.QLineEdit(Form)
        self.lineEdit_id.setEnabled(True)
        self.lineEdit_id.setText("")
        self.lineEdit_id.setReadOnly(True)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.gridLayout.addWidget(self.lineEdit_id, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtWidgets.QPushButton(Form)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add or edit coffee"))
        self.label_3.setText(_translate("Form", "type"))
        self.label_5.setText(_translate("Form", "price"))
        self.label_2.setText(_translate("Form", "name"))
        self.label.setText(_translate("Form", "id"))
        self.label_6.setText(_translate("Form", "pack_size"))
        self.label_4.setText(_translate("Form", "taste"))
        self.pushButton_save.setText(_translate("Form", "Сохранить"))
        self.pushButton_cancel.setText(_translate("Form", "Отменить"))
