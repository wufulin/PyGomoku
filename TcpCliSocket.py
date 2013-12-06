#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import select
from socket import *
from util.config import *
import sys

def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()


if __name__ == '__main__':

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.settimeout(2)

    try:
        tcpCliSock.connect(ADDR)
    except Exception, e:
        print('Unable to connect --> %s' % str(e))
        sys.exit()

    print('Connected to remote host. Start sending messages')
    prompt()

    while True:
        socket_list = [sys.stdin, tcpCliSock]

        # get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            # incoming message from remote server
            if sock == tcpCliSock:
                data = sock.recv(BUFSIZE)
                if not data:
                    print("\nDisconnected from chat server")
                    sys.exit()
                else:
                    #print data
                    sys.stdout.write(data)
                    prompt()
            # user entered a message
            else:
                msg = sys.stdin.readline()
                tcpCliSock.send(msg)
                prompt()
                #try:
                #    while True:
                #        data = raw_input('> ')
                #        if not data:
                #            break
                #        tcpCliSock.send(data)
                #
                #        data = tcpCliSock.recv(BUFSIZE)
                #        if not data:
                #            break
                #        print(data)
                #except KeyboardInterrupt, e:
                #    print(e.message)
                #finally:
                #    tcpCliSock.close()