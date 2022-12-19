# 计算函数调用的次数 (times)
def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)

    counted.call_count = 0
    return counted


# 计算函数运行所需的空间 (space)
def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
        counted.open_count -= 1
        return result

    counted.open_count = 0  # active的env数
    counted.max_count = 0  # 最大的active env数
    return counted


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    fib = count(fib)
    print(fib(19))  # 4181
    print(fib.call_count)  # 13529

    fib = count_frames(fib)
    print(fib(24))  # 46368
    print(fib.open_count)  # 0
    print(fib.max_count)  # 19
