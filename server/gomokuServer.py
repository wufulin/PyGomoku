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
        self.inputs = []
        self.outputs = []
        self.message_queues = {}

        self.opponent_list = []
        self.white_opponent = False
        self.black_opponent = False

    def _init_handlers(self):
        chesshandler = ChessMessageHandler()
        chathandler = ChatMessageHandler()
        systemhandler = SystemMessageHandler()

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
        self.inputs.append(self.server_sock)
        self._init_handlers()
        return True

    def shutdown(self):
        if self.server_sock:
            try:
                self.server_sock.close()
            except (KeyboardInterrupt, error):
                pass

        self.server_sock = None

        for n in self.inputs:
            if not n:
                continue
            try:
                n.close()
            except:
                pass

        for n in self.outputs:
            if not n:
                continue
            try:
                n.close()
            except:
                pass

        self.inputs = []
        self.outputs = []
        self.message_queues.clear()

    def broadcast(self, sock, message):
        # 服务端向大厅广播消息，除发送者外
        for socket in self.outputs:
            if socket != sock:
                try:
                    self.logger.debug("broadcast message --> %s" % message)
                    socket.send(message)
                except Exception, e:
                    self.logger.debug("broadcast message error --> {0}".format(str(e)))
                    self.outputs.remove(socket)
                    socket.close()

    def broadcast_one(self, sock, othersock, message):
        # 向对手发送消息
        pass

    def run(self):
        try:
            while True:
                read_sockets, write_sockets, error_sockets = select.select(self.inputs,
                                                                           self.outputs,
                                                                           self.inputs)

                for sock in error_sockets:
                    self.logger.error("exception condition on ", sock.getpeername())
                    self.inputs.remove(sock)
                    if sock in self.outputs:
                        self.outputs.remove(sock)
                    sock.close()
                    del self.message_queues[sock]

                for sock in read_sockets:
                    if sock == self.server_sock:
                        client, addr = self.server_sock.accept()
                        self.inputs.append(client)
                        self.message_queues[client] = Queue.Queue()
                        self.logger.debug("[%s:%s] connected" % (addr[0], addr[1]))
                    else:
                        data = sock.recv(BUFSIZE)
                        if data:
                            if sock not in self.outputs:
                                self.outputs.append(sock)
                            message = json.loads(data, encoding='utf-8')
                            response = self.handlers.handle(message)
                            if response is not None:
                                self.message_queues[sock].put(response)
                        else:
                            # 在对方关闭连接的情况下（CLOSE_WAIT状态）会立即返回，并且处于可读列表里面。
                            # 但是却会立即读到0长度的数据
                            if sock in self.outputs:
                                self.outputs.remove(sock)
                            self.inputs.remove(sock)
                            self.logger.debug("[%s:%s] disconnected" % (sock.getpeername()[0], sock.getpeername()[1]))
                            sock.close()
                            del self.message_queues[sock]

                for sock in write_sockets:
                    if self.message_queues.has_key(sock) and self.message_queues[sock].qsize() > 0:
                        message = self.message_queues[sock].get_nowait()
                        next_msg = message.dumps()
                        if message.type > 1002:
                            self.broadcast(sock, next_msg)
                        else:
                            self.logger.debug("send message --> %s" % next_msg)
                            sock.send(next_msg)


        except KeyboardInterrupt:
            self.logger.debug('server shutdown now because keyboard interrupt')
        finally:
            self.shutdown()

if __name__ == '__main__':
    gomokuServer = GomokuServer(addr=ADDR)
    result = gomokuServer.startup()
    if result:
        gomokuServer.logger.debug('Gomoku server started on port ' + str(ADDR[1]))
        gomokuServer.run()
