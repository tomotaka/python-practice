#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase
from nose.tools import *

from practice2 import Queue

class QueueTest(TestCase):

    def test_all(self):
        a = Queue()
        eq_(0, a.size())
        eq_(0, a.size())

        b = Queue()
        eq_(0, b.size())
        b.push(10)
        eq_(1, b.size())
        b_first = b.take()
        eq_(0, b.size())
        eq_(10, b_first)

        c = Queue()
        eq_(0, c.size())
        c.push(10)
        eq_(1, c.size())
        c.push(20)
        eq_(2, c.size())
        c1 = c.take()
        eq_(1, c.size())
        eq_(10, c1)
        c2 = c.take()
        eq_(0, c.size())
        eq_(20, c2)

        c.push(30)
        eq_(1, c.size())
        c.push(40)
        eq_(2, c.size())
        c3 = c.take()
        eq_(1, c.size())
        eq_(30, c3)
        c4 = c.take()
        eq_(0, c.size())
        eq_(40, c4)




