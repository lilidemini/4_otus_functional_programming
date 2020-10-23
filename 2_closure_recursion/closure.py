def mul(times):

    def wrapper(x):
        print(f"{times} * {x} =", end=" ")
        return times * x

    return wrapper


ten_times = mul(10)

print(ten_times(2))
print(ten_times(3))

five_times = mul(5)

print(five_times(2))
print(five_times(3))
