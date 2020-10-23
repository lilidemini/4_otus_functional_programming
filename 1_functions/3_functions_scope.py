A = 1

# # example 1
# def change():
#     A = A + 5
#     print(A)
#
# change()


# # example 2
# def change():
#     global A
#     A = A + 5
#     print(A)
#
# change()

print("After calling change() GLOBAL_A =", A)


# # example 3
# def change():
#     A = 10
#
#     def change_inside():
#         # nonlocal A - ?
#         # global A - ?
#         A = A + 5
#
#     print("before change_inside() inside A =", A)
#
#     change_inside()
#
#     print("after change_inside() inside A =", A)
#
# change()
#
# print("outside A =", A)
