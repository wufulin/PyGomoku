#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import mainUI
from PyQt4 import QtGui
from common.tools import get_logger

class GomokuMain(QtGui.QMainWindow, mainUI.Ui_MainWindow):

    def __init__(self, sock, user, parent=None):
        self.logger = get_logger('GomokuMain')
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user = user
        self.lblUsername.setText(user.username)