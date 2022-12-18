def rational_to_complex(r):
    return ComplexRI(r.numer / r.denom, 0)


class Number:
    def __add__(self, other):
        x, y = self.coerce(other)
        return x.add(y)

    def __mul__(self, other):
        x, y = self.coerce(other)
        return x.mul(y)

    def coerce(self, other):
        if self.type_tag == other.type_tag:
            return self, other
        elif (self.type_tag, other.type_tag) in self.coercions:
            return (self.coerce_to(other.type_tag), other)
        elif (other.type_tag, self.type_tag) in self.coercions:
            return (self, other.coerce_to(self.type_tag))

    def coerce_to(self, other_tag):
        coercion_fn = self.coercions[(self.type_tag, other_tag)]
        return coercion_fn(self)

    coercions = {('rat', 'com'): rational_to_complex}


class Rational(Number):
    type_tag = 'rat'

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
    type_tag = 'com'

    def add(self, other):
        # 注意这个Complex类依然没有__init__，因为根据开头的公式定义，不同的表达里有不同的变量，把变量的初始化交给具体的子类
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def mul(self, other):
        return ComplexMA(self.magnitude * other.magnitude, self.angle + other.angle)


from math import atan2, sin, cos, pi, gcd


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


if __name__ == '__main__':
    result = ComplexRI(1.5, 0) + Rational(3, 2)
    # result = Rational(3, 2) + ComplexRI(1.5, 0)
    print(result)
