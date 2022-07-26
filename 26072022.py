# sum of two numbers
# result = 1 + 1  # there is sum of numbers
# print("Result", result)
# print("Result", type("Result"))
# print(result, type(result))

# number_a = 7          # straight method
# number_b = number_a   # reference to another object
#
# print(number_a, number_b)


# number_a, number_b = 4, 12 + 3  # multiple assignment exist, not recommended
# print(number_a, number_b)
#
# value = 10

#
# value int;
# value = 3

# value: int = 13  # annotation
# print(value, type(value))

# value_str = "some string"
# value_int = 13
# result = value_str + value_int
# print(result)

# new_variable = 13
# print(new_variable, type(new_variable))
#
# new_variable = "my shiny string"
# print(new_variable, type(new_variable))


# my_int_value_a = 5
# my_int_value_b = 5
#
# print(id(6))
#
# print(id(id))
# print(id(my_int_value_a))
# print(id(my_int_value_b))
#
# print(id(346545))

# my_cool_str = "мій кльовий рядок111"
# my_cool_str_2 = 'ще літерки'
# my_cool_str_3 = '''А що так можно було!?!'''
# my_cool_str_4 = """та шо тут коється?!"""
#
# my_cool_str_5 = str(1)
# my_cool_str_6 = str(5.6)

# print(my_cool_str)
# print(my_cool_str_2)
# print(my_cool_str_3)
# print(my_cool_str_4)
# print(my_cool_str_5, type(my_cool_str_5))
# print(my_cool_str_6)

# multiplication = my_cool_str_3 * 2
# print(multiplication)
#
# sum_ = my_cool_str + "" + my_cool_str_2 + " " + my_cool_str_2
# print(sum_)
#
# usual_string = "New line here \n and tabulation \t here"
# print(usual_string)

# escaping_characters = "New line here \\n and tabulation \\t here"
# print(escaping_characters)
#
# raw_string = r"New line here \n and tabulation \t here"  # raw - as is
# print(raw_string)


# format_string = f"Put some value here - {my_cool_str}"
# print(format_string)
#
# format_string_2 = f"More magic - {my_cool_str_3=}"
# print(format_string_2)

# username: str = input("Please tell me your name ")
# result = f"Hello {username}, nice to e-meet you! {12354}"  # {} -> str()
#
# print(result)

# There is not only one string formatting method,
# but f-string is modern

# value_1 = int(5.9)  # removes decimal, doesn't round
# print(value_1, type(value_1))
#
# value_2 = int("3")
# print(value_2, type(value_2))
#
#
# value_1 = float("10.1")
# print(value_1, type(value_1))
#
# value_2 = float("3.7")
# print(value_2, type(value_2))


# sum_ = value_1 + value_2 + value_2
# print("SUM", sum_, type(sum_))
#
#
# subtraction = value_1 - value_2
# print(subtraction, type(subtraction))
#
#
# multiplication = value_1 * value_2
# print(multiplication, type(multiplication))

# exponentiation = value_2 ** 3
# print(exponentiation, type(exponentiation))


# square_root = value_2 ** 0.5
# print(square_root, type(square_root))

# division = value_1 / value_2  # if int or float are possible, the float will be used
# print(division, type(division))

#
# division_remainder = value_1 % value_2  # 5 % 3
# print(division_remainder, type(division_remainder))

# division_remainder_negative = -7 % 3  # MATH MEANING
# print(division_remainder_negative, type(division_remainder_negative))

# division_int = value_1 // value_2
# print(division_int, type(division_int))


# division_int_negative = -20 // 3  # MATH MEANING
# print(division_int_negative, type(division_int_negative))

#
# same_value = 3
# same_value *= 2  # same_value = same_value * 2
# print(same_value)
#
#
# same_value /= 3
# print(same_value)
#
# same_value += 1
# print(same_value)
#
# same_value -= 1
# print(same_value)
#
# same_value **= 4
# print(same_value)
#
# same_value %= 1
# print(same_value)
