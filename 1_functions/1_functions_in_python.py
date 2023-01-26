import inspect


# Объявление функции
def function(): # Имя функции
    pass  # Тело функции

def advanced_function(arg):
    """В докстринге кратко пишем что делает функция"""
    return arg  # Возвращаемое значение

def base_function():
    return 'base'

# Сигнатура функции - имя функции, кол-во и порядок аргументов, возвращаемого значения.

print("=== Функция является объектом ===")

# список атрибутов функции по алфавиту
print(dir(advanced_function)) # ['__annotations__', '__builtins__', '__call__', ... ]

# название функции
print("name:", advanced_function.__name__) # name: advanced_function

# получить код объекта и расположение функции в файле
print("code:", advanced_function.__code__) # code: <code object advanced_function at 0x000001FCFE1DE600, file "C:\PycharmProjects\4_otus\1_functions_in_python.py", line 9>

# Получить докстрингу финкции (докстринга - отдельный объект)
print("code:", advanced_function.__doc__) # В докстринге кратко пишем что делает функция

# получить тип функции
print("type:", type(advanced_function))


print("=== Использование функции как объекта первого класса ===")

# Хранить в структурах данных
my_functions = [base_function, 10, None]
print(my_functions) # [<function base_function at 0x000001B76986EB90>, 10, None]

# Присваивать переменным
my_arg = advanced_function
my_arg(10)
print('name:', my_arg.__name__) # name: advanced_function


# Передавать в качестве аргумента другим функциям
advanced_function(base_function)

# Возвращать из функций
result = advanced_function(base_function)
# выполнится функция в аргументе
print(result()) # base
# аналогичный результат:
print(advanced_function(base_function())) # base
print(advanced_function(base_function)()) # base

# Ошибка при передаче функции другим функциям вместо аргумента
# error = advanced_function(base_function())
# print(error()) # TypeError: 'NoneType' object is not callable

print("=== Возвращаемые значения ===")

def example1():
    print('example1')
    # по-умолчанию return None

def example2():
    return "example2"

print(example1(), example2()) # None example2
# функция example1 вернула None, так как нет return, поэтому по-умолчанию return None

