#!/usr/bin/python
# -*- coding: utf-8 -*-
from entity.user import User

__author__ = 'wufulin'

import loginUI
from socket import *
from PyQt4.QtCore import SIGNAL
from PyQt4 import QtGui
from common.tools import get_logger
from service.userservice import UserService
import backthread
from main import GomokuMain


class GomokuLogin(QtGui.QWidget, loginUI.Ui_Dialog):

    def __init__(self, parent=None):
        self.logger = get_logger('GomokuLogin')
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.btnLogin, SIGNAL('clicked()'), self.login)
        self.connect(self.btnExit, SIGNAL('clicked()'), self.exit)

    def login(self):
        ip = str(self.lineEditServer.text()).strip()
        port = int(self.lineEditPort.text())
        username = str(self.lineEditUsername.text()).strip().decode('utf-8')
        password = str(self.lineEditPassword.text()).strip().decode('utf-8')

        self.sock = socket(AF_INET, SOCK_STREAM)
        try:
            self.sock.connect((ip, port))
            self.logger.debug('connect to remote server successfully!')
            self.thread = backthread.BackThread(self.sock)
            self.thread.start()
            self.connect(self.thread, SIGNAL('login_success_signal(QString)'), self.login_success)
            self.connect(self.thread, SIGNAL('login_failed_signal(QString)'), self.login_failed)
            service = UserService(self.thread)
            service.verifyUser(username, password)
        except Exception, e:
            self.logger.error(str(e))
            QtGui.QMessageBox.information(self, "错误", "unable to connect server because {0}".format(str(e)))

    def login_success(self, msg):
        """
        登录成功回调函数
        """
        self.close()
        self.logger.debug(msg)
        user = User.loads(str(msg))
        self.hall = GomokuMain(self.sock, user)
        self.hall.show()

    def login_failed(self, error):
        """
        登录失败回调函数
        """
        self.logger.debug("login error --> {0}".format(str(error)))
        QtGui.QMessageBox.information(self, "错误", "%s" % str(error))
        self.thread.shutdown()

    def exit(self):
        self.logger.debug("close client now")
        self.thread.shutdown()
        self.close()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Gomoku")
    loginForm = GomokuLogin()
    loginForm.show()
    sys.exit(app.exec_())