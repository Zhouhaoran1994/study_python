# Higher-Order Functions

functions that can accept other functions as arguments or return functions as values

接收或返回其他函数的函数

~~~python
def f(fn):
    def g(y):
        return fn(y)

    return g
~~~

## Functions as Arguments (接收其他函数的函数)

假设现在有3种求和的算法

~~~python
# 前n项和
def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


# 前n项的立方和
def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k * k * k, k + 1
    return total


# 前n项的特定算法和
def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4 * k - 3) * (4 * k - 1)), k + 1
    return total
~~~

可以看出，其实除了具体的算法各异外，其他部分完全一致，所以可以把算法部分抽象（abstraction）出来，即term

~~~
def <name>(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + <term>(k), k + 1
    return total
~~~

把term抽象出来后，就可以写成这样

~~~python
def summation(n, fn):
    total, k = 0, 1
    while k <= n:
        total, k = total + fn(k), k + 1
    return total


def natural_term(n):
    return n


def cubes_term(n):
    return pow(n, 3)


def pi_term(n):
    return 8 / ((4 * n - 3) * (4 * n - 1))


result = summation(50, cubes_term)
~~~

## Functions as General Method (通用模式)

有的函数并不实现具体的功能，更像是一些经验的累积，或者说通用的规律总结，比如这个函数

~~~python
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess
~~~

它表达的意思很简单：给一个初始值guess，通过close不停进行"对比"，对比后update新的guess，继续对比，最终达到"修正"的目的

我们来看一个应用该函数的例子：计算黄金比例（Golden Ratio）

~~~python
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def golden_update(guess):
    return 1 / guess + 1


def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


golden_ratio = improve(golden_update, square_close_to_successor)
~~~

improve把所有细节都留给了update和close两个函数，它只约定了最基本的模式，即[对比->更新]

## Nested Functions (嵌套函数)

假如我们要求一个数的平方根，用代码应该怎么写？ 我们知道，假如一个数不是完全平方根，那么开根号会出现无限循环，例如√2

上网查资料得知，求根公式是（巴比伦算式）：
![Babylonian Method](https://img2022.cnblogs.com/blog/2857827/202205/2857827-20220518095454434-17879308.png "Babylonian Method")

x是一个猜测值，a是要开方的值，因为目的是求√2，所以我们可以猜测根在1附近

所以要用代码实现的是，不断用巴比伦算式计算x，让它无限"靠近"真正的根，当然要约定一个终点，不要让它永无止境地计算下去

[对比->更新]，听起来像不像improve的工作？

但新问题出现了，improve的close和update都只接收一个传参，但巴比伦算式有两个参数x和a

The solution to both of these issues is to place function definitions inside the body of other definitions.

解决办法正是嵌套函数

~~~python
def sqrt(a):
    def sqrt_update(x):
        return average(x, a / x)

    def sqrt_close(x):
        return approx_eq(x * x, a)

    return improve(sqrt_update, sqrt_close)


def average(x, y):
    return (x + y) / 2


def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


# 这个就是"终点"
def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


result = sqrt(2)
~~~

*(其实就是不断的用二分法计算x，然后把结果再计算平方，最后和原来的a对比，直到满足approx_eq)*

## Functions as Return Values (返回其他函数的函数)

An important feature of lexically scoped programming languages is that locally defined functions maintain their parent
environment when they are returned.

这儿有点抽象，先看例子比较好理解

~~~python
def square(x):
    return x * x


def successor(x):
    return x + 1


def compose1(f, g):
    def h(x):
        return g(f(x))

    return h


square_successor = compose1(square, successor)
result = square_successor(12)
~~~

好吧还是很抽象不知道他在干嘛，但这儿有意思的是compose1在返回h的时候，连同它的父环境（parent
environment）一起保存并返回了，所以h(12)依旧可以调用g(f(12))，即successor(square(12))

## Currying (柯里化)

有的时候，我们可能要将f(x, y)变成g(x)(y)，而得到同样的结果，区别是f接受2个参数，而g只需要1个

下面的例子将pow(2,3)变成curried_pow(2)(3)

~~~python
def curried_pow(x):
    def h(y):
        return pow(x, y)

    return h


result = curried_pow(2)(3)
~~~

其实也是利用了Functions as Return Values例子中的特性，返回h的时候，连同父环境也保存下来了，即x=2。

composing programs的作者更变态，他说你不仅能手写一个curried function，还可以写两个函数来自动转换

~~~python
def curry2(f):
    def h(x):
        def g(y):
            return f(x, y)

        return g

    return h


curried_pow = curry2(pow)
result = curried_pow(2)(3)  # f=pow, x=2, y=3


def uncurry2(f):
    def h(x, y):
        return f(x)(y)

    return h


pow = uncurry2(curried_pow)
result = pow(2, 3)  # f=curried_pow, x=2, y=3
~~~

## Function Decorators (装饰器)

Python里有一个higher order functions的应用，就是装饰器。

例如这个trace装饰器，用来打印函数的名字和传参

~~~python
def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)

    return wrapped


@trace
def triple(x):
    return x * 3


triple(3)
~~~

这里@triple做了一件事，triple = trace(triple)，其实也是把wrapped的父环境保存了下来，所以才知道fn=triple