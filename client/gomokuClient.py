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
        self.setWindowTitle(self.username)
        self.setButtonStatus(True, False, False, False, True)

        self.connect(self.btnSend, SIGNAL('clicked()'), self.sendChatMessage)
        self.connect(self.btnStart, SIGNAL('clicked()'), self.startChess)
        self.connect(self.btnBackMove, SIGNAL('clicked()'), self.backMoveChess)
        self.connect(self.btnLeave, SIGNAL('clicked()'), self.leaveChess)
        self.connect(self.btnAgain, SIGNAL('clicked()'), self.againChess)
        self.connect(self.btnLose, SIGNAL('clicked()'), self.loseChess)

        self.connect(self.backthread, SIGNAL('chatMsgReceived()'), self.handleChatMessage)
        self.connect(self.backthread, SIGNAL('systemMsgReceived()'), self.handleSystemMessage)
        self.connect(self.backthread, SIGNAL('chessWinMsgReceived()'), self.handleChessWinMessage)
        self.connect(self.backthread, SIGNAL('chessLoseMsgReceived()'), self.handleChessLoseMessage)

    def setButtonStatus(self, btnStartStatus, btnLoseStatus, btnAgainStatus, btnBackMoveStatus, btnLeaveStatus):
        """
        设置按钮状态
        """
        self.btnStart.setEnabled(btnStartStatus)
        self.btnLose.setEnabled(btnLoseStatus)
        self.btnAgain.setEnabled(btnAgainStatus)
        self.btnBackMove.setEnabled(btnBackMoveStatus)
        self.btnLeave.setEnabled(btnLeaveStatus)

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
        self.setButtonStatus(False, True, False, True, True)
        message = ChessMessage(CHESS_MESSAGE.START)
        self.client_sock.send(message.dumps())

    def againChess(self):
        """
        再来一局
        """
        self.setButtonStatus(False, True, False, True, True)
        self.chessboard.restart()
        message = ChessMessage(CHESS_MESSAGE.AGAIN)
        self.client_sock.send(message.dumps())

    def loseChess(self):
        """
        认输
        """
        self.setButtonStatus(False, False, True, False, True)
        message = ChessMessage(CHESS_MESSAGE.LOSE, self.chesstype)
        self.client_sock.send(message.dumps())
        QtGui.QMessageBox.information(self, u"提示", u"你认输了")

    def backMoveChess(self):
        """
        悔棋
        """
        self.chessboard.backmove()

    def leaveChess(self):
        """
        离开房间
        """
        message = SystemMessage(SYSTEM_MESSAGE.EXIT, self.chesstype)
        self.client_sock.send(message.dumps())
        self.chesstype = NONE_FLAGS

    def sendChatMessage(self):
        # 得到用户输入的消息、输入时间
        chatMsg = str(self.lineEdit.text()).decode('utf-8')
        name = "test"
        message = ChatMessage(name, now(), chatMsg)
        self.textBrowser.append(message.get_content())
        self.client_sock.send(message.dumps())
        self.lineEdit.clear()

    def handleChatMessage(self):
        # 接收服务器的聊天消息
        self.textBrowser.append(self.backthread.message)

    def handleChessWinMessage(self):
        self.setButtonStatus(False, False, True, False, True)
        whoWin = self.backthread.message.get_content()
        if whoWin == WHITE_FLAGS:
            QtGui.QMessageBox.information(self, u"恭喜", u"白棋赢了")
        else:
            QtGui.QMessageBox.information(self, u"恭喜", u"黑棋赢了")

        # TODO: 积分

    def handleChessLoseMessage(self):
        self.setButtonStatus(False, False, True, False, True)
        whoLose = self.backthread.message.get_content()
        if whoLose == WHITE_FLAGS:
             QtGui.QMessageBox.information(self, u"恭喜", u"白棋认输了")
        else:
            QtGui.QMessageBox.information(self, u"恭喜", u"黑棋认输了")

    def handleSystemMessage(self):
        message = self.backthread.message
        if message.get_content() == WHITE_FLAGS:
            self.chesstype = WHITE_FLAGS  # 白棋
            self.widget1.setStyleSheet("background-image: url(:/background/white.png) no-repeat;")
            self.widget2.setStyleSheet("background-image: url(:/background/black.png) no-repeat;")
            self.leftFrame.setStyleSheet("background-image: url(:/background/avatar1.jpg);")
            self.rightFrame.setStyleSheet("background-image: url(:/background/avatar2.jpg);")
        elif message.get_content() == BLACK_FLAGS:
            self.chesstype = BLACK_FLAGS  # 黑棋
            self.widget1.setStyleSheet("background-image: url(:/background/black.png) no-repeat;")
            self.widget2.setStyleSheet("background-image: url(:/background/white.png) no-repeat;")
            self.leftFrame.setStyleSheet("background-image: url(:/background/avatar2.jpg);")
            self.rightFrame.setStyleSheet("background-image: url(:/background/avatar1.jpg);")

        self.chessboard.CHESS_TYPE = self.chesstype
        self.chessboard.isstart = True
        if self.chesstype == WHITE_FLAGS:
            # 白棋先手
            self.chessboard.isnext = True
            self.chessboard.isend = False

    def closeEvent(self, event):
        """
        退出房间时，发送消息给服务端，令其重置相关资源
        """
        message = SystemMessage(SYSTEM_MESSAGE.EXIT, self.chesstype)
        self.client_sock.send(message.dumps())
        self.chesstype = NONE_FLAGS


