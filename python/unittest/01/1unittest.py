#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

import unittest
import myclass

class mytest(unittest.TestCase):
    #初始化方法
    def setUp(self):
        pass

    #每个以test开头的方法对应一个测试用例
    def test_sum(self):
        self.assertEqual(myclass.sum(3, 5), 8)

    def test_sub(self):
        self.assertEqual(myclass.sub(3, 5), 2, "WTF")
        #self.assertEqual(myclass.sub(3, 5), -2)
    #退出清理(cleanup)方法
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
