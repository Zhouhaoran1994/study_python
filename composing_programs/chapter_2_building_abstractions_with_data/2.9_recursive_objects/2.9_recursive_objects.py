from operator import add


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, index):
        if index == 0:
            return self.first
        else:
            return self.rest[index - 1]

    def __len__(self):
        return 1 + len(self.first)

    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + str(self.rest)
        return f'Link({self.first}{rest})'

    def __add__(self, other):
        if self.rest is Link.empty:
            return Link(self.first, other)
        else:
            return Link(self.first, self.rest + other)

        # if self is Link.empty:
        #     return other
        # else:
        #     return Link(s.first, self.rest+other)


def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        print(f, s.rest)
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered


def link_expression(s):
    """Return a string that would evaluate to s."""
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)


def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))


if __name__ == '__main__':
    s = Link(3, Link(4, Link(5)))
    # Link.__repr__ = link_expression
    print(s)
    print(s[1])
    print(s[2])

    odd = lambda x: x % 2 == 1
    filter_link(odd, s)

    # s2 = Link(3,4) # AssertionError

    # Link.__add__ = extend_link
    print(s + s)
