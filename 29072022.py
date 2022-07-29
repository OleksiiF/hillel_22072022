none_obj = None
# print(type(none_obj), none_obj)

# variable = type(none_obj)
# result = print("Look at me", variable)
#
# print(result, type(result))

#####################################################
# value_true = True
# value_false = False
# print(type(value_true))
# print(type(value_false))
#
# comparison_result: bool = 3 > 5
# print(comparison_result)
#
# comparison_result_1: bool = 3 < (5 - 1) * 2
# print(comparison_result_1)

#####################################################
# or, and, not
# is_true = True or False
# print(f"{is_true=}")
#
# is_true_1 = False or True
# print(f"{is_true_1=}")


# is_true_2 = True and False
# print(f"{is_true_2=}")
#
# is_true_3 = False and True
# print(f"{is_true_3=}")
#
# is_true_4 = True and True
# print(f"{is_true_4=}")
#
# is_true_5 = False and False
# print(f"{is_true_5=}")

# is_true_6 = (False and False) or True
# print(f"{is_true_6=}")

#
# logical_negation = not False
# print(logical_negation)
#
# logical_negation_1 = not True
# print(logical_negation_1)
#
# logical_negation_2 = not not not not True
# print(logical_negation_2)

####################################################
# is_belong = "el" in "Hello world"  # case is important
# print(is_belong)

####################################################
# x=45987569805479805409879875687956
# y=45987569805479805409879875687956
#
# is_ident = x is y  # id(x) == id(y)
# print(is_ident)
# print(id(x), id(y))
#######################################################
# bool_zero = bool(0)  # return True or False
# print(f"{bool_zero=}")
#
# bool_negative = bool(-1.1)  # "-4"
# print(f"{bool_negative=}")
#
#
# one_space_str = bool("cfgdf") or bool("")  # '', '''''', """""" ||| True or False
# print(f"{one_space_str=}")

# bool_bool = bool(True)
# print(bool_bool)
#
# bool_false = bool(False)
# print(f"dfglkjdlfkjg {bool_false=} hfl;gkjhlfdkgjh")  # bool_false=False
#
# str_false = bool("False")
# print(f"{str_false=}")
#
#
# bool_none = bool(None)
# print(f"{bool_none=}")
#
#
# # bool() -> False for 0, None, False, "", |||   [], {}, dict()
#
# python_result = not ("***" in "Python sadjkfhskajdfhkjasdhf")  # not False
# print(python_result)
################################################################################
# string_1 = "fdsgdfgd"
# string_1 += "D"  # "fdsgdfgdD"
# print(string_1)

# str_value = "some cool string"  # 0, 1, 3, 4, 5
# print("index 0", "some cool string"[0])
# print("index 4", str_value[4])
#
# str_index = 3
# print("index 3", str_value[str_index])
#
# last_symbol = -1
# print("last symbol", str_value[last_symbol])
#
# # print("will rise exception", str_value[1000])  # will rise IndexError
##########################################################################
# str_for_slice = "we get familiar with index and slices"
#
# print("slice between 3 and 7 --> ", str_for_slice[3:7])  # don't include
# print("slice between 3 and -1 --> ", str_for_slice[3:-1])
# print("slice between -10 and -2 --> ", str_for_slice[-10:-2])  # -3, -2, -1, 0, 1, 2, 3
#
# print("slice between -10 and till the end --> ", str_for_slice[-10:])
# print("slice start and till 6 --> ", str_for_slice[:6])
# print("copy of the string --> ", str_for_slice[:])
#
# print("end of the slice out of string --> ", str_for_slice[10:200])
# print("slice out of string --> ", str_for_slice[100:200])  # ""
#
# print("slice with step 2 --> ", str_for_slice[2:20:2])  # start:stop:step
# print("straight string --> ", str_for_slice[::])  # step 1 by default
# print("reversed string --> ", str_for_slice[::-1])
# print("reversed substring -->", str_for_slice[:-10:-1])
##########################################################################
# val_int = "1232432"
# new_string = f"my tesT {val_int} strINg with \n speci2al NON printable Symbols for string methods"  # 69
# print("length of string", len(new_string))
# #
# # print(bool(len("")))  # False
#
# print("swap the case", new_string.replace("2", "ssdaf"))

# print("is a string made of digit", val_int.isdigit())
# print("is a string made of letters", new_string.isalpha())
# print("is a string made of digits or letters", new_string.isalnum())
# print("give me first capital", new_string.capitalize())
# print("swap the case", new_string.swapcase())
# print("swap the case", new_string.title())