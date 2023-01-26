# Константы - неизменяемые переменные, объявляются верхним регистром в глобальных переменных
ARGUMENT_CONSTANTA = 1

def change():
    """"некорректная функция, изменяющая константу, в результате ошибка"""
    ARGUMENT_CONSTANTA = ARGUMENT_CONSTANTA + 5
    print(ARGUMENT_CONSTANTA) # UnboundLocalError: local variable 'A' referenced before assignment

# change()


# example 2
def change():
    """"функция изменит константу"""
    global ARGUMENT_CONSTANTA
    ARGUMENT_CONSTANTA = ARGUMENT_CONSTANTA + 5
    print(ARGUMENT_CONSTANTA)

change() # 6
print("After calling change() GLOBAL_A =", ARGUMENT_CONSTANTA)
