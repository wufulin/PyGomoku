# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Mon Dec  9 18:04:14 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(335, 152)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 227, 175);"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 62, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 62, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 62, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditServer = QtGui.QLineEdit(Dialog)
        self.lineEditServer.setGeometry(QtCore.QRect(90, 20, 211, 22))
        self.lineEditServer.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEditServer.setObjectName(_fromUtf8("lineEditServer"))
        self.lineEditPort = QtGui.QLineEdit(Dialog)
        self.lineEditPort.setGeometry(QtCore.QRect(90, 50, 211, 22))
        self.lineEditPort.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEditPort.setObjectName(_fromUtf8("lineEditPort"))
        self.lineEditUsername = QtGui.QLineEdit(Dialog)
        self.lineEditUsername.setGeometry(QtCore.QRect(90, 80, 211, 22))
        self.lineEditUsername.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEditUsername.setObjectName(_fromUtf8("lineEditUsername"))
        self.btnLogin = QtGui.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(140, 110, 71, 32))
        self.btnLogin.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.btnExit = QtGui.QPushButton(Dialog)
        self.btnExit.setGeometry(QtCore.QRect(230, 110, 71, 32))
        self.btnExit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btnExit.setObjectName(_fromUtf8("btnExit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "服务器：", None))
        self.label_2.setText(_translate("Dialog", "端口：", None))
        self.label_3.setText(_translate("Dialog", "用户名：", None))
        self.lineEditServer.setText(_translate("Dialog", "127.0.0.1", None))
        self.lineEditPort.setText(_translate("Dialog", "21567", None))
        self.btnLogin.setText(_translate("Dialog", "登录", None))
        self.btnExit.setText(_translate("Dialog", "退出", None))

