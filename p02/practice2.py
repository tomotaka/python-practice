#!/usr/bin/python
# -*- coding: utf-8 -*-


class LinkedListItem(object):

    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item


class LinkedList(object):

    def __init__(self):
        self._start = None

    def get(self, n):
        current = self._get_item(n)
        return current.value

    def _get_item(self, n):
        if self._start is None:
            raise IndexError()
        i = 0
        current = self._start
        while i < n:
            current = current.next_item
            if current is None:
                raise IndexError()
            i += 1
        return current

    def set(self, n, obj):
        size = self.size()
        if size-1 < n:
            d = n - (size-1)
            for i in range(d):
                self.append(None)
            self.append(obj)
        else:
            n_item = self._get_item(n)
            n_item.value = obj

    def size(self):
        count = 0
        current = self._start
        while current is not None:
            current = current.next_item
            count += 1
        return count

    def append(self, obj):
        if self._start is None:
            self._start = LinkedListItem(value=obj, next_item=None)
        else:
            item = self._start
            while item.next_item is not None:
                item = item.next_item
            item.next_item = LinkedListItem(value=obj, next_item=None)

    def insert(self, obj, n):
        size = self.size()
        if n == 0:
            if size == 0:
                self._start = LinkedListItem(value=obj, next_item=None)
            else:
                first = self._get_item(0)
                self._start = LinkedListItem(value=obj, next_item=first)
        elif n < size:
            the_item = self._get_item(n)
            prev_item = self._get_item(n-1)
            prev_item.next_item = LinkedListItem(value=obj, next_item=the_item)
        else:
            raise IndexError()

    def remove(self, n):
        size = self.size()
        if n == 0:
            if size == 1:
                self._start = None
            else:
                self._start = self._get_item(1)
        elif n < size:
            if n == size-1:
                self._get_item(n-1).next_item = None
            else:
                prev_item = self._get_item(n-1)
                next_item = self._get_item(n+1)
                prev_item.next_item = next_item
        else:
            raise IndexError()

    def __getitem__(self, n):
        return self.get(n)

    def __setitem__(self, n, obj):
        self.set(n, obj)

    def __len__(self):
        return self.size()


class Stack(object):
    def __init__(self):
        self._list = LinkedList()
    def push(self, obj):
        self._list.insert(obj, 0)
    def pop(self):
        item = self._list.get(0)
        self._list.remove(0)
        return item
    def size(self):
        return self._list.size()
    def __len__(self):
        return self.size()


class Queue(object):
    def __init__(self):
        self._list = LinkedList()
    def push(self, obj):
        self._list.append(obj)
    def take(self):
        item = self._list.get(0)
        self._list.remove(0)
        return item
    def size(self):
        return self._list.size()
    def __len__(self):
        return self.size()


def simple_hash(s):
    import struct
    fmt = ""
    for i in range(len(s)):
        fmt = fmt + "B"
    numbers = struct.unpack(fmt, s)
    ret = 0
    for n in numbers:
        ret = ret * 33 + n
    return ret


class KeyValuePair(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v


class Hashtable(object):
    def __init__(self, bucket_size=15):
        self._buckets = LinkedList()
        self._bucket_size = bucket_size
        for i in range(self._bucket_size):
            self._buckets.append(LinkedList())

    def get(self, key):
        return self._get_kvp(key).value

    def put(self, key, value):
        try:
            # no exeption: key already exists
            self._get_kvp(key).value = value
        except KeyError:
            self._get_bucket(key).append(KeyValuePair(key, value))
        
        # rehash if buckets are too few
        if 1.5 < (float(self.size()) / self._bucket_size):
            self._rehash()

    def remove(self, key):
        bucket = self._get_bucket(key)
        remove_idx = -1  # default: not found
        for i in range(bucket.size()):
            kvp = bucket.get(i)
            if kvp.key == key:
                remove_idx  = i  # found
                break
        if remove_idx != -1:
            bucket.remove(remove_idx)

    def size(self):
        return self.keys().size()

    def keys(self):
        ret = LinkedList()
        for lst in self._buckets:
            for kvp in lst:
                ret.append(kvp.key)
        return ret

    def _get_bucket(self, key):
        bucket_idx = self._hash(key) % self._bucket_size
        return self._buckets.get(bucket_idx)

    def _get_kvp(self, key):
        for kvp in self._get_bucket(key):
            if kvp.key == key:
                return kvp
        raise KeyError()  # not found

    def _hash(self, key):
        return simple_hash(key)

    def _rehash(self):
        next_size = self._bucket_size * 2
        new_ht = Hashtable(bucket_size=next_size)
        keys = self.keys()
        for i in range(keys.size()):
            key = keys.get(i)
            new_ht.put(key, self.get(key))
        self._buckets = new_ht._buckets
        self._bucket_size = new_ht._bucket_size

    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return self.size()

