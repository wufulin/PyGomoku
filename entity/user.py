#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import json

class User(object):

    def __init__(self, username, password, win=0, lose=0, score=0):
        self.username = username
        self.password = password
        self.win = win
        self.lose = lose
        self.score = score

    def __str__(self):
        return "username = %s\t win = %d\t lose = %d\t score = %d" % (self.username, self.win, self.lose, self.score)

    def dumps(self):
        d = {}
        d.update(self.__dict__)
        return json.dumps(d)

    @classmethod
    def loads(cls, data):
        d = json.loads(data)
        instance = cls.__new__(cls)
        instance.username = d['username']
        instance.password = d['password']
        instance.win = d['win']
        instance.lose = d['lose']
        instance.score = d['score']
        return instance

if __name__ == '__main__':
    user = User('wufulin', 'abc', 10, 4, 30)
    print(user.dumps())

    user2 = User.loads('{\"username\": \"wufulin\", \"win\": 0, \"password\": \"123456\", \"score\": 0, \"lose\": 0}')
    print(user2)