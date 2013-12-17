#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

__author__ = 'wufulin'

import mainUI

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from common.tools import get_logger, now
from client.service.userservice import UserService

class GomokuMain(QtGui.QMainWindow, mainUI.Ui_MainWindow):

    def __init__(self, sock, thread, user, parent=None):
        self.logger = get_logger('GomokuMain')
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.thread = thread
        self.sock = sock
        self.user = user
        self.refresh_user(user)
        self._init_signal()

    def _init_signal(self):
        self.connect(self.thread, SIGNAL('logout_signal(QString)'), self.logout)

    def logout(self, msg):
        username = json.loads(str(msg))['username']
        self.messageBrowser.append(u"%s - %s 退出大厅\n" % (now(), username))

    def refresh_user(self, user):
        self.lblUsername.setText(user.username)
        self.lblScore.setText(u"积分: {0}".format(user.score))

    def closeEvent(self, event):
        service = UserService(self.thread)
        service.logoutByUser(self.user.username)
        # self.thread.shutdown()
        self.close()
