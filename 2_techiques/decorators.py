def make_nickname_cool(func):

    def wrapped():
        return f"------[{func()}]-------"

    return wrapped

# с декоратором
# @make_nickname_cool
def my_nickname():
    return 'Lilia'

print(my_nickname()) # -----[Lilia]-------


# то же самое без  декоратора (закоментить строку с собачкой)
my_nickname = make_nickname_cool(my_nickname)
print(my_nickname()) # ------[Lilia]-------
