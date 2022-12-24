from turtle import *


# for _ in range(5):
#     color('red', 'white')
#     forward(100)
#     color('blue', 'white')
#     for _ in range(5):
#         forward(20)
#         right(144)
#     color('red', 'white')
#     right(144)
# end_fill()
# done()

def repeat(k, fn):
    if k > 0:
        fn()
        repeat(k - 1, fn)
    else:
        return None


def tri(fn):
    def g():
        fn()
        left(120)

    return repeat(3, g)


def sier(d, k):
    def fn():
        if k == 1:
            forward(d)
        else:
            leg(d, k)

    return tri(fn)


def leg(d, k):
    sier(d / 2, k - 1)
    penup()
    forward(d)
    pendown()


sier(400, 4)
done()
