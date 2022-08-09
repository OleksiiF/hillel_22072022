# empty_tuple = tuple()
# print(f"{type(empty_tuple)=}, {empty_tuple=}")

# alphabet = tuple("abcdefghijklmnopqrstuvwxyz")
# print(f"{type(alphabet)=}, {alphabet=}")
# print(f"{len(alphabet)=}")

# example = "a", "b", "c"  # try to avoid, because of implicitness
# print(f"{type(example)=}, {example=}")

# easy_tuple = (1, 2, 3, 4)
# print(f"{type(easy_tuple)=}, {easy_tuple=}")

# not_so_easy = ("one string")  # it is string
# print(f"{type(not_so_easy)=}, {not_so_easy=}")

# different_types = (-3, None, "I'm inside tuple", True, 4.5)
# print(f"{type(different_types)=}, {different_types=}")

# tuple_inside = (1, True, different_types, None)
# print(f"{type(tuple_inside)=}, {tuple_inside=}")
#
# alphabet = tuple("abcdefghijklmnopqrstuvwxyz")
# print(f"{len(alphabet)=}\n{alphabet[-10:-15:-1]=}\n{alphabet[13]=}")
#
# for i, letter in enumerate(alphabet):
#     if i % 2 == 0 and letter in "jklmnopq":
#         print(letter)
#######################################################
# number_a, number_b = 4, 12
# print(number_a, number_b)
#
# number_a, number_b = number_b, number_a
# print(number_a, number_b)

# number_a, number_b = (4, 12)  # tuple is unpacked
# print(number_a, number_b)
#
# number_a, number_b = (number_b, number_a)  # tuple is unpacked
# print(number_a, number_b)
############################################################
# empty_list = list()
# print(f"{type(empty_list)=}, {empty_list=}")

# alphabet = list("abcdefghijklmnopqrstuvwxyz")
# print(f"{type(alphabet)=}, {alphabet=}")

# numbers = list("12345")
# print(f"{type(numbers)=}, {numbers=}")
#
# numbers = tuple(numbers)
# print(f"{type(numbers)=}, {numbers=}")

# different_types = [-3, None, "I'm inside list", True, 4.5]
# print(f"{type(different_types)=}, {different_types=}")
#
#
# list_inside = [1, True, different_types, None]
# print(f"{type(list_inside)=}, {list_inside=}")
####################################################################

# alphabet = list("abcdefghijklmnopqrstuvwxyz")
# print(f"{len(alphabet)=}\n{alphabet[-10:-15:-1]=}\n{alphabet[13]=}")
#
# for i, letter in enumerate(alphabet):
#     if i % 2 == 0 and letter in "jklmnopq":
#         print(letter)
####################################################################
# text = "some text here"
#
# list_obj = list(text)
# tuple_obj = tuple(text)
# print(f"{id(list_obj)=}, {id(tuple_obj)=}")
#
# list_obj += [1, 2, 3]
# tuple_obj += (1, 2, 3)
# print(list_obj)
# print(tuple_obj)
# print(f"{id(list_obj)=}, {id(tuple_obj)=}")
####################################################################
# base_list = [1, 2]
# print(f"{base_list=}")
#
# derivate = [base_list] * 3
# print(f"{derivate=}")
#
# base_list.append(3)
# print(f"{base_list=}")
# print(f"{derivate=}")
#
# # you should use .copy() to avoid this behavior
# base_list = [1, 2]
# print(f"{base_list=}")
#
# derivate = [base_list.copy()] * 3
# print(f"{derivate=}")
#
# base_list.append(3)
# print(f"{base_list=}")
# print(f"{derivate=}")
####################################################################
some_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# some_list.append(-1)
#
# print(f"{some_list=} | {id(some_list)=}")

# some_list.extend([34, True, 72])
# print(f"{some_list=} | {id(some_list)=}")

# some_list.insert(2, 0.0001)
# print(f"{some_list=} | {id(some_list)=}")

# try:
#     some_list.remove(-3)
#     print(f"{some_list=} | {id(some_list)=}")
# except ValueError as e:
#     print(e)

# element = some_list.pop(3)
# print(f"{some_list=} | {id(some_list)=} | {element=}")

# folders = "path/to/my/file/sound.mp3".split("/")
# print(f"{type(folders)=}, {folders=}")

# joined_string = "/".join(folders)
# print(f"{type(joined_string)=}, {joined_string=}")

# folders.sort()
# print(f"{type(folders)=}, {folders=}")

# sorted_list = sorted(folders)
# print(f"{folders=} | {id(folders)=}")
# print(f"{sorted_list=} | {id(sorted_list)=}")
#
# rev_sorted_list = sorted(folders, reverse=True, key=len)
#
# print(f"{folders=} | {id(folders)=}")
# print(f"{rev_sorted_list=} | {id(rev_sorted_list)=}")
#################################################################
# el_a, el_b, el_c, *leftover = (1, 2, 3, 4)
# print(f"{el_a=}, {el_b=}, {el_c=}, {leftover=}, {type(leftover)=}")
#
# some_values = [1, "a", None, True]
#
# print(some_values)
# print(*some_values)  # equal to print(1, "a", None, True) != print(f"{1} {'a'} {None} {True}")
#########################################################################################
# [x for x in iterable] - general formula

# mix_list = ["1", "2", "f", "5", "poi", "j", "4", "df"]
# digits = []
#
# for el in mix_list:
#     if el.isdigit():
#         digits.append(el)
#
#     else:
#         digits.append(-1)
#
# gen_list = [el for el in mix_list if el.isdigit()]
# gen_list_ternary = [el if el.isdigit() else -1 for el in mix_list]
#
# print(f"{digits=}")
# print(f"{gen_list=}")
# print(f"{gen_list_ternary=}")
