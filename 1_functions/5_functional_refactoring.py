a = int(input("Input number a: "))
b = int(input("Input number b: "))

action = input("Input action [+, -, /, *]: ")

if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "/":
    print(a / b)
else:
    print(a * b)
