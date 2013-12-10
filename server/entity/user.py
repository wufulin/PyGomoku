#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

class User(object):

    def __init__(self, username, win, lose, score):
        self.username = username
        self.win = win
        self.lose = lose
        self.score = score

    def __str__(self):
        return "username = %s\t win = %d\t lose = %d\t score = %d" % (self.username, self.win, self.lose, self.score)

if __name__ == '__main__':
    user = User('wufulin', 10, 4, 30)
    print(str(user))