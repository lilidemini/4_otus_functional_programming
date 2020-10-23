from functools import partial


# Каррирование (от англ. currying, иногда — карринг) — преобразование функции от многих аргументов в набор функций,
# каждая из которых является функцией от одного аргумента. По факту же просто от меньшего числа аргументов.

def money_transfer(client_from, client_to, amount, currency, pay_system):
    print(f"Transfer from: {client_from} to: {client_to} made for {amount} {currency} with {pay_system}")


# Мы можем сделать так
def ruble_visa_transfer(client_from, client_to, amount):
    return money_transfer(client_from, client_to, amount, "RUB", "VISA")


def one_euro_mastercard_transfer(client_from, client_to):
    return money_transfer(client_from, client_to, 1.00, "EUR", "MasterCard")


# Можно воспользоваться функцией partial
dollar_visa_transfer = partial(money_transfer, currency="USD", pay_system="VISA")
dollar_visa_transfer("Donald", "Joe", 100)
