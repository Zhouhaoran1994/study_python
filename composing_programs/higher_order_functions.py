def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)

    return wrapped


@trace
def triple(x):
    return x * 3


triple(3)
