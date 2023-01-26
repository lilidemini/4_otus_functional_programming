def power_19(arg):
    """"функция возведения в 19 степень"""
    return arg ** 19

print(power_19(2)) # 524288


# возведем 2 в 19 степень с lambda:
print(
    (lambda arg: arg ** 19)(2)
) # 524288

# lambda не создает объект, используется для единичного расчета,
# чтобы не создавать мусорные функции, используемые единожды

# Применим lambda для сортировки массива
names = [
    "Генадий Букин",
    "Тим Эпл",
    "Аркадий Волож",
    "Билл Гейтс",
    "Илон Маск",
    "Игорь Николаев",
    "Джеф Безос",
    "Майк Тайсон"
]

# 1. Сортируем по имени
print(sorted(names))

# 2. Сортируем по фамилии с функцией
def get_surname(name):
    return name.split(" ")[1]

sorted_names = sorted(names, key=get_surname)

print(sorted_names)

# 2. Сортируем по фамилии с lambda
print(sorted(names, key=lambda person: person.split(" ")[1]))
