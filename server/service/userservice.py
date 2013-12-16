#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

from entity.user import User
from server.database.mydb import MyDB


class UserService(object):

    def __init__(self):
        self.db = MyDB("./database/gomoku.db3")

    def fetch_user(self, username, password):
        sql = r"select * from user where username = ?"
        result = self.db.queryone(sql, username)
        if result is not None:
            if result[2] == password:
                user = User(result[1], "", result[3], result[4], result[5])
                return user
            else:
                return "user password error!"
        else:
            return "%s user does not exist!" % username

    def fetch_users(self):
        sql = r"select * from user order by score desc"
        result = self.db.queryall(sql)
        users = []
        for r in result:
            user = User(r[1], "", r[3], r[4], r[5])
            users.append(user)
        return users

    def update_user(self, username, win, lose, score):
        sql = r"update user set win = ?, lose = ?, score = ? where username = ?"
        self.db.insert_or_update(sql, win, lose, score, username)

    def close(self):
        self.db.close()

if __name__ == '__main__':
    userservice = UserService()
    result = userservice.fetch_user('wufulin', '123456')
    if isinstance(result, User):
        print(result.dumps())
    else:
        print(result)

    userservice.update_user('wufulin', 2, 1, 10)
    print(userservice.fetch_user('wufulin', '123456'))

    userservice.close()