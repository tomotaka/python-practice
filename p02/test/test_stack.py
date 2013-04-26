#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase
from nose.tools import *

from practice2 import Stack

class StackTest(TestCase):

    def test_all(self):
        a = Stack()
        eq_(0, a.size())
        eq_(0, a.size())

        b = Stack()
        eq_(0, b.size())
        b.push(10)
        eq_(1, b.size())
        b1 = b.pop()
        eq_(0, b.size())
        eq_(10, b1)

        c = Stack()
        eq_(0, c.size())
        c.push(10)
        eq_(1, c.size())
        c.push(20)
        eq_(2, c.size())
        c1 = c.pop()
        eq_(1, c.size())
        eq_(20, c1)
        c2 = c.pop()
        eq_(0, c.size())
        c.push(30)
        eq_(1, c.size())
        c3 = c.pop()
        eq_(0, c.size())
        eq_(30, c3)
        c.push(40)
        eq_(1, c.size())
        c.push(50)
        eq_(2, c.size())
        c4 = c.pop()
        eq_(1, c.size())
        eq_(50, c4)
        c5 = c.pop()
        eq_(0, c.size())
        eq_(40, c5)
        






