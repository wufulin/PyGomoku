# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Thu Dec  5 11:07:50 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 595)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 252, 241);"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.infoWidget = QtGui.QTabWidget(self.centralwidget)
        self.infoWidget.setGeometry(QtCore.QRect(20, 80, 171, 461))
        self.infoWidget.setObjectName(_fromUtf8("infoWidget"))
        self.tabMessages = QtGui.QWidget()
        self.tabMessages.setObjectName(_fromUtf8("tabMessages"))
        self.tableView = QtGui.QTableView(self.tabMessages)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 164, 441))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.infoWidget.addTab(self.tabMessages, _fromUtf8(""))
        self.tabScores = QtGui.QWidget()
        self.tabScores.setObjectName(_fromUtf8("tabScores"))
        self.tableView_2 = QtGui.QTableView(self.tabScores)
        self.tableView_2.setGeometry(QtCore.QRect(0, 0, 164, 441))
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.infoWidget.addTab(self.tabScores, _fromUtf8(""))
        self.hallWidget = QtGui.QTabWidget(self.centralwidget)
        self.hallWidget.setGeometry(QtCore.QRect(220, 80, 551, 411))
        self.hallWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.hallWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hallWidget.setAutoFillBackground(False)
        self.hallWidget.setStyleSheet(_fromUtf8("border-color: rgb(225, 121, 25);\n"
"background-color: rgb(255, 255, 248);"))
        self.hallWidget.setTabPosition(QtGui.QTabWidget.North)
        self.hallWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.hallWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.hallWidget.setObjectName(_fromUtf8("hallWidget"))
        self.tabHall1 = QtGui.QWidget()
        self.tabHall1.setEnabled(True)
        self.tabHall1.setStyleSheet(_fromUtf8("background-color: rgb(255, 229, 202);"))
        self.tabHall1.setObjectName(_fromUtf8("tabHall1"))
        self.groupBox1 = QtGui.QGroupBox(self.tabHall1)
        self.groupBox1.setGeometry(QtCore.QRect(40, 10, 191, 141))
        self.groupBox1.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox1.setFlat(False)
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.pushButton = QtGui.QPushButton(self.groupBox1)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 50, 50))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox1)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 40, 50, 50))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.widget = QtGui.QWidget(self.groupBox1)
        self.widget.setGeometry(QtCore.QRect(70, 40, 55, 55))
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(159, 238, 255);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.groupBox1)
        self.label.setGeometry(QtCore.QRect(20, 100, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox1)
        self.label_2.setGeometry(QtCore.QRect(140, 100, 41, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox1_2 = QtGui.QGroupBox(self.tabHall1)
        self.groupBox1_2.setGeometry(QtCore.QRect(310, 10, 191, 141))
        self.groupBox1_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox1_2.setFlat(False)
        self.groupBox1_2.setObjectName(_fromUtf8("groupBox1_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox1_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 40, 50, 50))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox1_2)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 40, 50, 50))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.widget_2 = QtGui.QWidget(self.groupBox1_2)
        self.widget_2.setGeometry(QtCore.QRect(70, 40, 55, 55))
        self.widget_2.setStyleSheet(_fromUtf8("background-color: rgb(159, 238, 255);"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_3 = QtGui.QLabel(self.groupBox1_2)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 41, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox1_2)
        self.label_4.setGeometry(QtCore.QRect(140, 100, 41, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox1_3 = QtGui.QGroupBox(self.tabHall1)
        self.groupBox1_3.setGeometry(QtCore.QRect(40, 200, 191, 141))
        self.groupBox1_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox1_3.setFlat(False)
        self.groupBox1_3.setObjectName(_fromUtf8("groupBox1_3"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox1_3)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 40, 50, 50))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox1_3)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 40, 50, 50))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.widget_3 = QtGui.QWidget(self.groupBox1_3)
        self.widget_3.setGeometry(QtCore.QRect(70, 40, 55, 55))
        self.widget_3.setStyleSheet(_fromUtf8("background-color: rgb(159, 238, 255);"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.label_5 = QtGui.QLabel(self.groupBox1_3)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 41, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox1_3)
        self.label_6.setGeometry(QtCore.QRect(140, 100, 41, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.groupBox1_4 = QtGui.QGroupBox(self.tabHall1)
        self.groupBox1_4.setGeometry(QtCore.QRect(310, 200, 191, 141))
        self.groupBox1_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox1_4.setFlat(False)
        self.groupBox1_4.setObjectName(_fromUtf8("groupBox1_4"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox1_4)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 40, 50, 50))
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox1_4)
        self.pushButton_8.setGeometry(QtCore.QRect(130, 40, 50, 50))
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.widget_4 = QtGui.QWidget(self.groupBox1_4)
        self.widget_4.setGeometry(QtCore.QRect(70, 40, 55, 55))
        self.widget_4.setStyleSheet(_fromUtf8("background-color: rgb(159, 238, 255);"))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.label_7 = QtGui.QLabel(self.groupBox1_4)
        self.label_7.setGeometry(QtCore.QRect(20, 100, 41, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox1_4)
        self.label_8.setGeometry(QtCore.QRect(140, 100, 41, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.hallWidget.addTab(self.tabHall1, _fromUtf8(""))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 510, 471, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.btnSend = QtGui.QPushButton(self.centralwidget)
        self.btnSend.setGeometry(QtCore.QRect(700, 510, 71, 32))
        self.btnSend.setObjectName(_fromUtf8("btnSend"))
        self.logoWidget = QtGui.QWidget(self.centralwidget)
        self.logoWidget.setGeometry(QtCore.QRect(20, 20, 191, 51))
        self.logoWidget.setStyleSheet(_fromUtf8("background-color: rgb(207, 255, 214);"))
        self.logoWidget.setObjectName(_fromUtf8("logoWidget"))
        self.logoWidget_2 = QtGui.QWidget(self.centralwidget)
        self.logoWidget_2.setGeometry(QtCore.QRect(630, 28, 51, 51))
        self.logoWidget_2.setStyleSheet(_fromUtf8("background-color: rgb(207, 255, 214);"))
        self.logoWidget_2.setObjectName(_fromUtf8("logoWidget_2"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(700, 30, 62, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(700, 60, 62, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.infoWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.infoWidget.setTabText(self.infoWidget.indexOf(self.tabMessages), _translate("MainWindow", "信息", None))
        self.infoWidget.setTabText(self.infoWidget.indexOf(self.tabScores), _translate("MainWindow", "排行榜", None))
        self.groupBox1.setTitle(_translate("MainWindow", "桌子1", None))
        self.label.setText(_translate("MainWindow", "user1", None))
        self.label_2.setText(_translate("MainWindow", "user2", None))
        self.groupBox1_2.setTitle(_translate("MainWindow", "桌子2", None))
        self.label_3.setText(_translate("MainWindow", "user1", None))
        self.label_4.setText(_translate("MainWindow", "user2", None))
        self.groupBox1_3.setTitle(_translate("MainWindow", "桌子3", None))
        self.label_5.setText(_translate("MainWindow", "user1", None))
        self.label_6.setText(_translate("MainWindow", "user2", None))
        self.groupBox1_4.setTitle(_translate("MainWindow", "桌子4", None))
        self.label_7.setText(_translate("MainWindow", "user1", None))
        self.label_8.setText(_translate("MainWindow", "user2", None))
        self.hallWidget.setTabText(self.hallWidget.indexOf(self.tabHall1), _translate("MainWindow", "大厅1", None))
        self.btnSend.setText(_translate("MainWindow", "发送", None))
        self.label_9.setText(_translate("MainWindow", "Frank", None))
        self.label_10.setText(_translate("MainWindow", "积分：10", None))

