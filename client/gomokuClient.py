#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import select
from socket import *
import math
import sys

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *

import chess
import login
import game
from util.config import *
from util.message import *
from util.tools import *

class GomokuLogin(QtGui.QWidget, login.Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.btnLogin, SIGNAL('clicked()'), self.login)
        self.connect(self.btnExit, SIGNAL('clicked()'), self.exit)

    def login(self):
        ip = str(self.lineEditServer.text()).strip()
        port = int(self.lineEditPort.text())
        username = str(self.lineEditUsername.text()).strip()

        self.client = GomokuClient((ip, port), username, self.call_login_success, self.call_login_failed)
        self.client.startup()

    def call_login_success(self, msg):
        """
        登录成功回调函数
        """
        self.close()
        self.client.show()
        if DEBUG:
            print(msg)

    def call_login_failed(self, addr):
        """
        登录失败回调函数
        """
        QtGui.QMessageBox.information(self, "错误", "Unable to connect to [%s:%s]" % addr)

    def exit(self):
        self.close()

class GomokuClient(QtGui.QWidget, chess.Ui_chessDialog):
    def __init__(self, addr, username, login_success_caller=None, login_failed_caller=None):
        QtGui.QWidget.__init__(self, None)
        self.login_success_caller = login_success_caller
        self.login_failed_caller = login_failed_caller
        self.addr = addr
        self.username = username
        self.chesstype = 0

    def __init_config(self, sock):
        self.client_sock = sock

        # 后台接收消息线程
        self.backthread = BackendThread(self.client_sock)
        self.backthread.start()

        self.chessboard = ChessBoard(self, self.client_sock, self.backthread)

    def __init_ui(self):
        self.setupUi(self)

        self.connect(self.btnSend, SIGNAL('clicked()'), self.sendChatMessage)
        self.connect(self.btnStart, SIGNAL('clicked()'), self.startChess)
        self.connect(self.btnBackMove, SIGNAL('clicked()'), self.backMoveChess)
        self.connect(self.btnLeave, SIGNAL('clicked()'), self.leaveChess)
        self.connect(self.btnDrawn, SIGNAL('clicked()'), self.drawnChess)
        self.connect(self.btnLose, SIGNAL('clicked()'), self.loseChess)

        self.connect(self.backthread, SIGNAL('chatReceived()'), self.receiveChatMessage)
        self.connect(self.backthread, SIGNAL('systemReceived()'), self.systemMessage)

    def startup(self):
        sock = socket(AF_INET, SOCK_STREAM)
        try:
            sock.connect(self.addr)
            self.__init_config(sock)
            self.__init_ui()
            self.login_success_caller('Connected to remote host. Start sending messages')
        except Exception, e:
            self.login_failed_caller(self.addr)
            print(str(e))

    def startChess(self):
        """
        开始对弈，随机选取棋子
        """
        self.btnStart.setEnabled(False)
        message = ChessMessage(CHESS_MESSAGE.START)
        self.client_sock.send(message.dumps())

    def drawnChess(self):
        pass

    def loseChess(self):
        pass

    def backMoveChess(self):
        pass

    def leaveChess(self):
        pass

    def sendChatMessage(self):
        # 得到用户输入的消息、输入时间
        chatMsg = str(self.lineEdit.text()).decode('utf-8')
        name = "test"
        message = ChatMessage(name, now(), chatMsg)
        self.textBrowser.append(message.get_content())
        self.client_sock.send(message.dumps())
        self.lineEdit.clear()

    def receiveChatMessage(self):
        # 接收服务器的聊天消息
        self.textBrowser.append(self.backthread.message)

    def systemMessage(self):
        message = self.backthread.message
        if message.get_content() == 1:
            self.chesstype = 1
            self.widget1.setStyleSheet("background-image: url(:/background/white.png) no-repeat;")
            self.widget2.setStyleSheet("background-image: url(:/background/black.png) no-repeat;")
            self.leftFrame.setStyleSheet("background-image: url(:/background/avatar1.jpg);")
            self.rightFrame.setStyleSheet("background-image: url(:/background/avatar2.jpg);")
        elif message.get_content() == 2:
            self.chesstype = 2
            self.widget1.setStyleSheet("background-image: url(:/background/black.png) no-repeat;")
            self.widget2.setStyleSheet("background-image: url(:/background/white.png) no-repeat;")
            self.leftFrame.setStyleSheet("background-image: url(:/background/avatar2.jpg);")
            self.rightFrame.setStyleSheet("background-image: url(:/background/avatar1.jpg);")

    def closeEvent(self, QCloseEvent):

        self.client_sock.send()

