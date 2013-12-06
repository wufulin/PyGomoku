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

    def __init__(self, n=0, m=0, x=0, y=0, flag=0):
        # 初始化落子消息
        super(ChessMessage, self).__init__(CHESS_MESSAGE.STEP)
        self.n, self.m, self.x, self.y, self.flag = n, m, x, y, flag
        self.dict["content"] = {"x": self.x,
                                "y": self.y,
                                "n": self.n,
                                "m": self.m,
                                "flag": self.flag
        }


class ChatMessage(BaseMessage):
    """
    聊天消息类
    """

    def __init__(self):
        pass


class LoginMessage(BaseMessage):
    """
    登录消息类
    """

    def __init__(self):
        pass


if __name__ == '__main__':
    testMessage = ChessMessage(2,3,20,21,1)
    print(testMessage.dumps())

    str = '{"content": {"y": 21, "x": 20, "flag": 1, "m": 3, "n": 2}, "type": 1}'
    test1 = BaseMessage()
    type, dict = test1.loads(str)
    print(dict)
    print(test1.get_content_by_key('x'))

    #{
    #    type:CHAT_MESSAGE or CHESS_MESSAGE
    #    content:{
    #        n:1,
    #        m:2,
    #        x:20,
    #        y:30,
    #        flag:1
    #    }
    #}

    # {"content": {"y": 21, "x": 20, "flag": 1, "m": 3, "n": 2}, "type": 1}