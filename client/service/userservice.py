#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

from entity.user import User
from common.message import SystemMessage

class UserService(object):

    def __init__(self, thread):
        self.thread = thread

    def verifyUser(self, username, password):
        user = User(username, password)
        msg = SystemMessage.create_login(user)
        self.thread.add_msg(msg)

    def logoutByUser(self, username):
        user = User(username, "")
        msg = SystemMessage.create_logout(user)
        self.thread.add_msg(msg)

    def fetchAllUser(self):
        msg = SystemMessage