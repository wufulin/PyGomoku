#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wufulin'

import time
import logging


def now():
    return time.strftime('%H:%M:%S', time.localtime())


def get_logger(name):
    logging.basicConfig(level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    logger = logging.getLogger(name)
    return logger