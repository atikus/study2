"""
slot örneği
deneme 5
"""

class feed(object):
    __slots__ = ["__a", "b", "c", "d"]

    def __init__(self, a=0, b=19):
        self.__a = a
        self.b = b
        self.c = float(0)
        self.d = "denem"
    
    @property
    def m(self):
        return self.__a

    @m.setter
    def m(self, v):
        defff = type(v)
        if defff is int:
            self.__a = v
        else:
            self.__a = 0
    
    @property
    def geta(self):
        return self.__a


print(dir(feed))
f = feed()

f.m = 65536 * 65536
f.b = "qwe"
f.d = "fener"

print(f.m)
print(f.c)



quit()

ff = []

f8 = feed()
f8.m = 8
f8.b = "fb"

ff.append(f8)
ff.append(feed(12,17))

hhh = [x.b for x in ff if x.a == 5]

print(hhh)

bv = lambda x: x > 10

if bv(18):
    print("ok1")

lll = [x for x in range(30) if bv(x)]

print(lll)



class deneme(object):
    g = 23

    def __init__(self):
        self.g = 75
        print("yaz : %d" % self.g)

    def yaz1(self, a):
        self.g += a
        print("yaz1 : %d" % self.g)

    @classmethod
    def olustur(cls):
        cls.g = 50
        return deneme()

    @classmethod
    def olustur20(cls):
        cls.g = 20
        return deneme()

    @classmethod
    def yaz2(cls, a):
        cls.g += a
        print("yaz2 : %d" % cls.g)

    @staticmethod
    def yaz3():
        print("yaz3 : %d" % deneme.g)


d = deneme.olustur20()

d.yaz1(6)
d.yaz2(8)
d.yaz3()
d.yaz3()
d.yaz2(2)









"""
class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)

a=A()

a.foo(1)

a.class_foo(1)

a.static_foo(1)
a.static_foo("hi")
"""