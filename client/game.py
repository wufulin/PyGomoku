#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

v1 = [(0, -1), (0, 1)]      # 竖直方向
v2 = [(1, 0), (-1, 0)]      # 水平方向
v3 = [(1, -1), (-1, 1)]     # 右上到左下
v4 = [(-1, -1), (1, 1)]     # 左上到右下
v = [v1, v2, v3, v4]

WIN_NUMBER = 5
MAX_NUMBER = 15


def whowin(clist, x, y, chesstype, n=WIN_NUMBER):
    result = False

    for vector in v:
        m = scan_by_vector(clist, x, y, chesstype, vector)
        if m == n:
            result = True
            break

    return result


def scan_by_vector(clist, x, y, chesstype, vector):
    m = 1
    x0 = x
    y0 = y

    while True:
        x += vector[0][0]
        y += vector[0][1]
        if x in range(MAX_NUMBER + 1) and y in range(MAX_NUMBER + 1) and chesstype == clist[x][y][2]:
            m += 1
        else:
            x = x0
            y = y0
            break

    while True:
        x += vector[1][0]
        y += vector[1][1]
        if x in range(MAX_NUMBER + 1) and y in range(MAX_NUMBER + 1) and chesstype == clist[x][y][2]:
            m += 1
        else:
            x = x0
            y = y0
            break

    return m