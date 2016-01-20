#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

#文件操作

pathname="a.txt"

if __name__ == '__main__':
    try:
        with open(pathname, "r") as f:
            for i in f:
                print i
    except:
        print "Failed to open file: %s"%pathname
        exit (-1)
