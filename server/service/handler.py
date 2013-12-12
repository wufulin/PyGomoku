#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import common.tools as tools

class Handler(object):

    logger = tools.get_logger('handler')

    def __init__(self):
        self._nexthandler = None

    def next(self, handler):
        self._nexthandler = handler


class ChessMessageHandler(Handler):
    def handle(self, message):
        if message.get_message_type() < 10:
            self.logger.debug('start handle chess message --> {0}'.format(str(message)))
        else:
            self._nexthandler.handle(self, message)


class ChatMessageHandler(Handler):
    def handle(self, message):
        if 100 < message.get_message_type() < 1000:
            self.logger.debug('start handle chat message --> {0}'.format(str(message)))
        else:
            self._nexthandler.handle(self, message)


class SystemMessageHandler(Handler):
    def handle(self, message):
        if 1000 < message.get_message_type():
            self.logger.debug('start handle system message --> {0}'.format(str(message)))
        else:
            self.logger.debug('can not handle --> {0}'.format(str(message)))