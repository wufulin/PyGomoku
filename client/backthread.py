#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import Queue
import select
from common.config import BUFSIZE
from common.message import *
from PyQt4 import QtCore


class BackThread(QtCore.QThread):

    login_success_signal = QtCore.pyqtSignal(str)
    login_failed_signal = QtCore.pyqtSignal(str)

    def __init__(self, sock):
        super(BackThread, self).__init__()
        self.sock = sock
        self.sendqueue = Queue.Queue()
        self.inputs = []
        self.outputs = []

    def add_msg(self, message):
        self.sendqueue.put(message)

    def shutdown(self):
        self.sendqueue.empty()
        self.inputs = []
        self.outputs = []
        self.sock.close()

    def run(self):
        self.inputs = [self.sock]
        self.outputs = [self.sock]

        try:
            while True:

                read_sockets, write_sockets, error_sockets = select.select(self.inputs, self.outputs, [])

                for s in read_sockets:
                    # 接收服务端发来的消息
                    data = s.recv(BUFSIZE)
                    if data != "":
                        resp = json.loads(data, encoding='utf-8')
                        type = resp['type']
                        if type == SYSTEM_MESSAGE.VERIFIED_PASS:
                            self.login_success_signal.emit(resp['content'])
                        elif type == SYSTEM_MESSAGE.VERIFIED_FAIL:
                            self.login_failed_signal.emit(resp['content'])

                for s in write_sockets:
                    if self.sendqueue.qsize() > 0:
                        req = self.sendqueue.get()
                        s.send(req.dumps())

        except KeyboardInterrupt, e:
            raise e

