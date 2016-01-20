#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

#文件操作

pathname="a.txt"

if __name__ == '__main__':
    try:
        f = open(pathname, "r")
    except:
        print "Failed to open file: %s"%pathname
        exit (-1)
    try:
        lines = f.readlines()
        for i in lines:
            print "new line ------->",i,
    except:
        pass
    finally:
        f.close()
        print "====== file closed! ======="


