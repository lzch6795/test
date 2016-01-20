#!/usr/bin/python2
# -*- coding: utf-8 -*-

import random

mlist = [23, 3, 56, 18, 23, 34]
mtuple = ('zacard', 'jack', 'mary', 'lucy')

if __name__ == "__main__":
    print "==============="
    print mlist
    # choice 从列表中选择一个元素
    print 'choice:',random.choice(mlist)
    # shuffle打乱元素顺序
    print 'shuffle:',random.shuffle(mlist)
    print mlist

    print '-----------------------------------'
    print mtuple
    print 'choice:',random.choice(mtuple)
    # 元组元素不支持赋值操作
    #print 'shuffle:',random.shuffle(mtuple)


    print '\n-----------------------------------'
    print 'range(10):',range(10)
    print 'range(3, 10):',range(3,10)

    print random.uniform(1, 3)


