#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

#文件操作



if __name__ == '__main__':
    f = open("a.txt", "r")
    out = f.read()
    print out
    f.close()


