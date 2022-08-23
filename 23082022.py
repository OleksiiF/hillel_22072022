# first_word = "Hi"
#
#
# def get_message(name: str):
#     second_word = name.capitalize()
#     result = f"{first_word}, {second_word}"
#
#     return result

#
# message = get_message("John")
# print(f"{message=}")
#
# try:
#     print(f"{name=}")
# except NameError as error:
#     print(error)
#
# try:
#     print(f"{result=}")
#
# except NameError as error:
#     print(error)
############################################
# word = "GLOBAL"
#
#
# def new_word():
#     word = "LOCAL"
#     print(f"Cool word is {word}")
#
#
# new_word()
# print(f"{word=}")
############################################
# name = "Robbert"
# print(f"Initial name - {name}")
#
#
# def greetings():
#     global name
#     name = "Artur"
#     print(f"Hello {name}")
#
#
# def congratulations():
#     print(f"Congratulate {name}")
#
#
# greetings()
# print(f"Name after greetings - {name}")
# congratulations()
# print(f"Name after congratulations - {name}")
############################################
# def grandfather():
#     number = 1
#
#     def father():
#         number = 2  # it will be changed
#
#         def son():
#             nonlocal number
#             number = 3
#             print(f"son's {number=}")
#
#         son()
#
#         print(f"father's {number=}")
#
#     father()
#     print(f"grandfather's {number=}")
#
# grandfather()
############################################
# sequence = [1, 2, 3, 4]
#
#
# def modify(seq: list):
#     seq.append("New element")
#
#     return None
#
#
# modify(sequence)
# print(f"{sequence=}")
############################################
# def outside():
#     number = 0
#
#     def inside():
#         nonlocal number
#         number += 1
#         print(f"{number=}")
#
#     return inside
#
#
# func = outside()  # closure itself, inside func + env of inside func
# func()
# func()
# func()
############################################
# def factorial(n):  # 5!
#     if n == 0:
#         return 1
#
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))
############################################
# def main_decor(func_to_decor):
#     print("Inside start main_decor")
#
#     def warapper():
#         print("Inside start wrapper")
#         func_to_decor()
#         print("Inside end wrapper")
#
#     print("Inside finish main_decor")
#
#     return warapper
#
#
# def main_func():
#     print("Inside main function")
#
#
# main_func()  # usual call
# decorated_main_func = main_decor(main_func)
# decorated_main_func()  # decorated call
############################################
# def main_decor(func_to_decor):
#     print("Inside start main_decor")
#
#     def warapper():
#         print("Inside start wrapper")
#         func_to_decor()
#         print("Inside end wrapper")
#
#     print("Inside finish main_decor")
#
#     return warapper
#
#
# def main_func():
#     print("Inside main function")
#
#
# main_func = main_decor(main_func)
# main_func()  # decorated call
############################################
# def main_decor(func_to_decor):
#     print("Inside start main_decor")
#
#     def warapper():
#         print("Inside start wrapper")
#         func_to_decor()
#         print("Inside end wrapper")
#
#     print("Inside finish main_decor")
#
#     return warapper
#
#
# @main_decor
# def main_func():
#     print("Inside main function")
#
#
# main_func()  # decorated call
############################################
# def param_decorator(func_to_decor):
#     print("Inside start main_decor")
#
#     def param_warapper(argument):
#         print("Inside start wrapper")
#         func_to_decor(argument)
#         print("Inside end wrapper")
#
#     print("Inside finish main_decor")
#
#     return param_warapper

#
# @param_decorator
# def say_hi(name):
#     print(f"Hello {name}!")
#
#
# say_hi("World")
############################################
# def decorator_worker(decor_argument_1, decor_argument_2):
#     print("let's create a decorator")
#     print(
#         f"I've got {decor_argument_1=}, "
#         f"{decor_argument_2=} inside decorator_worker"
#     )
#
#     def param_decorator(func_to_decor):
#         print("inside start main_decor")
#         print(
#             f"I've got {decor_argument_1=}, "
#             f"{decor_argument_2=} inside param_decorator"
#         )
#
#         def param_warapper(func_argument):
#             print("inside start wrapper")
#             print(
#                 f"I've got {decor_argument_1=}, "
#                 f"{decor_argument_2=}, "
#                 f"{func_argument=} inside param_warapper"
#             )
#             func_to_decor(func_argument)
#             print("inside end wrapper")
#
#         print("inside finish main_decor")
#
#         return param_warapper
#
#     print("decorator created")
#
#     return param_decorator
#
#
# @decorator_worker("letter a", "letter b")  # NB!
# def say_hi(name):
#     print(f"Hello {name}!")
#
# say_hi("World")  # NB!
#
#
# # you can uncomment step by step algorithm, comment rows with NB!
# # decorator = decorator_worker("letter a", "letter b")
# # say_hi = decorator(say_hi)
# # say_hi("World")
############################################
# def print_hello(name: str) -> None:
#     print(f"Hello {name}")
#
#
# print_hello('World')
#
#
# def get_sum(operand_a: int or float, operand_b: int or float) -> int or float:
#     return operand_a + operand_b
#
#
# sum_result: int or float = get_sum(3, -4.9)
# print(f"{sum_result=}")
############################################
# def get_multiply(a: int or float, b: int or float, c=0) -> int or float:
#     """Return sum of multiplication of all arguments.
#
#     :param a: arg1
#     :type a: int
#     :param b: arg2
#     :type b: int
#     :param c: arg3, defaults to 0
#     :type c: int, optional
#
#     :raises ValueError: if arg1 is equal to arg2
#
#     :rtype: int or float
#     :return: multiplication of all arguments
#     """
#     if a == b:
#         raise ValueError('arg1 must not be equal to arg2')
#
#     return a * b * c
#
#
# get_multiply(1, 2, 3)