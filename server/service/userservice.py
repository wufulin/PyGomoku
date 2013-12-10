#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

from server.entity.user import User
from server.database.mydb import MyDB

class UserService(object):

    def fetchUserByUsername(self, username):
        pass

    def fetchAllUser(self):
        pass

    def close(self):
        pass


class UserServiceImpl(UserService):

    def __init__(self):
        self.db = MyDB("../database/gomoku.db3")

    def fetchUserByUsername(self, username):
        sql = r"select * from user where username = ?"
        result = self.db.queryone(sql, username)
        user = User(result[1], result[2], result[3], result[4])
        return user

    def fetchAllUser(self):
        sql = r"select * from user"
        result = self.db.queryall(sql)
        users = []
        for r in result:
            user = User(r[1], r[2], r[3], r[4])
            users.append(user)
        return users

    def close(self):
        self.db.close()

if __name__ == '__main__':
    userservice = UserServiceImpl()
    user = userservice.fetchUserByUsername('wufulin')
    print(user)

    list = userservice.fetchAllUser()
    print(list)

    userservice.close()