from math import gcd
from operator import add

"""Arithmetic"""


class Account:

    def __init__(self, holder_name, balance=[]):
        self.holder_name = holder_name
        self.balance = balance

    def __repr__(self):
        return 'aaa'

    def __bool__(self):
        return self.balance != 0

    def __add__(self, other):
        # return [self.balance[i] + other.balance[i] for i in range(len(self.balance))]
        return list(map(add, self.balance, other.balance))

    def __getitem__(self, item):
        if item == 1:
            return self.balance


# a = Account()
# print(a.__repr__())
# print(repr(Account))
# print(a)
# if not Account('Jack'):
#     print('Jack has nothing')

# rich = Account('rich', 1000)
# poor = Account('poor',20)
# print(rich + poor)

# rich = Account('rich', [1000, 2000, 3000])
# poor = Account('poor', [10, 20, 30])
# print(rich + poor)
#
# Account.__bool__ = lambda self: self.balance != 0
#
# Account.__getitem__ = lambda self, item: self.balance if item == 2 else None
#
# print(poor[2])

"""Type dispatching"""


def add_complex_and_rational(c, r):
    return ComplexRI(c.real + r.numer / r.denom, c.imag)


def mul_complex_and_rational(c, r):
    r_magnitude, r_angle = r.numer / r.denom, 0
    if r_magnitude < 0:
        r_magnitude, r_angle = -r_magnitude, pi
    return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)


def add_rational_and_complex(r, c):
    return add_complex_and_rational(c, r)


def mul_rational_and_complex(r, c):
    return mul_complex_and_rational(c, r)


class Number:
    def __add__(self, other):
        if self.tag_type == other.tag_type:
            return self.add(other)
        elif (self.tag_type, other.tag_type) in self.adders:
            return self.cross_apply(other, self.adders)

    def __mul__(self, other):
        if self.type_tag == other.type_tag:
            return self.mul(other)
        elif (self.type_tag, other.type_tag) in self.multipliers:
            return self.cross_apply(other, self.multipliers)

    def cross_apply(self, other, cross_fn):
        cross_fn = cross_fn[(self.tag_type, other.tag_type)]
        return cross_fn(self, other)

    adders = {
        ("com", "rat"): add_complex_and_rational,
        ("rat", "com"): add_rational_and_complex
    }
    multipliers = {
        ("com", "rat"): mul_complex_and_rational,
        ("rat", "com"): mul_rational_and_complex
    }


class Rational(Number):
    tag_type = 'rat'

    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)

    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)


class Complex(Number):
    tag_type = 'com'

    def add(self, other):
        # 注意这个Complex类依然没有__init__，因为根据开头的公式定义，不同的表达里有不同的变量，把变量的初始化交给具体的子类
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def mul(self, other):
        return ComplexMA(self.magnitude * other.magnitude, self.angle + other.angle)


from math import atan2, sin, cos, pi


class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # 为什么要实现这两个property装饰的方法？
    # 因为事实上，这两种表达方式可以互相转换
    # 作者可能想传达的是，即使现在没有这样的需求，难保未来会有
    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return f"ComplexRI({self.real}, {self.imag})"


class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return f"ComplexMA({self.magnitude}, {self.angle / pi} * pi)"


result = ComplexRI(1.5, 0) + Rational(3, 2)
print(result)
