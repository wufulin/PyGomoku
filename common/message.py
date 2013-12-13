#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import json

# 定义枚举
def enum(**enums):
    return type('Enum', (), enums)

# 定义棋子消息枚举
# 枚举值都是小于10
CHESS_MESSAGE = enum(
    END=-1,     # 结束游戏
    START=0,    # 开始游戏
    STEP=1,     # 落子
    LOSE=2,     # 输棋
    WIN=3,      # 赢棋
    RESTART=4,  # 再来一局
    REGRET=5    # 悔棋
)

# 定义聊天消息枚举
# 枚举值大于100，小于1000
CHAT_MESSAGE = enum(
    HALL=101,   # 大厅聊天消息
    ROOM=102    # 房间聊天消息
)

# 定义系统消息枚举
# 枚举值大于1000
SYSTEM_MESSAGE = enum(
    LOGIN=1001,
    LOGOUT=1002,
    OPPONENT=1003,
    LEAVE=1004
)


class ChessMessage(object):
    """
    棋子消息类
    """
    def __init__(self, hall=None, room=None, type=None, descriptor=None, content={}):
        self.hall = hall
        self.room = room
        self.type = type
        self.descriptor = descriptor
        self.content = content

    def __repr__(self):
        return repr(self.__dict__)

    def gettype(self):
        return self.type

    def getcontent(self):
        return self.content

    def dumps(self):
        d = {}
        d.update(self.__dict__)
        return json.dumps(d)

    @classmethod
    def loads(cls, data):
        d = json.loads(data)
        instance = cls.__new__(cls)
        instance.hall = d['hall']
        instance.room = d['room']
        instance.type = d['type']
        instance.descriptor = d['descriptor']
        instance.content = d['content']
        return instance

    @classmethod
    def create_start(cls, hall=1, room=1, flag=0):
        instance = cls.__new__(cls)
        instance.hall = hall
        instance.room = room
        instance.type = CHESS_MESSAGE.START
        instance.descriptor = "开始消息"
        instance.content = {"flag": flag}
        return instance

    @classmethod
    def create_restart(cls, hall=1, room=1, flag=0):
        instance = cls.__new__(cls)
        instance.hall = hall
        instance.room = room
        instance.type = CHESS_MESSAGE.RESTART
        instance.descriptor = "再来一局消息"
        instance.content = {"flag": flag}
        return instance

    @classmethod
    def create_step(cls, hall=1, room=1, n=0, m=0, x=0, y=0, flag=0):
        instance = cls.__new__(cls)
        instance.hall = hall
        instance.room = room
        instance.type = CHESS_MESSAGE.STEP
        instance.descriptor = "落子消息"
        instance.content = {"n": n,
                            "m": m,
                            "x": x,
                            "y": y,
                            "flag": flag}
        return instance

    @classmethod
    def create_regret(cls, hall=1, room=1, n=0, m=0, x=0, y=0):
        instance = cls.__new__(cls)
        instance.hall = hall
        instance.room = room
        instance.type = CHESS_MESSAGE.REGRET
        instance.descriptor = "悔棋消息"
        instance.content = {"n": n,
                            "m": m,
                            "x": x,
                            "y": y}
        return instance

    @classmethod
    def create_win(cls, hall=1, room=1, flag=0):
        instance = cls.__new__(cls)
        instance.hall = hall
        instance.room = room
        instance.type = CHESS_MESSAGE.WIN
        instance.descriptor = "赢棋消息"
        instance.content = {"flag": flag}
        return instance

    @classmethod
    def create_lose(cls, hall=1, room=1, flag=0):
        instance = cls.__new__(cls)
        instance.hall = hall
        instance.room = room
        instance.type = CHESS_MESSAGE.LOSE
        instance.descriptor = "输棋消息"
        instance.content = {"flag": flag}
        return instance

    @classmethod
    def create_end(cls, hall=1, room=1, flag=0):
        instance = cls.__new__(cls)
        instance.hall = hall
        instance.room = room
        instance.type = CHESS_MESSAGE.END
        instance.descriptor = "结束消息"
        instance.content = {"flag": flag}
        return instance


class ChatMessage(object):
    """
    聊天消息类
    """
    def __init__(self, hall=None, room=None, type=None, descriptor=None, content=None):
        self.hall = hall
        self.room = room
        self.type = type
        self.descriptor = descriptor
        self.content = content

    def __repr__(self):
        return repr(self.__dict__)

    def gettype(self):
        return self.type

    def getcontent(self):
        return self.content

    def dumps(self):
        d = {}
        d.update(self.__dict__)
        return json.dumps(d)

    @classmethod
    def loads(cls, data):
        d = json.loads(data)
        instance = cls.__new__(cls)
        instance.hall = d['hall']
        instance.room = d['room']
        instance.type = d['type']
        instance.descriptor = d['descriptor']
        instance.content = d['content']
        return instance

    @classmethod
    def create_hall_msg(cls, name, time, message, hall=1):
        instance = cls.__new__(cls)
        instance.hall = hall
        instance.room = 0
        instance.type = CHAT_MESSAGE.HALL
        instance.descriptor = "大厅聊天消息"
        instance.content = name +' ' + time + '\n' + message + '\n'
        return instance

    @classmethod
    def create_room_msg(cls, name, time, message, room=1):
        instance = cls.__new__(cls)
        instance.hall = 0
        instance.room = room
        instance.type = CHAT_MESSAGE.ROOM
        instance.descriptor = "房间聊天消息"
        instance.content = name +' ' + time + '\n' + message + '\n'
        return instance


class SystemMessage(object):
    """
    系统消息类
    """
    def __init__(self, type=None, descriptor=None, content=None):
        self.type = type
        self.descriptor = descriptor
        self.content = content

    def __repr__(self):
        return repr(self.__dict__)

    def gettype(self):
        return self.type

    def getcontent(self):
        return self.content

    def dumps(self):
        d = {}
        d.update(self.__dict__)
        return json.dumps(d)

    @classmethod
    def loads(cls, data):
        d = json.loads(data)
        instance = cls.__new__(cls)
        instance.type = d['type']
        instance.descriptor = d['descriptor']
        instance.content = d['content']
        return instance

    @classmethod
    def create_login(cls, username, ip, port, time):
        instance = cls.__new__(cls)
        instance.type = SYSTEM_MESSAGE.LOGIN
        instance.descriptor = "用户登录消息"
        instance.content = '%s [%s:%s] login at %s' % (username, ip, port, time)
        return instance

    @classmethod
    def create_logout(cls, username, ip, port, time):
        instance = cls.__new__(cls)
        instance.type = SYSTEM_MESSAGE.LOGOUT
        instance.descriptor = "用户注销消息"
        instance.content = '%s [%s:%s] logout at %s' % (username, ip, port, time)
        return instance

    @classmethod
    def create_leave(cls, username, time, room=1):
        instance = cls.__new__(cls)
        instance.type = SYSTEM_MESSAGE.LEAVE
        instance.descriptor = "用户退出房间消息"
        instance.content = '%s leave %d room at %s' % (username, room, time)
        return instance

    def __init_opponent(self, *args):
        # 初始化棋子分配消息
        super(SystemMessage, self).__init__(args[0])
        self.dict['content'] = args[1]
