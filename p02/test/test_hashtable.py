#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase
from nose.tools import *

from practice2 import KeyValuePair, Hashtable, LinkedList

class KeyValuePairTest(TestCase):

    def test_key_value(self):
        a = KeyValuePair("key1", 10)
        eq_("key1", a.key)
        eq_(10, a.value)

        b = KeyValuePair("key2", 20)
        eq_("key2", b.key)
        eq_(20, b.value)

class HashtableTest(TestCase):

    def test_put_get(self):
        a = Hashtable()
        a.put("key1", 100)
        eq_(100, a.get("key1"))
        eq_(100, a.get("key1"))

        a.put("key2", 200)
        eq_(200, a.get("key2"))
        eq_(100, a.get("key1"))

        for i in range(100):
            v = i * 10 + 3
            k = "key%d" % v
            a.put(k, v)
            eq_(v, a.get(k))

    @raises(KeyError)
    def test_unknown_key1(self):
        a = Hashtable()
        a.get("hoge")

    @raises(KeyError)
    def test_unknown_key2(self):
        a = Hashtable()
        a.put("hoge", "hogevalue")
        a.get("fuga")

    @raises(KeyError)
    def test_unknown_key3(self):
        a = Hashtable()
        for i in range(100):
            v = i
            k = "key%d" % v
            a.put(k, v)
        a.get("very-unknown-key")

    @raises(KeyError)
    def test_removed_key1(self):
        a = Hashtable()
        a.put("key1", 100)
        a.remove("key1")
        a.get("key1")

    @raises(KeyError)
    def test_removed_key2(self):
        a = Hashtable()
        for i in range(100):
            k = "key%d" % i
            a.put(k, i)
        eq_(10, a.get("key10"))
        a.remove("key10")
        a.get("key10")

    def test_remove(self):
        a = Hashtable()
        eq_(0, a.size())
        a.put("a", 10)
        eq_(1, a.size())
        a.remove("a")
        eq_(0, a.size())

        b = Hashtable()
        eq_(0, b.size())
        b.put("a", 10)
        b.put("b", 20)
        eq_(2, b.size())
        b.remove("a")
        eq_(1, b.size())
        b.remove("b")
        eq_(0, b.size())

        c = Hashtable()
        c_keys = []
        for i in range(100):
            k = "key%d" % i
            c_keys.append(k)
            c.put(k, i)
        eq_(100, c.size())
        removed_count = 0
        for key in c_keys:
            c.remove(key)
            removed_count += 1
            eq_(100 - removed_count, c.size())

    def test_size(self):
        a = Hashtable()
        eq_(0, a.size())

        b = Hashtable()
        eq_(0, b.size())
        b.put("a", 10)
        eq_(1, b.size())
        b.put("b", 20)
        eq_(2, b.size())

        c = Hashtable()
        eq_(0, c.size())
        for i in range(100):
            k = "key%d" % i
            c.put(k, i)
            eq_(i+1, c.size())

    def test_keys(self):
        a = Hashtable()
        ka = a.keys()
        eq_(LinkedList, type(ka))
        eq_(0, ka.size())

        b = Hashtable()
        b.put("key1", 10)
        kb = b.keys()
        eq_(LinkedList, type(kb))
        eq_(1, kb.size())
        eq_("key1", kb.get(0))

        c = Hashtable()
        c_keys = []
        for i in range(100):
            k = "key%d" % i
            c_keys.append(k)
            c.put(k, i)
        kc = c.keys()
        eq_(LinkedList, type(kc))
        for k in c_keys:
            ok_(self._is_included(k, kc))

    def _is_included(self, item, linked_list):
        size = linked_list.size()
        for i in range(size):
            if item == linked_list.get(i):
                return True
        return False



