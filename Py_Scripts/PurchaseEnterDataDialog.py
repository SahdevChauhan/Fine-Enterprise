# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PurchaseEnterDataDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PurchaseEnterDataDialog(object):
    def setupUi(self, PurchaseEnterDataDialog):
        PurchaseEnterDataDialog.setObjectName("PurchaseEnterDataDialog")
        PurchaseEnterDataDialog.resize(506, 436)
        self.gridLayout = QtWidgets.QGridLayout(PurchaseEnterDataDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_cancel = QtWidgets.QPushButton(PurchaseEnterDataDialog)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 14, 2, 1, 1)
        self.line_edit_cheque_no = QtWidgets.QLineEdit(PurchaseEnterDataDialog)
        self.line_edit_cheque_no.setObjectName("line_edit_cheque_no")
        self.gridLayout.addWidget(self.line_edit_cheque_no, 9, 1, 1, 1)
        self.lbl_bill_no = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.lbl_bill_no.setObjectName("lbl_bill_no")
        self.gridLayout.addWidget(self.lbl_bill_no, 10, 0, 1, 1)
        self.lbl_payment_paid_date = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.lbl_payment_paid_date.setObjectName("lbl_payment_paid_date")
        self.gridLayout.addWidget(self.lbl_payment_paid_date, 7, 0, 1, 1)
        self.btn_add_record = QtWidgets.QPushButton(PurchaseEnterDataDialog)
        self.btn_add_record.setObjectName("btn_add_record")
        self.gridLayout.addWidget(self.btn_add_record, 13, 2, 1, 1)
        self.line_edit_qty = QtWidgets.QLineEdit(PurchaseEnterDataDialog)
        self.line_edit_qty.setMaximumSize(QtCore.QSize(341, 16777215))
        self.line_edit_qty.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_edit_qty.setObjectName("line_edit_qty")
        self.gridLayout.addWidget(self.line_edit_qty, 4, 1, 1, 1)
        self.line_edit_chalan_no = QtWidgets.QLineEdit(PurchaseEnterDataDialog)
        self.line_edit_chalan_no.setObjectName("line_edit_chalan_no")
        self.gridLayout.addWidget(self.line_edit_chalan_no, 10, 1, 1, 1)
        self.lbl_remarks = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.lbl_remarks.setObjectName("lbl_remarks")
        self.gridLayout.addWidget(self.lbl_remarks, 11, 0, 1, 1)
        self.llbl_selling_quantity = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.llbl_selling_quantity.setObjectName("llbl_selling_quantity")
        self.gridLayout.addWidget(self.llbl_selling_quantity, 4, 0, 1, 1)
        self.lbl_size = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.lbl_size.setObjectName("lbl_size")
        self.gridLayout.addWidget(self.lbl_size, 3, 0, 1, 1)
        self.line_edit_selling_rate = QtWidgets.QLineEdit(PurchaseEnterDataDialog)
        self.line_edit_selling_rate.setMaxLength(32700)
        self.line_edit_selling_rate.setObjectName("line_edit_selling_rate")
        self.gridLayout.addWidget(self.line_edit_selling_rate, 5, 1, 1, 1)
        self.combo_box_size = QtWidgets.QComboBox(PurchaseEnterDataDialog)
        self.combo_box_size.setMinimumSize(QtCore.QSize(69, 0))
        self.combo_box_size.setMaximumSize(QtCore.QSize(69, 16777215))
        self.combo_box_size.setObjectName("combo_box_size")
        self.combo_box_size.addItem("")
        self.combo_box_size.addItem("")
        self.combo_box_size.addItem("")
        self.combo_box_size.addItem("")
        self.combo_box_size.addItem("")
        self.combo_box_size.addItem("")
        self.combo_box_size.addItem("")
        self.gridLayout.addWidget(self.combo_box_size, 3, 1, 1, 1)
        self.lbl_purchase_rate_of_44_size = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.lbl_purchase_rate_of_44_size.setObjectName("lbl_purchase_rate_of_44_size")
        self.gridLayout.addWidget(self.lbl_purchase_rate_of_44_size, 6, 0, 1, 1)
        self.lbl_cheque_no = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.lbl_cheque_no.setObjectName("lbl_cheque_no")
        self.gridLayout.addWidget(self.lbl_cheque_no, 9, 0, 1, 1)
        self.date_edit_payment_paid_date = QtWidgets.QDateEdit(PurchaseEnterDataDialog)
        self.date_edit_payment_paid_date.setCalendarPopup(True)
        self.date_edit_payment_paid_date.setObjectName("date_edit_payment_paid_date")
        self.gridLayout.addWidget(self.date_edit_payment_paid_date, 7, 1, 1, 1)
        self.line_edit_purchase_rate_of_44_size = QtWidgets.QLineEdit(PurchaseEnterDataDialog)
        self.line_edit_purchase_rate_of_44_size.setObjectName("line_edit_purchase_rate_of_44_size")
        self.gridLayout.addWidget(self.line_edit_purchase_rate_of_44_size, 6, 1, 1, 1)
        self.lbl_purchase_rate = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.lbl_purchase_rate.setObjectName("lbl_purchase_rate")
        self.gridLayout.addWidget(self.lbl_purchase_rate, 5, 0, 1, 1)
        self.lbl_payment_paid_amount = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.lbl_payment_paid_amount.setObjectName("lbl_payment_paid_amount")
        self.gridLayout.addWidget(self.lbl_payment_paid_amount, 8, 0, 1, 1)
        self.line_edit_payment_paid_amount = QtWidgets.QLineEdit(PurchaseEnterDataDialog)
        self.line_edit_payment_paid_amount.setObjectName("line_edit_payment_paid_amount")
        self.gridLayout.addWidget(self.line_edit_payment_paid_amount, 8, 1, 1, 1)
        self.line_edit_party_name = QtWidgets.QLineEdit(PurchaseEnterDataDialog)
        self.line_edit_party_name.setObjectName("line_edit_party_name")
        self.gridLayout.addWidget(self.line_edit_party_name, 1, 1, 1, 1)
        self.lbl_gsm = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.lbl_gsm.setObjectName("lbl_gsm")
        self.gridLayout.addWidget(self.lbl_gsm, 2, 0, 1, 1)
        self.combo_box_gsm = QtWidgets.QComboBox(PurchaseEnterDataDialog)
        self.combo_box_gsm.setMinimumSize(QtCore.QSize(69, 22))
        self.combo_box_gsm.setMaximumSize(QtCore.QSize(69, 16777215))
        self.combo_box_gsm.setObjectName("combo_box_gsm")
        self.combo_box_gsm.addItem("")
        self.combo_box_gsm.addItem("")
        self.gridLayout.addWidget(self.combo_box_gsm, 2, 1, 1, 1)
        self.lbl_date = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.lbl_date.setObjectName("lbl_date")
        self.gridLayout.addWidget(self.lbl_date, 0, 0, 1, 1)
        self.date_edit_date = QtWidgets.QDateEdit(PurchaseEnterDataDialog)
        self.date_edit_date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.date_edit_date.setCalendarPopup(True)
        self.date_edit_date.setObjectName("date_edit_date")
        self.gridLayout.addWidget(self.date_edit_date, 0, 1, 1, 1)
        self.lbl_party_name = QtWidgets.QLabel(PurchaseEnterDataDialog)
        self.lbl_party_name.setObjectName("lbl_party_name")
        self.gridLayout.addWidget(self.lbl_party_name, 1, 0, 1, 1)
        self.text_edit_remarks = QtWidgets.QTextEdit(PurchaseEnterDataDialog)
        self.text_edit_remarks.setObjectName("text_edit_remarks")
        self.gridLayout.addWidget(self.text_edit_remarks, 11, 1, 1, 1)
        self.lbl_bill_no.setBuddy(self.line_edit_chalan_no)
        self.lbl_payment_paid_date.setBuddy(self.date_edit_payment_paid_date)
        self.lbl_remarks.setBuddy(self.text_edit_remarks)
        self.llbl_selling_quantity.setBuddy(self.line_edit_qty)
        self.lbl_size.setBuddy(self.combo_box_size)
        self.lbl_purchase_rate_of_44_size.setBuddy(self.line_edit_purchase_rate_of_44_size)
        self.lbl_cheque_no.setBuddy(self.line_edit_cheque_no)
        self.lbl_purchase_rate.setBuddy(self.line_edit_selling_rate)
        self.lbl_payment_paid_amount.setBuddy(self.line_edit_payment_paid_amount)
        self.lbl_gsm.setBuddy(self.combo_box_gsm)
        self.lbl_date.setBuddy(self.date_edit_date)
        self.lbl_party_name.setBuddy(self.line_edit_party_name)

        self.retranslateUi(PurchaseEnterDataDialog)
        QtCore.QMetaObject.connectSlotsByName(PurchaseEnterDataDialog)
        PurchaseEnterDataDialog.setTabOrder(self.date_edit_date, self.line_edit_party_name)
        PurchaseEnterDataDialog.setTabOrder(self.line_edit_party_name, self.combo_box_gsm)
        PurchaseEnterDataDialog.setTabOrder(self.combo_box_gsm, self.combo_box_size)
        PurchaseEnterDataDialog.setTabOrder(self.combo_box_size, self.line_edit_qty)
        PurchaseEnterDataDialog.setTabOrder(self.line_edit_qty, self.line_edit_selling_rate)
        PurchaseEnterDataDialog.setTabOrder(self.line_edit_selling_rate, self.line_edit_purchase_rate_of_44_size)
        PurchaseEnterDataDialog.setTabOrder(self.line_edit_purchase_rate_of_44_size, self.date_edit_payment_paid_date)
        PurchaseEnterDataDialog.setTabOrder(self.date_edit_payment_paid_date, self.line_edit_payment_paid_amount)
        PurchaseEnterDataDialog.setTabOrder(self.line_edit_payment_paid_amount, self.line_edit_cheque_no)
        PurchaseEnterDataDialog.setTabOrder(self.line_edit_cheque_no, self.line_edit_chalan_no)
        PurchaseEnterDataDialog.setTabOrder(self.line_edit_chalan_no, self.text_edit_remarks)
        PurchaseEnterDataDialog.setTabOrder(self.text_edit_remarks, self.btn_add_record)
        PurchaseEnterDataDialog.setTabOrder(self.btn_add_record, self.btn_cancel)

    def retranslateUi(self, PurchaseEnterDataDialog):
        _translate = QtCore.QCoreApplication.translate
        PurchaseEnterDataDialog.setWindowTitle(_translate("PurchaseEnterDataDialog", "Enter Data"))
        self.btn_cancel.setText(_translate("PurchaseEnterDataDialog", "Cancel"))
        self.lbl_bill_no.setText(_translate("PurchaseEnterDataDialog", "Bill No.:"))
        self.lbl_payment_paid_date.setText(_translate("PurchaseEnterDataDialog", "Payment paid date:"))
        self.btn_add_record.setText(_translate("PurchaseEnterDataDialog", "Add Record"))
        self.lbl_remarks.setText(_translate("PurchaseEnterDataDialog", "Remarks:"))
        self.llbl_selling_quantity.setText(_translate("PurchaseEnterDataDialog", "Quantity:"))
        self.lbl_size.setText(_translate("PurchaseEnterDataDialog", "Size:"))
        self.combo_box_size.setItemText(0, _translate("PurchaseEnterDataDialog", "36"))
        self.combo_box_size.setItemText(1, _translate("PurchaseEnterDataDialog", "44"))
        self.combo_box_size.setItemText(2, _translate("PurchaseEnterDataDialog", "48"))
        self.combo_box_size.setItemText(3, _translate("PurchaseEnterDataDialog", "54"))
        self.combo_box_size.setItemText(4, _translate("PurchaseEnterDataDialog", "58"))
        self.combo_box_size.setItemText(5, _translate("PurchaseEnterDataDialog", "60"))
        self.combo_box_size.setItemText(6, _translate("PurchaseEnterDataDialog", "63"))
        self.lbl_purchase_rate_of_44_size.setText(_translate("PurchaseEnterDataDialog", "Purchase rate of 44 size:"))
        self.lbl_cheque_no.setText(_translate("PurchaseEnterDataDialog", "Cheque No.:"))
        self.date_edit_payment_paid_date.setDisplayFormat(_translate("PurchaseEnterDataDialog", "dd/MM/yyyy"))
        self.lbl_purchase_rate.setText(_translate("PurchaseEnterDataDialog", "Purchase Rate:"))
        self.lbl_payment_paid_amount.setText(_translate("PurchaseEnterDataDialog", "Payment paid amount:"))
        self.lbl_gsm.setText(_translate("PurchaseEnterDataDialog", "GSM:"))
        self.combo_box_gsm.setItemText(0, _translate("PurchaseEnterDataDialog", "70"))
        self.combo_box_gsm.setItemText(1, _translate("PurchaseEnterDataDialog", "100"))
        self.lbl_date.setText(_translate("PurchaseEnterDataDialog", "Date:"))
        self.date_edit_date.setDisplayFormat(_translate("PurchaseEnterDataDialog", "dd/MM/yyyy"))
        self.lbl_party_name.setText(_translate("PurchaseEnterDataDialog", "Party Name:"))

