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
    EQUAL=4,    # 和棋
    REGRET=5    # 悔棋
)

# 定义聊天消息枚举
# 枚举值大于100，小于1000
CHAT_MESSAGE = enum(
    NORMAL=101
)

# 定义系统消息枚举
# 枚举值大于1000
SYSTEM_MESSAGE = enum(
    LOGIN=1001,
    LOGOUT=1002,
    OPPONENT=1003
)


class BaseMessage(object):
    """
    消息类型基类
    """

    def __init__(self, message_type=None):
        """
        初始化
        """
        self.type = message_type
        self.dict = {"type": self.type}

    def dumps(self):
        """
        转换成Json格式
        """
        return json.dumps(self.dict)

    def loads(self, data):
        """
        转换成Python字典类型
        """
        self.dict = json.loads(data)
        self.type = self.dict['type']
        return self.type, self.dict

    def get_message_type(self):
        return self.type

    def get_content(self):
        if 'content' in self.dict.keys():
            return self.dict['content']

    def get_content_by_key(self, key):
        tmpDict = self.get_content()
        if tmpDict and key in tmpDict.keys():
            return tmpDict[key]


class ChessMessage(BaseMessage):
    """
    棋子消息类
    """

    def __init__(self, *args):
        if len(args) == 5:
            self.__init__step(*args)
        elif len(args) == 1:
            self.__init_start(*args)

    def __init__step(self, n=0, m=0, x=0, y=0, flag=0):
        # 初始化落子消息
        super(ChessMessage, self).__init__(CHESS_MESSAGE.STEP)
        self.n, self.m, self.x, self.y, self.flag = n, m, x, y, flag
        self.dict["content"] = {"x": self.x,
                                "y": self.y,
                                "n": self.n,
                                "m": self.m,
                                "flag": self.flag
        }

    def __init_start(self, type):
        # 开始选棋消息
        super(ChessMessage, self).__init__(type)
        self.dict['content'] = "start"

class ChatMessage(BaseMessage):
    """
    聊天消息类
    """

    def __init__(self, name, time, message):
        # 初始化聊天消息
        super(ChatMessage, self).__init__(CHAT_MESSAGE.NORMAL)
        content = name +' ' + time + '\n' + message + '\n'
        self.dict['content'] = content


class SystemMessage(BaseMessage):
    """
    系统消息类
    """
    def __init__(self, *args):
        if len(args) == 2:
            self.__init_opponent(*args)
        if len(args) == 4:
            self.__init_login(*args)

    def __init_login(self, *args):
         # 初始化登录或注销消息
        ip, port, time, type = args[0], args[1], args[2], args[3]
        if type == 1:
            super(SystemMessage, self).__init__(SYSTEM_MESSAGE.LOGIN)
            message = '[%s:%s] entered room at %s' % (ip, port, time)
        else:
            super(SystemMessage, self).__init__(SYSTEM_MESSAGE.LOGOUT)
            message = '[%s:%s] leaved room at %s' % (ip, port, time)

        self.dict['content'] = message

    def __init_opponent(self, *args):
        # 初始化棋子分配消息
        super(SystemMessage, self).__init__(args[0])
        self.dict['content'] = args[1]

if __name__ == '__main__':
    testMessage = ChessMessage(2, 3, 20, 21, 1)
    print(testMessage.dumps())

    str = '{"content": {"y": 21, "x": 20, "flag": 1, "m": 3, "n": 2}, "type": 1}'
    test1 = BaseMessage()
    type, dict = test1.loads(str)
    print(test1.get_content_by_key('x'))

    testMessage2 = SystemMessage("127.0.0.1", "53336", "2013-12-09", 2)
    print(testMessage2.dumps())

    testMessage3 = ChessMessage(CHESS_MESSAGE.START)
    print(testMessage3.dumps())

    testMessage4 = SystemMessage(SYSTEM_MESSAGE.OPPONENT, 2)
    print(testMessage4.dumps())

    #{
    #    type:CHAT_MESSAGE or CHESS_MESSAGE or SYSTEM_MESSAGE
    #    content:{
    #        n:1,
    #        m:2,
    #        x:20,
    #        y:30,
    #        flag:1
    #    }
    #}

    # {"content": {"y": 21, "x": 20, "flag": 1, "m": 3, "n": 2}, "type": 1}