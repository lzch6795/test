#!/usr/bin/python2
# -*- coding: utf-8 -*-

import collections

#命名元组
Person = collections.namedtuple('Person', 'name age gender')
print 'Type of Person:',type(Person)

Bob = Person(name='Bob', age=23, gender='male')

print 'Representation:',Bob

Jane = Person(name='Jane', age=27, gender='female')
print 'Field By Name:',Jane.name

print '---------------------------------'
for i in [Bob, Jane]:
    print "%s is %d years old %s"% i

print Person._fields

#重命名模式开启
Dog = collections.namedtuple('dogi', 'def age gender', rename=True)

#print dogi._fields
print Dog._fields

