#!/usr/bin/python
# -*- coding: utf-8 -*-
from entity.user import User

__author__ = 'wufulin'

from common.tools import get_logger
from common.message import *
from userservice import UserService


class Handler(object):

    logger = get_logger('handler')

    def __init__(self, queue):
        self._nexthandler = None
        self.queue = queue

    def next(self, handler):
        self._nexthandler = handler


class ChessMessageHandler(Handler):
    def handle(self, message):
        if message['type'] < 10:
            self.logger.debug('handle chess message --> {0}'.format(str(message)))
        else:
            self._nexthandler.handle(message)


class ChatMessageHandler(Handler):
    def handle(self, message):
        if 100 < message['type'] < 1000:
            self.logger.debug('handle chat message --> {0}'.format(str(message)))
        else:
            self._nexthandler.handle(message)


class SystemMessageHandler(Handler):
    def handle(self, message):
        type = message['type']
        resp = None

        if 1000 < type:
            self.logger.debug('handle system message --> {0}'.format(str(message)))
            if type == SYSTEM_MESSAGE.LOGIN:
                userservice = UserService()
                user = User.loads(message['content'])
                result = userservice.fetch_user(user.username, user.password)

                if isinstance(result, User):
                    resp = SystemMessage.create_verified_pass(result)
                else:
                    resp = SystemMessage.create_verified_failed(result)

            if resp is not None:
                self.logger.debug("send message --> %s" % resp.dumps())
                self.queue.put(resp.dumps())
        else:
            self.logger.debug('can not handle --> {0}'.format(str(message)))