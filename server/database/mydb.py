#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import sqlite3


class MyDB(object):
    DB_FILE = "gomoku.db3"
    CREATE_TABLE = r'''
        create table user (
            id integer primary key autoincrement,
            username varchar(20),
            win integer,
            lose integer,
            score integer
        )
    '''

    def __init__(self, file=DB_FILE):
        self.con = sqlite3.connect(file)

    def create_table(self, sql):
        cur = self.con.cursor()
        cur.execute(sql)
        cur.close()
        self.con.commit()

    def drop_table(self, tablename):
        cur = self.con.cursor()
        cur.execute('drop table ' + tablename)
        cur.close()
        self.con.commit()

    def queryone(self, sql, *args):
        cur = self.con.cursor()
        cur.execute(sql, args)
        result = cur.fetchone()
        cur.close()
        return result

    def queryall(self, sql, *args):
        cur = self.con.cursor()
        cur.execute(sql, args)
        result = cur.fetchall()
        cur.close()
        return result

    def insert(self, sql, *args):
        cur = self.con.cursor()
        cur.execute(sql, args)
        cur.close()
        self.con.commit()

    def update(self, sql, *args):
        cur = self.con.cursor()
        cur.execute(sql, args)
        cur.close()
        self.con.commit()

    def close(self):
        self.con.close()


if __name__ == '__main__':
    db = MyDB()
    # db.create_table(db.CREATE_TABLE)
    # db.insert("insert into user(username, win, lose, score) values (?, ?, ?, ?)", 'wufulin', 10, 2, 20)
    result = db.queryall(r'select * from user')
    print(result)