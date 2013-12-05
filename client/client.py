#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import sys
import math
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *

import chess
import game

class GomokuClient(QtGui.QWidget, chess.Ui_chessDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.__init_ui()

    def __init_ui(self):
        self.setupUi(self)
        self.chessboard = ChessBoard(self)


    def __init_socket(self):
        pass

    def start(self):
        pass

    def sendChessMessage(self):
        pass

    def receivedMessage(self):
        pass


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

    def __init__(self, parent=None):
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

        # 初始化棋盘数组
        self.list = [[(0, 0, self.NONE_FLAGS)] * 16 for i in range(16)]

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
            print('n = %d, m = %d, x = %d, y = %d' % (self.locateTo(curX, curY)))
            n, m, x, y = self.locateTo(curX, curY)
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
    client = GomokuClient()
    client.show()
    sys.exit(app.exec_())