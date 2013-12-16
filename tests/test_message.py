#!/usr/bin/python
# -*- coding: utf-8 -*-
from entity.user import User

__author__ = "wufulin"

import unittest
from common.message import *


class TestMessage(unittest.TestCase):
    def test_chess_start(self):
        s = ChessMessage.create_start()
        obj = ChessMessage.loads(s.dumps())
        self.assertEquals(obj.descriptor, u'开始消息')

    def test_chess_restart(self):
        s = ChessMessage.create_restart(2, 3, 1)
        print(s.dumps())

    def test_chess_regret(self):
        s = ChessMessage.create_regret()
        print(s.dumps())

    def test_chat_hall_msg(self):
        s = ChatMessage.create_hall_msg('wufulin', "2012-02-10 10:30:15", "go back")
        print(s.dumps())

    def test_chat_room_msg(self):
        s = ChatMessage.create_room_msg('wufulin', "2012-02-10 10:30:15", "enter room")
        print(s.dumps())

    def test_sys_login_msg(self):
        user = User('wufulin', '123456')
        s = SystemMessage.create_login(user)
        print(s.dumps())

        obj = SystemMessage.loads(s.dumps())
        self.assertEqual(obj.gettype(), 1001)

if __name__ == "__main__":
    unittest.main()