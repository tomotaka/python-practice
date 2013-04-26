#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase
from nose.tools import *

from practice2 import LinkedList

class LinkedListTest(TestCase):

    def test_append(self):
        a = LinkedList()
        a.append(1)
        eq_(1, a.get(0))
        a.append(2)
        eq_(1, a.get(0))
        eq_(2, a.get(1))

    def test_size(self):
        a = LinkedList()
        eq_(0, a.size())
        a.append(1)
        eq_(1, a.size())
        a.append(2)
        eq_(2, a.size())

    def test_set(self):
        a = LinkedList()
        a.append(1)
        eq_(1, a.get(0))
        a.set(0, 100)
        eq_(100, a.get(0))

        b = LinkedList()
        b.append(10)
        b.append(20)
        eq_(20, b.get(1))
        b.set(1, 200)
        eq_(200, b.get(1))

        c = LinkedList()
        c.append(11)
        c.append(22)
        c.append(33)
        eq_(22, c.get(1))
        c.set(1, 222)
        eq_(222, c.get(1))

    def test_remove(self):
        a = LinkedList()
        a.append(1)
        eq_(1, a.size())
        a.remove(0)
        eq_(0, a.size())
        a.append(2)
        eq_(1, a.size())
        eq_(2, a.get(0))

        b = LinkedList()
        b.append(10)
        b.append(20)
        eq_(2, b.size())
        eq_(10, b.get(0))
        eq_(20, b.get(1))
        b.remove(0)
        eq_(1, b.size())
        eq_(20, b.get(0))
        b.append(30)
        eq_(2, b.size())
        eq_(30, b.get(1))

        c = LinkedList()
        c.append(100)
        c.append(200)
        eq_(2, c.size())
        eq_(100, c.get(0))
        eq_(200, c.get(1))
        c.remove(1)
        eq_(1, c.size())
        eq_(100, c.get(0))
        c.append(300)
        eq_(2, c.size())
        eq_(300, c.get(1))

        d = LinkedList()
        d.append(1000)
        d.append(2000)
        d.append(3000)
        eq_(3, d.size())
        eq_(1000, d.get(0))
        eq_(2000, d.get(1))
        eq_(3000, d.get(2))
        d.remove(1)
        eq_(2, d.size())
        eq_(1000, d.get(0))
        eq_(3000, d.get(1))
        d.append(4000)
        eq_(3, d.size())
        eq_(4000, d.get(2))

    def test_insert(self):
        a = LinkedList()
        eq_(0, a.size())
        a.insert(10, 0)
        eq_(1, a.size())
        eq_(10, a.get(0))

        b = LinkedList()
        b.append(10)
        eq_(1, b.size())
        b.insert(20, 0)
        eq_(2, b.size())
        eq_(20, b.get(0))
        eq_(10, b.get(1))

        c = LinkedList()
        c.append(10)
        c.append(20)
        eq_(2, c.size())
        c.insert(30, 1)
        eq_(10, c.get(0))
        eq_(30, c.get(1))
        eq_(20, c.get(2))

        d = LinkedList()
        d.append(10)
        d.append(20)
        eq_(2, d.size())
        d.insert(30, 0)
        eq_(3, d.size())
        eq_(30, d.get(0))
        eq_(10, d.get(1))
        eq_(20, d.get(2))

        e = LinkedList()
        e.append(10)
        e.append(20)
        e.append(30)
        eq_(3, e.size())
        e.insert(40, 1)
        eq_(4, e.size())
        eq_(10, e.get(0))
        eq_(40, e.get(1))
        eq_(20, e.get(2))
        eq_(30, e.get(3))

        f = LinkedList()
        f.append(10)
        f.remove(0)
        eq_(0, f.size())
        f.insert(11, 0)
        eq_(1, f.size())
        eq_(11, f.get(0))

        f.append(100)
        f.append(200)
        eq_(3, f.size())
        eq_(100, f.get(1))
        eq_(200, f.get(2))
        f.insert(300, 1)
        eq_(4, f.size())
        eq_(11, f.get(0))
        eq_(300, f.get(1))
        eq_(100, f.get(2))
        eq_(200, f.get(3))





        




        

        


    

        