class BackendThread(QtCore.QThread):
    chessPressed = QtCore.pyqtSignal()
    chatReceived = QtCore.pyqtSignal()
    systemReceived = QtCore.pyqtSignal()
    def __init__(self, sock):
        super(BackendThread, self).__init__()
        self.sock = sock
        self.message = None

    def run(self):
        while True:
            self.socket_list = [self.sock]

            read_sockets, write_sockets, error_sockets = select.select(self.socket_list, [], [])

            for sock in read_sockets:
                # 接收服务端发来的消息
                msg = sock.recv(BUFSIZE)
                if msg != "":
                    message = BaseMessage()
                    type, data = message.loads(msg)
                    if type < 10:
                        print('receive chess message --> %s' % message.get_content())
                        self.message = message
                        self.chessPressed.emit()
                    elif 100 < type < 1000:
                        print('receive chat message --> %s' % message.get_content())
                        self.message = message.get_content()
                        self.chatReceived.emit()
                    elif type == 1003:
                        print('receive system message --> %s' % message.get_content())
                        self.message = message
                        self.systemReceived.emit()



class ChessBoard(QtGui.QWidget):
    NONE_FLAGS = 0      # 代表没有棋子
    WHITE_FLAGS = 1     # 代表白棋
    BLACK_FLAGS = 2     # 代表黑棋

    leftMargin = rightMargin = 21.0
    gridWidth = 0.0
    halfGridWidth = 0.0
    limit = 0.0
    chessWidth = 0.0
    chessHeight = 0.0

    def __init__(self, parent=None, sock=None, thread=None):
        super(ChessBoard, self).__init__(parent)
        self.setGeometry(QtCore.QRect(210, 20, 490, 490))
        self.whiteChessImage = QPixmap("../images/white.png")
        self.blackChessImage = QPixmap("../images/black.png")
        self.chessWidth = self.whiteChessImage.width()
        self.chessHeight = self.whiteChessImage.height()
        self.gridWidth = (self.geometry().width() - 21 * 2) / 14
        self.halfGridWidth = self.gridWidth / 2
        self.limit = self.leftMargin + self.halfGridWidth
        self.count = 0
        self.sock = sock
        self.thread = thread

        # 初始化棋盘数组
        self.list = [[(0, 0, self.NONE_FLAGS)] * 16 for i in range(16)]

        self.connect(self.thread, QtCore.SIGNAL("chessPressed()"), self.refreshBoard)

    def locateTo(self, x, y):
        """
        计算棋子该放置的坐标
        """
        n = int(math.ceil((x - self.limit) / self.gridWidth))
        m = int(math.ceil((y - self.limit) / self.gridWidth))
        if n <= 0:
            n = 0
        elif n > 15:
            n = 15

        if m <= 0:
            m = 0
        elif m > 15:
            m = 15
        return n, m, self.gridWidth * n + 21, self.gridWidth * m + 21

    def restart(self):
        """
        重新开始
        """
        self.list = [[(0, 0, self.NONE_FLAGS)] * 16 for i in range(16)]

    def clear(self):
        """
        清空棋盘
        """
        del self.list[:]

    def refreshBoard(self):
        message = self.thread.message
        n = message.get_content_by_key('n')
        m = message.get_content_by_key('m')
        x = message.get_content_by_key('x')
        y = message.get_content_by_key('y')
        flag = message.get_content_by_key('flag')
        self.list[n][m] = (float(x), float(y), flag)
        self.update()

    def updateList(self):
        pass

    def paintEvent(self, QPaintEvent):
        self.setAutoFillBackground(True)
        palette = QtGui.QPalette(self)
        palette.setBrush(QtGui.QPalette.Background,
                         QtGui.QBrush(QtGui.QPixmap("../images/chessboard.png")))
        self.setPalette(palette)

        painter = QPainter(self)

        for i in range(16):
            for j in range(16):
                x, y, type = self.list[i][j]
                if type == self.NONE_FLAGS:
                    continue
                elif type == self.WHITE_FLAGS:
                    painter.drawPixmap(x - self.chessWidth / 2.0, y - self.chessHeight / 2.0, self.chessWidth,
                                       self.chessHeight, self.whiteChessImage)
                elif type == self.BLACK_FLAGS:
                    painter.drawPixmap(x - self.chessWidth / 2.0, y - self.chessHeight / 2.0, self.chessWidth,
                                       self.chessHeight, self.blackChessImage)

    def mousePressEvent(self, QMouseEvent):
        """
        判断鼠标左键点击
        """
        if QMouseEvent.button() == Qt.LeftButton:
            curX = QMouseEvent.x()
            curY = QMouseEvent.y()
            self.count += 1
            n, m, x, y = self.locateTo(curX, curY)
            self.sock.send(ChessMessage(n, m, x, y, self.WHITE_FLAGS).dumps())
            if self.count % 2 == 0:
                self.list[n][m] = (float(x), float(y), self.WHITE_FLAGS)
                result = self.isWin(self.list, n, m, self.WHITE_FLAGS)
            else:
                self.list[n][m] = (float(x), float(y), self.BLACK_FLAGS)
                result = self.isWin(self.list, n, m, self.BLACK_FLAGS)
            self.update()

            #result = self.isWin(self.list, n, m, 1)
            if result:
                print("win")

    def isWin(self, list, x, y, chesstype):
        """
        判断输赢
        """
        return game.whowin(list, x, y, chesstype)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Gomoku")
    loginForm = GomokuLogin()
    loginForm.show()
    sys.exit(app.exec_())