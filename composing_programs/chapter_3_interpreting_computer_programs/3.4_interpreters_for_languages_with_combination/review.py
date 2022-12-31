"""
实现目标：
> expr = Pair('+', Pair(Pair('*', Pair(3, Pair(4, nil))), Pair(5, nil)))
> print(expr)
(+ (* 3 4) 5)

> (- 100 (* 7 (+ 8 (/ -12 -3))))
16.0
"""


class Pair:

    def __init__(self, first, second):
        """
        > s = Pair(1, Pair(2, nil))
        """
        self.first = first
        self.second = second

    def __len__(self):
        """
        > len(s)
        > 2

        > s = Pair(1, Pair(2, 3))
        > len(s)
        TypeError("length attempted on improper list")
        """
        n, second = 0, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError("length attempted on improper list")
        return n

    def __getitem__(self, i):
        """
        > s[1]
        2

        > s = Pair(1, Pair(2, 3))
        > s[1]
        2
        > s[2]
        TypeError("ill-formed list")
        > s[-1]
        IndexError("negative index into list")
        > s[3]
        IndexError("list index out of bounds")
        """
        if i < 0:
            raise IndexError("negative index into list")
        y = self
        for _ in range(i):
            y = y.second
            if y is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(y, Pair):
                raise TypeError("ill-formed list")
        return y.first

    def __repr__(self):
        """
        > s
        Pair(1, Pair(2, nil))
        """
        return f'Pair({repr(self.first)}, {repr(self.second)})'

    def __str__(self):
        """
        > s = Pair(1, Pair(2, nil))
        > print(s)
        (1 2)

        > s = Pair(1, Pair(2, 3))
        > print(s)
        (1 2·3)
        """
        s = '(' + str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s = s + ' ' + str(second.first)
            second = second.second
        if second is not nil:
            s = s + '·' + str(second)
        s = s + ')'
        return s

    def map(self, fn):
        """
        > print(s.map(lambda x: x+4))
        (5 6)

        > s = Pair(1, Pair(2, 3))
        > s.map(lambda x: x+4)
        TypeError("ill-formed list")
        """
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(fn(self.first), self.second.map(fn))
        else:
            raise TypeError("ill-formed list")


class nil:
    def __repr__(self):
        return 'nul'

    def __str__(self):
        return ''

    def map(self, fn):
        return self


nil = nil()

if __name__ == '__main__':
    s1 = Pair(1, Pair(2, Pair(3, nil)))
    print(repr(s1))
    print(s1)
    print(len(s1))
    print(s1[2])
    try:
        print(s1[4])
    except IndexError as e:
        print(e)
    print(s1.map(lambda x: x + 4))

    s2 = Pair(1, Pair(2, Pair(3, 4)))
    print(repr(s2))
    print(s2)
    try:
        print(len(s2))
    except TypeError as e:
        print(e)
    try:
        print(s2[-1])
    except IndexError as e:
        print(e)
    try:
        print(s2[3])
    except TypeError as e:
        print(e)
    try:
        print(s2.map(lambda x: x + 4))
    except TypeError as e:
        print(e)

    expr = Pair('+', Pair(Pair('*', Pair(3, Pair(4, nil))), Pair(5, nil)))
    assert str(expr) == '(+ (* 3 4) 5)'
    assert str(expr.second.first) == '(* 3 4)'
    assert expr.second.first.second.first == 3