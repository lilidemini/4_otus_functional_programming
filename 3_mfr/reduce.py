import functools


def foo(x, y):
    print(x, " * ", y)
    return x * y


some_range = range(3, 10)

result = functools.reduce(foo, some_range)

print("result:", result)
