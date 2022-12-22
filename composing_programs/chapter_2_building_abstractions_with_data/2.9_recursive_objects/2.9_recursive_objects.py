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
            return self.rest[index-1]

    def __len__(self):
        return 1 + len(self.first)

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

if __name__ == '__main__':
    s = Link(3, Link(4, Link(5)))
    print(s)
    print(s[1])
    print(s[2])

    odd = lambda x: x%2 == 1
    filter_link(odd, s)
