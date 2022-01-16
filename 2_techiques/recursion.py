def example(count):
    if not count:
        return count
    print(count)
    return example(count - 1)


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


example(10)
