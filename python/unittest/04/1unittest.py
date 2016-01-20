#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

import unittest
import myclass

class mytest(unittest.TestCase):
    #初始化方法
    def setUp(self):
        #实例化被测模块中的类
        self.tclass = myclass.foo()

    #每个以test开头的方法对应一个测试用例
    def test_sum(self):
        t = self.tclass
        self.assertEqual(t.sum(3, 5), 8)

    def test_sub(self):
        t = self.tclass
        self.assertEqual(t.sub(3, 5), 2, "WTF")
        #self.assertEqual(myclass.sub(3, 5), -2)
    #退出清理(cleanup)方法
    def tearDown(self):
        pass

#构造测试套件
def mysuite():
    suite = unittest.TestSuite()
    suite.addTest(mytest('test_sum'))
    suite.addTest(mytest('test_sub'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(mysuite())

