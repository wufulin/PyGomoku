#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import sqlite3
from Queue import Queue
from common.tools import get_logger


class DBPool(object):

    logger = get_logger("DBPool")

    def __init__(self, maxconnectinos, connstr, dbtype):
        self._pool = Queue(maxconnectinos)
        self.connstr = connstr
        self.dbtype = dbtype
        self.maxconnections = maxconnectinos

        try:
            for i in range(maxconnectinos):
                self._add_connection(self._create_connection(self.connstr, self.dbtype))
        except Exception, e:
            self.logger.error("can not create db connection --> {0}".format(e.message))

    def _add_connection(self, conn):
        if self._pool.not_full:
            self._pool.put(conn)

    def get_connection(self):
        con = None
        if self._pool.not_empty:
            con = self._pool.get()
        return con

    def return_connection(self, conn):
        if self._pool.not_full:
            self._pool.put(conn)

    def _create_connection(self, connstr, dbtype):
        try:
            if dbtype == 'sqlite3':
                con = sqlite3.connect(connstr)
                return con
        except Exception, e:
            raise e

    def close(self):
        for i in range(self._pool.qsize()):
            self._pool.get().close()