# Позиционные, обязательные
def example_pos(a, b):
    print("a:", a, "b:", b)

# Именованные (имеющие значения по умолчанию)
def example_name(a=1, b=1):
    pass


# Комбинированная сигнатура
def foo(a, b=1):
    return a + b


# Передача по имени
example_pos(b=10, a=12)

"""
!Позиционные, могут идти ТОЛЬКО ПЕРЕД именованными,
как в сигнатуре так и при вызове функции
"""

# Функция принимающая любое количество неименованных аргументов
print("=== Любое количество позиционных аргументов ===")

def any_pos_args(*args):
    """" *args - кумулятивный аргумент
        в докстринге можно написать передаваемые аргументы"""
    print(args)

# кортеж
any_pos_args(1, 2, 3, 4) # (1, 2, 3, 4)

# получить значение по индексу
def get_pos_args(*args):
    print(args[1])

get_pos_args(1, 2, 3, 4) # 2

# Функция принимающая любое количество именованных аргументов
print("=== Любое количество именованных аргументов ===")

def any_kwargs(**kwargs):
    """"в докстринге можно написать передаваемые аргументы"""
    print(kwargs)

# словарь
any_kwargs(test=1, money=2, something=10) # {'test': 1, 'money': 2, 'something': 10}


def get_existed_kwargs(**kwargs):
    """"получить значение по существующему ключу"""
    print(kwargs['test'])

get_existed_kwargs(test=1, money=2, something=10) # 1

def get_unexisted_kwargs(**kwargs):
    """"получить значение по НЕсуществующему ключу,
        заранее неизвестно какие аргументы будут переданы"""
    if not kwargs.get('password'):
        print('Password is not in arguments')

get_unexisted_kwargs(test=1, money=2, something=10) # Password is not in arguments

# def error_unexisted_kwargs(**kwargs):
#    """Ошибка при получении значения по ключу, которого не оказалось"""
#     print(kwargs['password'])
# error_unexisted_kwargs(test=1, money=2, something=10) # KeyError: 'password'

# Функция принимающая любое количество любых аргументов
# Первыми нужно передавать позиционные, потом именованные
print("=== Любое количество любых аргументов, c учетом правил ===")

def any_of_any(*args, **kwargs):
    print(args)
    print(kwargs)


any_of_any(1, 2, 3, 4, test=1, money=2)

# Распаковка значений при передаче в функцию
print("=== Распаковка значений из списков и словарей ===")

# список из элементов
l = [1, 2, 3]

def len_tulpe(*args):
    """"расчитывает длину аргумента"""
    print(len(args))

# передадим аргумент
len_tulpe(l) # 1, так как в кортеже 1 элемент, в котором список ([1, 2, 3],)

# передадим *аргумент для распаковки списка или кортежа
len_tulpe(*l) # 3

# словарь
d = {"k1": "v1", "k2": "v2"}

def get_arg_dic(k1, k2):
    """"расчитывает длину аргумента"""
    print(k1, k2)

# передадим *аргумент для распаковки списка или кортежа
get_arg_dic(**d) # v1 v2
