#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

#文件操作

pathname="a.txt"
#mylist = []
mylist = list()

if __name__ == '__main__':
    try:
        f = open(pathname, "r")
    except:
        print "Failed to open file: %s"%pathname
        exit (-1)
    try:
        done = 0
        while not done:
            line = f.readline()
            if line != '':
                mylist.append(line)
                print line
            else:
                done = 1
    except:
        pass
    finally:
        f.close()
        print "====== file closed! ======="

    mylist.sort()
    print mylist

