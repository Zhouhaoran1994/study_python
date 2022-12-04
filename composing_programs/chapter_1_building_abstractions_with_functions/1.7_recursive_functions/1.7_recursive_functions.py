def unrecursive_sum_digits(n):
    total = 0
    while n > 10:
        total = total + n % 10
        n = n // 10
    return total + n


def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last = n // 10
        last = n % 10
        return sum_digits(all_but_last) + last


def cascade(n):
    """Print a cascade of prefixes of n."""
    # print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)


def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n - 1)


def play_bob(n):
    if n == 0:
        print("Alice wins!")
    # elif is_even(n):
    elif n % 2 == 0:
        play_alice(n - 2)
    else:
        play_alice(n - 1)


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def count_partitions(n, m):
    """Count the ways to partition n using parts up to m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)


# print(unrecursive_sum_digits(18117))
# print(sum_digits(18117))
# cascade(2013)
play_alice(20)  # Bob wins!
# print(fib(6))
print(count_partitions(6, 4))