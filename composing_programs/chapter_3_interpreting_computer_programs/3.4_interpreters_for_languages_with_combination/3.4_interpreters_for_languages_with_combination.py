class Pair:

    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    # Pair(1, Pair(2, Pair(3, nil)))
    def __repr__(self):
        return f'Pair({self.first}, {repr(self.rest)})'

    # (1 2 3)
    def __str__(self):
        # if self is Pair.nil:
        #     return ''
        # elif self.rest is Pair.nil:
        #     return str(self.first)
        # else:
        #     result = str(self.first) + ' ' + str(self.rest)
        #     # return f'({self.first} {self.rest})'
        # return result

        s = "(" + str(self.first)
        rest = self.rest
        while isinstance(rest, Pair):
            s += " " + str(rest.first)
            rest = rest.rest
        if rest is not nil:
            s += " . " + str(rest)
        return s + ")"

    # s = Pair(1, Pair(2, Pair(3, nil)))
    # len(s) = 3
    def __len__(self):
        # return 1 + len(self.rest)

        n, rest = 1, self.rest
        while isinstance(rest, Pair):
            n += 1
            rest = rest.rest
        if rest is not nil:
            raise TypeError('length attempted on improper list')
        return n

    def __getitem__(self, k):
        # if i < 0 or i >= len(self):
        #     raise IndexError('list index out of range')
        # n, rest = 1, self.rest
        # if i == 0:
        #     return self.first
        # else:
        #     while n < len(self):
        #         if n == i:
        #             return rest.first
        #         n += 1
        #         rest = rest.rest

        if k < 0:
            raise IndexError("negative index into list")
        y = self
        for _ in range(k):  # 老师没有用len(self)，避免了耦合
            if y.rest is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(y.rest, Pair):  # 允许创建Pair(1, 2)，但不允许getitem?
                raise TypeError("ill-formed list")
            y = y.rest
        return y.first

    def map(self, fn):
        # return Pair(fn(self.first), self.rest.map(fn))

        # 和getitem一样，允许创建Pair(1, 2)，但不允许map
        mapped = fn(self.first)
        if self.rest is nil or isinstance(self.rest, Pair):
            return Pair(mapped, self.rest.map(fn))
        else:
            raise TypeError("ill-formed list")


class nil:
    def __repr__(self):
        return 'nil'

    def __len__(self):
        return 0

    def map(self, fn):
        return self


nil = nil()

if __name__ == '__main__':
    s = Pair(1, Pair(2, Pair(3, nil)))
    # s = Pair(1, Pair(2, Pair(3, 4))) # TypeError: length attempted on improper list
    print(repr(s))
    print(str(s))
    print(len(s))
    print(s[2])
    print(s.map(lambda x: x + 4))
