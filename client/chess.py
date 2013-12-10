# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chess.ui'
#
# Created: Tue Dec 10 11:20:44 2013
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

class Ui_chessDialog(object):
    def setupUi(self, chessDialog):
        chessDialog.setObjectName(_fromUtf8("chessDialog"))
        chessDialog.resize(904, 534)
        chessDialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 227, 175);"))
        self.leftFrame = QtGui.QFrame(chessDialog)
        self.leftFrame.setGeometry(QtCore.QRect(40, 40, 140, 140))
        self.leftFrame.setStyleSheet(_fromUtf8("background-image: url(:/background/avatar1.jpg);"))
        self.leftFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.leftFrame.setObjectName(_fromUtf8("leftFrame"))
        self.rightFrame = QtGui.QFrame(chessDialog)
        self.rightFrame.setGeometry(QtCore.QRect(730, 40, 140, 140))
        self.rightFrame.setStyleSheet(_fromUtf8("background-image: url(:/background/avatar2.jpg);"))
        self.rightFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.rightFrame.setObjectName(_fromUtf8("rightFrame"))
        self.lineEdit = QtGui.QLineEdit(chessDialog)
        self.lineEdit.setGeometry(QtCore.QRect(720, 485, 111, 22))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.btnSend = QtGui.QPushButton(chessDialog)
        self.btnSend.setGeometry(QtCore.QRect(835, 485, 51, 21))
        self.btnSend.setStyleSheet(_fromUtf8("background-color: rgb(224, 147, 62);"))
        self.btnSend.setObjectName(_fromUtf8("btnSend"))
        self.textBrowser = QtGui.QTextBrowser(chessDialog)
        self.textBrowser.setGeometry(QtCore.QRect(720, 290, 161, 181))
        self.textBrowser.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.splitter = QtGui.QSplitter(chessDialog)
        self.splitter.setGeometry(QtCore.QRect(30, 290, 161, 221))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.btnStart = QtGui.QPushButton(self.splitter)
        self.btnStart.setStyleSheet(_fromUtf8("background-color: rgb(224, 147, 62);"))
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.btnLose = QtGui.QPushButton(self.splitter)
        self.btnLose.setStyleSheet(_fromUtf8("background-color: rgb(224, 147, 62);"))
        self.btnLose.setObjectName(_fromUtf8("btnLose"))
        self.btnDrawn = QtGui.QPushButton(self.splitter)
        self.btnDrawn.setStyleSheet(_fromUtf8("background-color: rgb(224, 147, 62);"))
        self.btnDrawn.setObjectName(_fromUtf8("btnDrawn"))
        self.btnBackMove = QtGui.QPushButton(self.splitter)
        self.btnBackMove.setStyleSheet(_fromUtf8("background-color: rgb(224, 147, 62);"))
        self.btnBackMove.setObjectName(_fromUtf8("btnBackMove"))
        self.btnLeave = QtGui.QPushButton(self.splitter)
        self.btnLeave.setStyleSheet(_fromUtf8("background-color: rgb(224, 147, 62);"))
        self.btnLeave.setObjectName(_fromUtf8("btnLeave"))
        self.lblYou = QtGui.QLabel(chessDialog)
        self.lblYou.setGeometry(QtCore.QRect(80, 200, 62, 16))
        self.lblYou.setAlignment(QtCore.Qt.AlignCenter)
        self.lblYou.setObjectName(_fromUtf8("lblYou"))
        self.lblOpponent = QtGui.QLabel(chessDialog)
        self.lblOpponent.setGeometry(QtCore.QRect(770, 200, 71, 16))
        self.lblOpponent.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOpponent.setObjectName(_fromUtf8("lblOpponent"))
        self.widget1 = QtGui.QWidget(chessDialog)
        self.widget1.setGeometry(QtCore.QRect(100, 220, 29, 29))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.widget2 = QtGui.QWidget(chessDialog)
        self.widget2.setGeometry(QtCore.QRect(790, 220, 29, 29))
        self.widget2.setObjectName(_fromUtf8("widget2"))

        self.retranslateUi(chessDialog)
        QtCore.QMetaObject.connectSlotsByName(chessDialog)

    def retranslateUi(self, chessDialog):
        chessDialog.setWindowTitle(_translate("chessDialog", "Dialog", None))
        self.btnSend.setText(_translate("chessDialog", "发送", None))
        self.btnStart.setText(_translate("chessDialog", "开始", None))
        self.btnLose.setText(_translate("chessDialog", "认输", None))
        self.btnDrawn.setText(_translate("chessDialog", "和棋", None))
        self.btnBackMove.setText(_translate("chessDialog", "悔棋", None))
        self.btnLeave.setText(_translate("chessDialog", "离开", None))
        self.lblYou.setText(_translate("chessDialog", "You", None))
        self.lblOpponent.setText(_translate("chessDialog", "Opponent", None))

import assets_rc
