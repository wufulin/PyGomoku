#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import pool

class MyDB(object):
    DB_FILE = "gomoku.db3"
    CREATE_TABLE = r'''
        create table user (
            id integer primary key autoincrement,
            username varchar(20),
            password varchar(20),
            win integer,
            lose integer,
            score integer
        )
    '''

    def __init__(self, file=DB_FILE):
        self.pool = pool.DBPool(4, file, 'sqlite3')

    def create_table(self, sql):
        con = self.pool.get_connection()
        cur = con.cursor()
        cur.execute(sql)
        cur.close()
        con.commit()
        self.pool.return_connection(con)

    def drop_table(self, tablename):
        con = self.pool.get_connection()
        cur = con.cursor()
        cur.execute('drop table ' + tablename)
        cur.close()
        con.commit()
        self.pool.return_connection(con)

    def queryone(self, sql, *args):
        con = self.pool.get_connection()
        cur = con.cursor()
        cur.execute(sql, args)
        result = cur.fetchone()
        cur.close()
        self.pool.return_connection(con)
        return result

    def queryall(self, sql, *args):
        con = self.pool.get_connection()
        cur = con.cursor()
        cur.execute(sql, args)
        result = cur.fetchall()
        cur.close()
        self.pool.return_connection(con)
        return result

    def insert_or_update(self, sql, *args):
        con = self.pool.get_connection()
        cur = con.cursor()
        cur.execute(sql, args)
        cur.close()
        con.commit()
        self.pool.return_connection(con)

    def close(self):
        self.pool.close()


if __name__ == '__main__':
    db = MyDB()
    # db.create_table(db.CREATE_TABLE)
    db.insert_or_update("insert into user(username, password, win, lose, score)\
    values (?, ?, ?, ?, ?)", 'wufulin', '123456', 10, 2, 20)
    db.close()
