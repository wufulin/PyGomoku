#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import select
import Queue
from socket import *
from common.config import *
from service.handler import *
from common.tools import get_logger


class GomokuServer(object):
    logger = get_logger('server')

    def __init__(self, addr=None):
        self.addr = addr
        self.server_sock = None
        self.sendqueue = Queue.Queue()
        self.connection_list = []
        self.opponent_list = []
        self.white_opponent = False
        self.black_opponent = False

    def _init_handlers(self):
        chesshandler = ChessMessageHandler(self.sendqueue)
        chathandler = ChatMessageHandler(self.sendqueue)
        systemhandler = SystemMessageHandler(self.sendqueue)

        chesshandler.next(chathandler)
        chathandler.next(systemhandler)
        self.handlers = chesshandler

    def startup(self):
        self.shutdown()
        self.server_sock = socket(AF_INET, SOCK_STREAM)
        try:
            self.server_sock.bind(self.addr)
        except:
            try:
                self.server_sock.close()
            except:
                pass
            return False
        self.server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_sock.listen(65536)
        self.server_sock.setblocking(False)
        self.connection_list.append(self.server_sock)
        self._init_handlers()
        return True

    def shutdown(self):
        if self.server_sock:
            try:
                self.server_sock.close()
            except (KeyboardInterrupt, error):
                pass

        self.server_sock = None

        for n in self.connection_list:
            if not n:
                continue
            try:
                n.close()
            except:
                pass

        self.connection_list = []

    def broadcast_data(self, sock, message):
        # 向接收者广播消息，除发送者和服务器端外
        for socket in self.connection_list:
            if socket != self.server_sock and socket != sock:
                try:
                    socket.send(message)
                except Exception, e:
                    print(str(e))
                    socket.close()
                    self.connection_list.remove(socket)

    def setOpponent(self, sock):
        # 设置对手
        for socket in self.connection_list:
            if socket == sock:
                try:
                    if not self.white_opponent:
                        self.white_opponent = True
                        msg = SystemMessage(SYSTEM_MESSAGE.OPPONENT, 1)
                    elif not self.black_opponent:
                        self.black_opponent = True
                        msg = SystemMessage(SYSTEM_MESSAGE.OPPONENT, 2)
                    socket.send(msg.dumps())
                except Exception, e:
                    print(str(e))
                    self.white_opponent = False
                    self.black_opponent = False
                    socket.close()
                    self.connection_list.remove(socket)

    def clearOpponent(self, sock, data):
        # 重置
        for socket in self.connection_list:
            if socket == sock:
                type = data['content']
                if type == 1:
                    self.white_opponent = False
                else:
                    self.black_opponent = False
                self.connection_list.remove(socket)

    def run(self):
        try:
            while True:
                read_sockets, write_sockets, error_sockets = select.select(self.connection_list, self.connection_list,
                                                                           self.connection_list)

                for sock in error_sockets:
                    self.connection_list.remove(sock)
                    sock.close()

                for sock in read_sockets:
                    if sock == self.server_sock:
                        client, addr = self.server_sock.accept()
                        self.connection_list.append(client)
                        self.logger.debug("[%s:%s] connected" % (addr[0], addr[1]))
                    else:
                        try:
                            data = sock.recv(BUFSIZE)
                            if data != "":
                                message = json.loads(data, encoding='utf-8')
                                self.handlers.handle(message)
                        except:
                            self.connection_list.remove(sock)
                            sock.close()
                            continue

                for sock in write_sockets:
                    if sock != self.server_sock:
                        if self.sendqueue.qsize() > 0:
                            sock.send(self.sendqueue.get())


        except KeyboardInterrupt:
            self.logger.debug('server shutdown now because keyboard interrupt')
        finally:
            self.shutdown()


if __name__ == '__main__':
    gomokuServer = GomokuServer(addr=ADDR)
    result = gomokuServer.startup()
    if result:
        print('Gomoku server started on port ' + str(ADDR[1]))
        gomokuServer.run()
