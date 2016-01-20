#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

#文件操作

#pathname="a.txt"
pathname="b.txt"

if __name__ == '__main__':
    try:
        f = open(pathname, "r")
    except:
        print "Failed to open file: %s"%pathname
        exit (-1)
    try:
        print f.read()
    except:
        pass
    finally:
        f.close()
        print "======file closed!======="


