from math import sqrt


class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess


def improve(update, done, guess=1, max_updates=1000):
    k = 0
    try:
        while not done(guess) and k < max_updates:
            guess = update(guess)
            k = k + 1
        return guess
    except ValueError:
        raise IterImproveError(guess)


def newton_update(f, df): # df是f的求导函数
    def update(x):
        return x - f(x) / df(x)

    return update


def find_zero(f, df, guess=1):
    def done(x):
        return f(x) == 0

    try:
        return improve(newton_update(f, df), done, guess)
    except IterImproveError as e:
        print('error!')
        return e.last_guess


if __name__ == '__main__':
    result = find_zero(lambda x: 2 * x * x + sqrt(x), lambda x: 4 * x + 0.5 * x ** -.5)
    print(result)
    # sqrt(-1) # ValueError: math domain error