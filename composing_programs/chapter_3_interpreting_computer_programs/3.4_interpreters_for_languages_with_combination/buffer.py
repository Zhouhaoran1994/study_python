import math


class Buffer:
    """
    >>> buf = Buffer(iter([['(', '+'], [15], [12, ')']]))
    >>> buf.pop()
    '('
    >>> buf.pop()
    '+'
    >>> buf.current()
    15
    >>> print(buf)
    1: ( +
    2:  >> 15
    >>> buf.pop()
    15
    >>> buf.current()
    12
    >>> buf.pop()
    12
    >>> print(buf)
    1: ( +
    2: 15
    3: 12 >> )
    >>> buf.pop()
    ')'
    >>> print(buf)
    1: ( +
    2: 15
    3: 12 ) >>
    >>> buf.pop()  # returns None
    """
    def __init__(self, source):
        self.index = 0
        self.source = source
        self.lines = []
        self.current_line = ()
        self.current()

    def pop(self):
        current = self.current()
        self.index += 1
        return current

    @property
    def more_in_lines(self):
        return self.index < len(self.current_line)

    def current(self):
        # 其实就是遍历每个列表里面的字列表
        while not self.more_in_lines:
            self.index = 0
            try:
                self.current_line = next(self.source)
                self.lines.append(self.current_line)
            except StopIteration:
                self.current_line = ()
                return None
        return self.current_line[self.index]

    # def __str__(self):
    # s = '{0:>4}: '
    # 1:  ( \n
    # 2: >>
    #

    def __str__(self):
        """Return recently read contents; current element marked with >>."""
        # Format string for right-justified line numbers
        n = len(self.lines)
        msg = '{0:>' + str(math.floor(math.log10(n)) + 1) + "}: "

        # Up to three previous lines and current line are included in output
        s = ''
        for i in range(max(0, n - 4), n - 1):
            s += msg.format(i + 1) + ' '.join(map(str, self.lines[i])) + '\n'
        s += msg.format(n)
        s += ' '.join(map(str, self.current_line[:self.index]))
        s += ' >> '
        s += ' '.join(map(str, self.current_line[self.index:]))
        return s.strip()

    # def __repr__(self):
    #     n = len(self.lines)
    #     s = ''
    #     msg = '{0}: '
    #     for i in range(n-1):
    #         s += '{0}: '.format(i+1) + ' '.join(map(str, self.lines[i])) + '\n'
    #     s += msg.format(n)
    #     s += ' '.join(map(str, self.current_line[:self.index]))
    #     s += ' >> '
    #     s += ' '.join(map(str, self.current_line[self.index:]))
    #     return s.strip()

class InputReader(object):
    """An InputReader is an iterable that prompts the user for input."""
    def __init__(self, prompt):
        self.prompt = prompt

    def __iter__(self):
        while True:
            yield input(self.prompt)
            self.prompt = ' ' * len(self.prompt)

if __name__ == '__main__':
    buf = Buffer(iter([['(', '+'], [15], [12, ')']]))
    buf.pop()
    buf.pop()
    buf.pop()
    buf.pop()
