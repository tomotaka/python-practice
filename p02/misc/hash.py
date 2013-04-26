def myhash(s):
    import hashlib
    import struct
    m = hashlib.md5()
    m.update(s)
    bindigest = m.digest()
    first4 = bindigest[0:4]
    ary = struct.unpack("I", first4)
    return ary[0]

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

x = myhash("hello")
print x
print simple_hash("hello")
#print len(x)

