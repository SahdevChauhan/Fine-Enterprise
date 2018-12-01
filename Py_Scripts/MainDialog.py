# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(403, 329)
        self.gridLayout = QtWidgets.QGridLayout(MainDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_fine_enterprise = QtWidgets.QLabel(MainDialog)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_fine_enterprise.setFont(font)
        self.lbl_fine_enterprise.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_fine_enterprise.setObjectName("lbl_fine_enterprise")
        self.gridLayout.addWidget(self.lbl_fine_enterprise, 0, 0, 1, 3)
        self.btn_view_graph = QtWidgets.QPushButton(MainDialog)
        self.btn_view_graph.setEnabled(True)
        self.btn_view_graph.setObjectName("btn_view_graph")
        self.gridLayout.addWidget(self.btn_view_graph, 4, 2, 1, 1)
        self.btn_enter_data = QtWidgets.QPushButton(MainDialog)
        self.btn_enter_data.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btn_enter_data.setFont(font)
        self.btn_enter_data.setCheckable(True)
        self.btn_enter_data.setChecked(False)
        self.btn_enter_data.setObjectName("btn_enter_data")
        self.gridLayout.addWidget(self.btn_enter_data, 1, 2, 1, 1)
        self.btn_delete_data = QtWidgets.QPushButton(MainDialog)
        self.btn_delete_data.setEnabled(True)
        self.btn_delete_data.setObjectName("btn_delete_data")
        self.gridLayout.addWidget(self.btn_delete_data, 3, 2, 1, 1)
        self.btn_view_data = QtWidgets.QPushButton(MainDialog)
        self.btn_view_data.setEnabled(True)
        self.btn_view_data.setObjectName("btn_view_data")
        self.gridLayout.addWidget(self.btn_view_data, 2, 2, 1, 1)
        self.radio_btn_selling = QtWidgets.QRadioButton(MainDialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.radio_btn_selling.setFont(font)
        self.radio_btn_selling.setObjectName("radio_btn_selling")
        self.gridLayout.addWidget(self.radio_btn_selling, 1, 1, 1, 1)
        self.radio_btn_purchase = QtWidgets.QRadioButton(MainDialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.radio_btn_purchase.setFont(font)
        self.radio_btn_purchase.setObjectName("radio_btn_purchase")
        self.gridLayout.addWidget(self.radio_btn_purchase, 2, 1, 1, 1)
        self.lbl_category = QtWidgets.QLabel(MainDialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_category.setFont(font)
        self.lbl_category.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_category.setObjectName("lbl_category")
        self.gridLayout.addWidget(self.lbl_category, 1, 0, 1, 1)
        self.btn_stock = QtWidgets.QPushButton(MainDialog)
        self.btn_stock.setObjectName("btn_stock")
        self.gridLayout.addWidget(self.btn_stock, 3, 1, 1, 1)

        self.retranslateUi(MainDialog)
        self.radio_btn_selling.clicked.connect(self.btn_enter_data.show)
        self.radio_btn_selling.clicked.connect(self.btn_view_data.show)
        self.radio_btn_selling.clicked.connect(self.btn_delete_data.show)
        self.radio_btn_selling.clicked.connect(self.btn_view_graph.show)
        self.radio_btn_purchase.clicked.connect(self.btn_enter_data.show)
        self.radio_btn_purchase.clicked.connect(self.btn_view_data.show)
        self.radio_btn_purchase.clicked.connect(self.btn_delete_data.show)
        self.radio_btn_purchase.clicked.connect(self.btn_view_graph.show)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "Fine Enterprise"))
        self.lbl_fine_enterprise.setText(_translate("MainDialog", "Fine Enterprise"))
        self.btn_view_graph.setText(_translate("MainDialog", "View Graph"))
        self.btn_enter_data.setText(_translate("MainDialog", "Enter Data"))
        self.btn_delete_data.setText(_translate("MainDialog", "Delete Data"))
        self.btn_view_data.setText(_translate("MainDialog", "View Data"))
        self.radio_btn_selling.setText(_translate("MainDialog", "Selling"))
        self.radio_btn_purchase.setText(_translate("MainDialog", "Purchase"))
        self.lbl_category.setText(_translate("MainDialog", "Category:"))
        self.btn_stock.setText(_translate("MainDialog", "View Stock"))
