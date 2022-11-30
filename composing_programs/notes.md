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

*(我觉得approx_eq也是一个general method，因为它有通用性)*

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
~~~

*(其实就是不断的用二分法计算x和a，然后把结果再计算平方，最后和原来的a对比，直到满足approx_eq)*

## Functions as Return Values (返回其他函数的函数)