class BackendThread(QtCore.QThread):

    chessWinMsgReceived = QtCore.pyqtSignal()
    chessLoseMsgReceived = QtCore.pyqtSignal()
    chessPressed = QtCore.pyqtSignal()
    chatMsgReceived = QtCore.pyqtSignal()
    systemMsgReceived = QtCore.pyqtSignal()
    chessRegretMsgReceived = QtCore.pyqtSignal()
    chessAgainMsgReceived = QtCore.pyqtSignal()

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
                        if type == CHESS_MESSAGE.WIN:
                            self.chessWinMsgReceived.emit()
                        elif type == CHESS_MESSAGE.LOSE:
                            self.chessLoseMsgReceived.emit()
                        elif type == CHESS_MESSAGE.STEP:
                            self.chessPressed.emit()
                        elif type == CHESS_MESSAGE.REGRET:
                            self.chessRegretMsgReceived.emit()
                        elif type == CHESS_MESSAGE.AGAIN:
                            self.chessAgainMsgReceived.emit()
                    elif 100 < type < 1000:
                        print('receive chat message --> %s' % message.get_content())
                        self.message = message.get_content()
                        self.chatMsgReceived.emit()
                    elif type == 1003:
                        print('receive system message --> %s' % message.get_content())
                        self.message = message
                        self.systemMsgReceived.emit()


class ChessBoard(QtGui.QWidget):

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
        self.sock = sock
        self.thread = thread
        self.isstart = False
        self.isnext = False
        self.isend = False
        self.CHESS_TYPE = NONE_FLAGS

        # 初始化棋盘数组
        self.list = [[(0, 0, NONE_FLAGS)] * 16 for i in range(16)]

        self.connect(self.thread, QtCore.SIGNAL("chessPressed()"), self.refreshBoard)
        self.connect(self.thread, QtCore.SIGNAL('chessRegretMsgReceived()'), self.handleChessRegretMessage)
        self.connect(self.thread, QtCore.SIGNAL("chessAgainMsgReceived()"), self.handleChessAgainMessage)

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
        self.list = [[(0, 0, NONE_FLAGS)] * 16 for i in range(16)]
        self.isend = False
        if self.CHESS_TYPE == WHITE_FLAGS:
            # 白棋先手
            self.isnext = True
            self.isstart = True
        else:
            self.isnext = False
            self.isstart = False

        self.update()

    def refreshBoard(self):
        message = self.thread.message
        n = message.get_content_by_key('n')
        m = message.get_content_by_key('m')
        x = message.get_content_by_key('x')
        y = message.get_content_by_key('y')
        flag = message.get_content_by_key('flag')
        self.list[n][m] = (float(x), float(y), flag)
        self.update()

        self.isnext = True
        self.isstart = True

    def handleChessRegretMessage(self):
        message = self.thread.message
        n = message.get_content_by_key('n')
        m = message.get_content_by_key('m')
        x = message.get_content_by_key('x')
        y = message.get_content_by_key('y')
        self.list[n][m] = (float(x), float(y), NONE_FLAGS)
        self.update()

        self.isnext = False

    def handleChessAgainMessage(self):
        self.restart()

    def backmove(self):
        self.list[self.n][self.m] = (float(self.x), float(self.y), NONE_FLAGS)
        self.update()
        self.isnext = True

        message = ChessMessage(self.n, self.m, self.x, self.y)
        self.sock.send(message.dumps())

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
                if type == NONE_FLAGS:
                    continue
                elif type == WHITE_FLAGS:
                    painter.drawPixmap(x - self.chessWidth / 2.0, y - self.chessHeight / 2.0, self.chessWidth,
                                       self.chessHeight, self.whiteChessImage)
                elif type == BLACK_FLAGS:
                    painter.drawPixmap(x - self.chessWidth / 2.0, y - self.chessHeight / 2.0, self.chessWidth,
                                       self.chessHeight, self.blackChessImage)

    def mousePressEvent(self, QMouseEvent):
        """
        判断鼠标左键点击
        """
        if QMouseEvent.button() == Qt.LeftButton:
            if not self.isstart:
                QtGui.QMessageBox.information(self, u"提示", u"对弈还未开始,白棋先手")
                return

            if not self.isnext:
                QtGui.QMessageBox.information(self, u"提示", u"您的对手还未下，请等待")
                return

            curX = QMouseEvent.x()
            curY = QMouseEvent.y()
            self.n, self.m, self.x, self.y = self.locateTo(curX, curY)
            if self.list[self.n][self.m][2] != NONE_FLAGS:
                return
            self.list[self.n][self.m] = (float(self.x), float(self.y), self.CHESS_TYPE)
            self.isnext = False
            self.update()

            self.sock.send(ChessMessage(self.n, self.m, self.x, self.y, self.CHESS_TYPE).dumps())

            result = self.isWin(self.list, self.n, self.m, self.CHESS_TYPE)

            if result:
                self.sock.send(ChessMessage(CHESS_MESSAGE.WIN, self.CHESS_TYPE).dumps())
                QtGui.QMessageBox.information(self, u"恭喜", "You win")

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