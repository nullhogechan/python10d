#! /usr/bin/env python
# coding: utf-8

x = '2'
try:
    r = 1 + x
except:
    r = 1 + int(x)
print r